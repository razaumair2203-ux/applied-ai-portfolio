"""Sanitized Clear Run edge-detector excerpt.

Representative team-developed source published as deployment evidence.
Umair Raza's role in Clear Run is technical direction, systems engineering,
integration, experiment/validation framing and team leadership; this file is not
presented as sole personal code authorship.

The complete private runtime includes additional UI, telemetry, geolocation and
mission-integration code. Programme-specific paths and unrelated details are
omitted here.
"""

from __future__ import annotations

import time
from dataclasses import dataclass

import cv2
import numpy as np
from ultralytics import YOLO

try:
    from sahi import AutoDetectionModel
    from sahi.predict import get_sliced_prediction
except ImportError:  # optional precision mode
    AutoDetectionModel = None
    get_sliced_prediction = None


@dataclass
class Detection:
    class_id: int
    class_name: str
    confidence: float
    bbox_pixels: tuple[float, float, float, float]
    center_pixel: tuple[float, float]
    norm_center: tuple[float, float]


def jetson_csi_pipeline(
    sensor_id: int = 0,
    capture_width: int = 1920,
    capture_height: int = 1080,
    display_width: int = 1280,
    display_height: int = 720,
    framerate: int = 30,
) -> str:
    """GStreamer pipeline used for CSI capture on NVIDIA Jetson."""
    return (
        f"nvarguscamerasrc sensor-id={sensor_id} ! "
        f"video/x-raw(memory:NVMM), width=(int){capture_width}, "
        f"height=(int){capture_height}, format=(string)NV12, "
        f"framerate=(fraction){framerate}/1 ! "
        "nvvidconv ! "
        f"video/x-raw, width=(int){display_width}, height=(int){display_height}, "
        "format=(string)BGRx ! videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink drop=1 max-buffers=1 sync=false"
    )


class FODDetector:
    """YOLO / optional SAHI detector for GPU edge inference."""

    def __init__(
        self,
        model_path: str,
        *,
        use_sahi: bool = False,
        conf_thresh: float = 0.35,
        device: str = "0",
        slice_size: int = 640,
        overlap_ratio: float = 0.2,
    ) -> None:
        self.model_path = model_path
        self.use_sahi = use_sahi
        self.conf_thresh = conf_thresh
        self.device = device
        self.slice_size = slice_size
        self.overlap_ratio = overlap_ratio

        self.model = None
        self.sahi_model = None
        self._load_model()

    def _load_model(self) -> None:
        if self.use_sahi and AutoDetectionModel is not None:
            self.sahi_model = AutoDetectionModel.from_pretrained(
                model_type="ultralytics",
                model_path=self.model_path,
                confidence_threshold=self.conf_thresh,
                device=(
                    f"cuda:{self.device}"
                    if self.device not in {"cpu", "-1"}
                    else "cpu"
                ),
            )
        else:
            # Ultralytics accepts .pt, .onnx and TensorRT .engine model paths.
            self.model = YOLO(self.model_path, task="detect")

    def detect(self, frame: np.ndarray) -> tuple[list[Detection], float]:
        """Return normalized detections plus measured inference time in ms."""
        started = time.perf_counter()
        height, width = frame.shape[:2]
        detections: list[Detection] = []

        if self.sahi_model is not None and get_sliced_prediction is not None:
            result = get_sliced_prediction(
                frame,
                self.sahi_model,
                slice_height=self.slice_size,
                slice_width=self.slice_size,
                overlap_height_ratio=self.overlap_ratio,
                overlap_width_ratio=self.overlap_ratio,
                verbose=0,
            )

            for prediction in result.object_prediction_list:
                x1, y1, x2, y2 = (
                    prediction.bbox.minx,
                    prediction.bbox.miny,
                    prediction.bbox.maxx,
                    prediction.bbox.maxy,
                )
                u = (x1 + x2) / 2.0
                v = (y1 + y2) / 2.0
                detections.append(
                    Detection(
                        class_id=int(prediction.category.id),
                        class_name=str(prediction.category.name),
                        confidence=float(prediction.score.value),
                        bbox_pixels=(x1, y1, x2, y2),
                        center_pixel=(u, v),
                        norm_center=(u / width, v / height),
                    )
                )
        else:
            result = self.model.predict(
                source=frame,
                conf=self.conf_thresh,
                device=self.device,
                verbose=False,
            )[0]

            for box in result.boxes:
                x1, y1, x2, y2 = map(float, box.xyxy[0].cpu().numpy())
                class_id = int(box.cls[0].cpu().numpy())
                u = (x1 + x2) / 2.0
                v = (y1 + y2) / 2.0
                detections.append(
                    Detection(
                        class_id=class_id,
                        class_name=str(result.names[class_id]),
                        confidence=float(box.conf[0].cpu().numpy()),
                        bbox_pixels=(x1, y1, x2, y2),
                        center_pixel=(u, v),
                        norm_center=(u / width, v / height),
                    )
                )

        elapsed_ms = (time.perf_counter() - started) * 1000.0
        return detections, elapsed_ms


def open_jetson_camera(sensor_id: int = 0) -> cv2.VideoCapture:
    """Representative headless camera setup used by the aerial runtime."""
    return cv2.VideoCapture(jetson_csi_pipeline(sensor_id), cv2.CAP_GSTREAMER)
