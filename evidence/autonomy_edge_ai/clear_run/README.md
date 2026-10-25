# Clear Run: detector code and field logs

## What this code shows

- [Edge detector excerpt](edge_detector_excerpt.py) — the Jetson detector interface: YOLO with optional SAHI slicing, `.pt`/`.onnx`/TensorRT models, USB, CSI and RTSP cameras, and structured detection output.
- [Field-log summary](field_trial_snapshot.json) — early detection flights (Sep 2026): 8 trial videos (5 RGB, 3 thermal), 12 detection events across 8 classes, confidence 0.55–0.89.
- [Mission verification matrix](mission_verification_matrix.json) — the pass criteria for each stage, from detection to retrieval.

The full system runs RGB and thermal cameras through separate FP16 TensorRT models, geolocates detections and sends them over MAVLink to the ground station.

Current field results (30 trials, 42/45 objects retrieved) are in the [Clear Run engineering case](../../../domains/01-autonomy-edge-ai/CLEAR_RUN_ENGINEERING_CASE_2026_10.md).

## How to run

```bash
python evidence/autonomy_edge_ai/clear_run/validate_field_evidence.py
```

Checks the summary and matrix files for consistency. No dependencies.

[Back to code and data](../../README.md) · [Back to portfolio](../../../README.md)
