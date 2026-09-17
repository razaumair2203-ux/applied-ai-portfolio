# TIR-FOD / Clear Run — deployed edge AI for runway inspection and autonomy

This programme spans the full path from dataset/model development to airborne edge inference and multi-agent systems integration.

## TIR-FOD — LWIR dataset, multi-model AI and controlled evaluation

**Public dataset:** [TIR-FOD v1.2 — Zenodo DOI 10.5281/zenodo.22546586](https://doi.org/10.5281/zenodo.22546586)  
**Inspectable result data:** [selected benchmark snapshot](../evidence/tir-fod/benchmark_results.json)

The released study contains:

- **3,499** single-shot LWIR source frames acquired over real runway surfaces;
- **5,593** bounding-box annotations across **23 FOD classes**;
- a 29,243-image stored archival pool after offline augmentation;
- frozen source-lineage-aware partitions and automated leakage checks;
- blind second annotation on **338 frames**;
- **29 completed training runs**;
- a multi-generation detector study across **YOLOv8n, YOLOv8s, YOLOv8m, YOLO11s, YOLO11m and YOLO12s**;
- repeated-seed evaluation, class/size diagnostics, contamination tests and acquisition-block generalisation studies.

The best observed three-seed YOLOv8n mean mAP@[.50:.95] is **0.8603 ± 0.0017**. A size-matched contamination experiment produced an **8.52 ± 0.19 percentage-point** uplift, demonstrating why lineage control matters more than reporting a single attractive score. On the shared 12-class experiment, acquisition-block-disjoint evaluation produced **0.7410 ± 0.0423**, compared with **0.8223 ± 0.0070** for frame-level partitioning.

### Multi-model LWIR work

Beyond the published six-configuration benchmark, current project work includes **multi-model LWIR fusion using YOLO-family detectors**, extending comparative model evaluation into fused inference. The detailed fusion implementation remains part of the underlying project evidence while this public page records the capability and its relationship to the released benchmark.

## ML experiment and model-lifecycle engineering

The model-development workflow is implemented as reproducible engineering rather than ad-hoc training:

- configuration-driven experiment queues;
- resumable execution that skips completed runs;
- controlled protocol deviations recorded per configuration;
- deterministic multi-seed training;
- validation-based checkpoint selection followed by held-out test evaluation;
- per-class AP, mAP, precision, recall, parameter count and training-duration capture;
- preserved run histories, initializer checksums and experiment manifests;
- public reproducibility artifacts;
- model conversion for edge execution;
- field throughput, power and thermal measurement.

This is practical model lifecycle management: train, compare, select, package, deploy, measure and iterate.

## TIR-FOD — flight-tested Jetson / TensorRT deployment

The thermal detector was deployed onboard a **Jetson Orin Nano** and exercised through repeated runway UAV trials with a thermal payload and GNSS/Pixhawk flight stack.

The flight-tested system demonstrated:

- thermal image acquisition in the airborne environment;
- onboard TensorRT inference;
- transmission of detection outputs to the operator interface;
- successful detections plus recorded misses, false detections and misclassifications;
- ten-run mean **25.0 FPS TensorRT inference**;
- ten-run mean **15.6 FPS end-to-end** on the 640 × 512 LWIR stream;
- approximately **16–18 W** compute-and-camera subsystem power during the reported trials;
- reported Jetson module temperatures of approximately **55–70 °C**.

This is a completed edge-AI system-integration and flight-test demonstration, not a desktop-only benchmark.

## Clear Run — deployed dual-camera AI runtime

Clear Run takes the perception stack into a broader UAV–GCS–UGV autonomy system. The current source/runtime contains an operational aerial AI layer on **Jetson Orin Nano** with:

- **1080p RGB** and **passive IR** camera streams;
- independent **FP16 TensorRT engines** for RGB and IR inference;
- concurrent multi-stream processing;
- **YOLOv12 + SAHI-style sliced inference** for small-object detection in the active aerial stack;
- support for TensorRT `.engine`, ONNX and Ultralytics model paths;
- CUDA/GPU execution on Jetson;
- independent model management so RGB and IR models can be changed without stopping the other stream;
- synchronized RGB/IR video recording with bounding-box overlays;
- CSV/JSON mission records with camera-tagged detection events;
- camera-source handling for USB, CSI/GStreamer, RTSP and recorded video;
- real-time detection latency/FPS reporting;
- geolocation and coordinate transformation;
- MAVLink injection and bandwidth-aware telemetry;
- Flask/Leaflet ground-control integration using MAVLink/REST data;
- a common detected-FOD list carrying RGB/IR source tags into the mission workflow.

The resulting architecture is **multi-model and multi-stream at the edge**: two sensing streams, independent optimized inference engines and a common telemetry/GCS layer rather than a single offline detector.

```text
RGB camera ──> FP16 TensorRT model ──┐
                                     ├─> camera-tagged detections ─> geolocation ─> MAVLink/REST ─> GCS
IR camera  ──> FP16 TensorRT model ──┘

GCS target handling ─> UGV mission / navigation ─> terminal retrieval subsystem
```

## Systems-integration status

AI inference, dual-camera processing, telemetry/GCS integration, day/night detection trials, UGV computing/navigation hardware and the retrieval mechanism are all part of the active system. Current engineering work is focused on closing and quantitatively validating the final **detection-to-physical-retention** chain: target hand-off, terminal alignment, collection and retention KPIs.

That remaining systems-validation work is a maturity statement about the **complete robotic mission**, not a qualification on whether the AI has been deployed.

## My role

I lead the applied R&D / systems-engineering effort: technical direction, architecture and interfaces, experiment design, model/evaluation strategy, deployment review, integration gates, performance/KPI definition, multidisciplinary student/research teams and publication development.

## Research status

- TIR-FOD dataset v1.2 is publicly released on Zenodo.
- TIR-FOD IEEE Access manuscript is under revision in 2026.
- Clear Run is under active field integration and measurement.

[Back to portfolio](../README.md) · [Research record](../research/README.md)
