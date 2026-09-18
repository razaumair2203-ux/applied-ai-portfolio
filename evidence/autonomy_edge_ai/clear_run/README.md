# Clear Run — public deployment evidence extract

This folder publishes a **sanitized, non-sensitive evidence extract** from the private Clear Run programme so that edge-AI deployment claims in the portfolio are technically inspectable.

Clear Run is team-developed work at CAE/NUST. **Umair Raza's role is technical direction, systems engineering/integration, experiment and validation framing, and team leadership; this folder does not claim sole authorship of the team source code.**

## What the underlying source demonstrates

The working aerial AI code implements a real-time detector intended for NVIDIA Jetson platforms with:

- Ultralytics YOLO inference;
- optional SAHI sliced prediction for small FOD;
- CUDA/GPU execution;
- model paths supporting `.pt`, `.onnx` and TensorRT `.engine` artefacts;
- USB, CSI/GStreamer, RTSP and recorded-video input paths;
- normalized detection outputs with bounding boxes, class/confidence and image centres;
- runtime latency/FPS measurement;
- headless flight execution and optional annotated-video recording;
- a MAVLink telemetry injector path for forwarding FOD detections into the mission system.

A separate integrated dual-camera runtime in the programme uses:

- RGB and passive-IR cameras;
- independent FP16 TensorRT engines;
- concurrent camera processing;
- independent per-stream model management;
- synchronized recording;
- camera-tagged detection events;
- geolocation and compact MAVLink transmission;
- GCS decoding and mission display.

## Field-evidence snapshot

The public portfolio now carries an aggregate, non-location-sensitive snapshot from the **10 September 2026** evidence review:

- **8 unique trial videos**: 5 RGB and 3 passive-IR, approximately **12 min 45 s** total;
- **12 structured RGB event records** across **8 reported classes**;
- model-confidence range **0.5488–0.8887**, mean **0.7125**;
- logged altitude range **1.176–2.334 m AGL**, mean **2.069 m**;
- event fields include image centre, target coordinates, UAV position/orientation and altitude.

These numbers describe available event/log evidence. The reviewed batch has no surveyed target coordinates, ground-truth detection denominator or completed retrieval outcomes, so it cannot support precision/recall, geolocation-error or mission-success claims.

- [`field_trial_snapshot.json`](field_trial_snapshot.json) — machine-readable aggregate evidence
- [`mission_verification_matrix.json`](mission_verification_matrix.json) — detection-to-retention verification gates
- [`validate_field_evidence.py`](validate_field_evidence.py) — zero-dependency consistency check used in CI

The mission matrix makes the open gates explicit: geolocation accuracy, GCS→UGV acknowledgement, terminal approach, physical capture, post-movement retention and complete mission success each require their own declared measurement rather than inheriting confidence from an upstream subsystem.

## Inspectable excerpt

[`edge_detector_excerpt.py`](edge_detector_excerpt.py) contains a reduced public extract of the detector contract: Jetson/GStreamer camera handling, YOLO/SAHI model loading and detection-output structure. It excludes programme-specific paths and unrelated runtime/UI code.

The purpose is not to publish the complete Clear Run repository. It is to demonstrate that the portfolio's edge-deployment claims trace to working implementation rather than narrative alone.

## System evidence represented in the case study

The [Clear Run / TIR-FOD case study](../../../domains/01-autonomy-edge-ai/clear-run-tir-fod.md) documents the broader stack:

```text
RGB camera ──> FP16 TensorRT model ──┐
                                     ├─> detections ─> geolocation ─> MAVLink/REST ─> GCS
IR camera  ──> FP16 TensorRT model ──┘

GCS target handling ─> UGV mission/navigation ─> terminal retrieval subsystem
```

TIR-FOD's published flight-test measurements provide the quantitative edge-inference evidence; Clear Run demonstrates the broader multi-stream/system integration.

[Back to technical evidence index](../../README.md) · [Back to portfolio](../../../README.md)
