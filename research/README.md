# Research record — AI, computer vision, sensing and resilient systems

This page separates **published/indexed work**, **public datasets**, **conference status** and **active manuscripts**. Submitted or in-progress work is not presented as published.

**Public author record:** [Google Scholar — Muhammad Umair Raza](https://scholar.google.com/citations?user=0EVckyAAAAAJ&hl=en) · College of Aeronautical Engineering / NUST affiliation.

## Published / indexed conference papers

### Low-Latency Architectures for Real-Time Multi-Stream Object Detection

**IEEE ICoDT2, 2025**  
DOI: [10.1109/ICoDT269104.2025.11360736](https://doi.org/10.1109/ICoDT269104.2025.11360736)

Focus: low-latency processing architectures for concurrent object-detection streams, evaluated around throughput, latency and system bottlenecks rather than a single-stream accuracy result.

**Engineering relevance:** real-time computer vision, concurrent inference, latency/throughput trade-offs and deployment-oriented architecture.

### TK-Patch: Universal Top-K Adversarial Patches for Cross-Model Person Evasion

**IEEE ICoDT2, 2025**  
DOI: [10.1109/ICoDT269104.2025.11360694](https://doi.org/10.1109/ICoDT269104.2025.11360694)

Focus: transferable physical adversarial patches evaluated across multiple YOLO person detectors and real-world transformations.

**Engineering relevance:** adversarial ML, robustness evaluation, cross-model transfer and physical-world testing.

## 2026 conference work

### Adaptive Interference Suppression in GNSS Using an 8-Element CRPA Antenna Array

**IBCAST 2026, Pakistan**  
Authors include **Umair Raza**.

Status used in this portfolio: **accepted/presented at IBCAST 2026**. No IEEE Xplore indexing or DOI is claimed until a public record can be independently verified.

**Engineering relevance:** adaptive signal processing, antenna arrays, GNSS resilience and interference suppression.

## Public AI dataset

### TIR-FOD — Thermal-Infrared Benchmark Dataset for Foreign Object Debris Detection on Airfields

**Zenodo v1.2, 2026**  
DOI: [10.5281/zenodo.22546586](https://doi.org/10.5281/zenodo.22546586)

Verified dataset/study scope includes:

- **3,499** single-shot LWIR source frames;
- **5,593** object annotations;
- **23** categories;
- source-lineage-aware benchmark partitions;
- blind second annotation on **338 frames** plus automated checks;
- repeated YOLO benchmarking and leakage/generalisation diagnostics;
- a **flight-tested Jetson Orin Nano / TensorRT UAV prototype**, including measured onboard/integrated throughput.

A public dataset is treated here as an engineering output in its own right: acquisition design, annotation, curation, source lineage, leakage control, versioning, reproducible partitions and deployment testing are part of the work.

[Technical case study](../domains/01-autonomy-edge-ai/clear-run-tir-fod.md) · [Inspectable benchmark result snapshot](../evidence/autonomy_edge_ai/tir_fod/benchmark_results.json)

## Submitted systems-engineering case

### From debris detection to verified removal: Evidence-linked MBSE for an evolving airfield robotics system

**INCOSE Applications & Case Studies (IACS) — submitted 16 September 2026.**

Status: **submitted; editorial acknowledgement/review pending**. The case documents a bounded retrospective Capella/Arcadia reconstruction, evidence-applicability gates and a reproducible producer-consumer telemetry replay. Submission is not represented as acceptance or publication.

[Public portfolio case study](../domains/01-autonomy-edge-ai/ai-systems-assurance-mbse.md)

## Active manuscript

### TIR-FOD: A Thermal-Infrared Benchmark Dataset for Foreign Object Debris Detection on Airfields

**IEEE Access — revision in progress, 2026.**

The current manuscript includes repeated training runs, source-aware splitting, controlled contamination testing, acquisition-block generalisation analysis and measured Jetson/TensorRT UAV flight performance. It is **not labelled as published** while the publication process remains open.

## Active research directions — not completed-publication claims

- supervised UAV–GCS–UGV runway FOD detection and retrieval;
- edge-AI deployment validation and reliability measurement;
- RGB/LWIR sensing and future multimodal integration;
- adversarial robustness / resilient perception;
- GNSS interference suppression and CRPA arrays;
- RAG / retrieval systems with explicit provenance and evaluation;
- sensor-enhanced digital-twin concepts;
- GPU/HPC infrastructure for applied engineering research.

## Verification boundary

The two 2025 ICoDT2 papers have public DOI records. The TIR-FOD dataset has a public Zenodo DOI. The current TIR-FOD manuscript remains under revision. Citation counts are not copied into this repository because they are mutable, and conference/indexing status is not upgraded without a verifiable public record.

[Back to portfolio](../README.md)
