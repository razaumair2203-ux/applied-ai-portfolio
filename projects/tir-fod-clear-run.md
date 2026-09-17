# TIR-FOD / Clear Run — thermal edge AI and runway autonomy research

This work has two different maturity levels and they should not be blended:

1. **TIR-FOD:** a completed public thermal dataset/benchmark programme with real UAV edge-AI flight trials.
2. **Clear Run:** the follow-on UAV–GCS–UGV inspection/retrieval system, where several subsystems exist but the complete detection-to-retention loop is still being integrated and measured.

## TIR-FOD — dataset and benchmark

**Public dataset:** [TIR-FOD v1.2 — Zenodo DOI 10.5281/zenodo.22546586](https://doi.org/10.5281/zenodo.22546586)  
**Inspectable result data:** [selected raw benchmark snapshot](../evidence/tir-fod/benchmark_results.json)

Verified dataset / study scope:

- **3,499** single-shot LWIR source frames acquired over real runway surfaces;
- **5,593** bounding-box annotations;
- **23** FOD categories;
- source acquisition from approximately **0.5–10 m**;
- **29,243** stored images in the offline archival pool after augmentation;
- frozen source-lineage-aware partitions;
- blind second annotation on **338 frames** plus automated consistency checks;
- **29 training runs** across YOLOv8, YOLO11, YOLO12 and comparative studies.

### Why the evaluation design matters

The project was deliberately tested against common ways object-detection results can look better than they generalise:

- best observed three-seed YOLOv8n mean mAP@[.50:.95]: **0.8603 ± 0.0017**;
- detector means in the principal comparison span only **0.0062**, so repeated-seed variation is reported rather than over-interpreting one checkpoint;
- a size-matched held-out-source contamination experiment increased mAP@[.50:.95] by **8.52 ± 0.19 percentage points**;
- on a shared 12-class source pool, acquisition-block-disjoint partitioning produced **0.7410 ± 0.0423**, compared with **0.8223 ± 0.0070** using a frame-level partition.

The value of the work is therefore not only the detector score. It includes source-lineage control, repeated seeds, contamination testing, acquisition-block separation, annotation checks, and class/size-resolved analysis.

## Edge deployment and UAV runway trials

The detector was taken beyond workstation evaluation and integrated into a UAV sensing stack consisting of:

- LWIR camera payload;
- NVIDIA **Jetson Orin Nano**;
- **TensorRT** detector execution;
- GNSS-equipped Pixhawk flight-control system;
- custom payload mounts;
- communication of detection outputs to the operator interface.

Repeated runway trials exercised the integrated inspection path at UAV heights of approximately **5–10 m**, including isolated debris, multiple/overlapping objects and objects of different sizes. Trial records include successful detections as well as missed objects, false detections and correct localization with incorrect classification.

The current manuscript reports ten-run means of:

- **25.0 FPS** TensorRT inference;
- **15.6 FPS** complete inspection pipeline on a 640×512 LWIR stream;
- approximately **16–18 W** for the compute-and-camera subsystem during the reported trials (UAV propulsion excluded);
- reported module temperatures of approximately **55–70 °C**.

These are integrated field-test measurements. The records do **not** establish per-frame latency distributions, checkpoint-specific precision for the deployed engine, or an enterprise production deployment, so those are not claimed here.

## Clear Run — current integration state

Clear Run extends perception into a supervised inspection-and-retrieval research system:

```text
UAV RGB / LWIR sensing
          ↓
edge detection + geolocation
          ↓
GCS event / target hand-off
          ↓
UGV navigation
          ↓
local target re-acquisition + terminal visual alignment
          ↓
physical retrieval / retention
          ↓
mission-level KPIs and failure accounting
```

### Demonstrated or available now

- daytime and night-time aerial detection have been tested;
- recording sessions include camera-tagged detections, video and associated flight telemetry;
- UAV, GCS and UGV components form the current experimental platform;
- UGV chassis, onboard compute and navigation subsystems are available;
- retrieval-mechanism CAD is complete;
- current perception and embedded-performance baselines exist from TIR-FOD.

### In progress / next engineering gates

- validate the complete target-dispatch and acknowledgement path;
- fabricate and integrate the retrieval mechanism;
- implement and validate local target re-acquisition / terminal visual alignment;
- measure hand-off error, alignment tolerance, intervention burden and retrieval/retention outcomes;
- execute matched controlled trials for complete detection-to-retention performance.

**Current evidence does not yet establish an integrated collection rate, complete target hand-off performance, terminal-alignment accuracy or retained-object success under the full operating envelope.** Those remain measurements to be produced, not claims to be inferred from the subsystem work.

## Engineering role

I lead the applied R&D / systems-engineering effort: architecture and integration direction, experiment design, maturity gates, KPI definition, deployment review, multidisciplinary/student engineering teams and research/publication development. That leadership role should not be read as sole authorship of every algorithm, mechanical component or line of code produced by the team.

## Research status

- TIR-FOD dataset v1.2 is publicly released on Zenodo.
- The TIR-FOD IEEE Access manuscript is under revision in 2026 and is **not represented as published**.
- Clear Run remains an active integration and validation programme.

[Back to portfolio](../README.md) · [Research record](../research/README.md)
