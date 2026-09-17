# Research record — AI, computer vision, sensing and resilient systems

This page separates **published / indexed work**, **public datasets**, and **active manuscripts**. Status is stated explicitly; no submitted paper is presented as published.

**Public author record:** [Google Scholar — Muhammad Umair Raza](https://scholar.google.com/citations?user=0EVckyAAAAAJ&hl=en) · College of Aeronautical Engineering · verified `cae.nust.edu.pk` affiliation.

## Published / indexed conference papers

### Low-Latency Architectures for Real-Time Multi-Stream Object Detection

**IEEE ICoDT2, 2025**  
DOI: [10.1109/ICoDT269104.2025.11360736](https://doi.org/10.1109/ICoDT269104.2025.11360736)

Focus: low-latency processing architectures for concurrent high-definition object-detection streams, evaluated around throughput and latency rather than single-stream accuracy alone.

**Portfolio relevance:** real-time AI architecture, multi-stream inference, latency engineering, system bottleneck analysis.

### TK-Patch: Universal Top-K Adversarial Patches for Cross-Model Person Evasion

**IEEE ICoDT2, 2025**  
DOI: [10.1109/ICoDT269104.2025.11360694](https://doi.org/10.1109/ICoDT269104.2025.11360694)

Focus: transferable physical adversarial patches evaluated across multiple YOLO person detectors and real-world transformations.

**Portfolio relevance:** adversarial ML, robustness evaluation, physical-world testing, model-agnostic attack design.

## 2026 conference paper

### Adaptive Interference Suppression in GNSS Using an 8-Element CRPA Antenna Array

**IBCAST 2026, Murree Hills, Pakistan**  
Authors: Samaira Waqar Elahi, Malik Muhammad Abdullah, Waqas Aftab, Sohaib Yaqoob Chaudhry, **Umair Raza**.

Accepted/presented at IBCAST 2026. This portfolio does **not** claim IEEE Xplore indexing or a DOI until a public record is verifiable.

**Portfolio relevance:** adaptive signal processing, antenna arrays, GNSS resilience, interference suppression, sensing-system engineering.

## Public AI dataset

### TIR-FOD — Thermal-Infrared Benchmark Dataset for Foreign Object Debris Detection on Airfields

**Zenodo v1.2, 2026**  
DOI: [10.5281/zenodo.22546586](https://doi.org/10.5281/zenodo.22546586)

- **3,499** single-shot LWIR source frames;
- **5,593** object annotations;
- **23** categories;
- source-lineage-aware benchmark partitions;
- blind second annotation on **338** frames plus automated checks;
- repeated YOLO benchmarking and leakage/generalisation diagnostics;
- operational Jetson Orin Nano / TensorRT UAV demonstration.

A public dataset is treated here as a first-class research output: acquisition design, annotation, curation, leakage control, versioning, reproducible splits and evaluation are part of the engineering contribution.

[Technical case study](../projects/tir-fod-clear-run.md) · [Inspectable benchmark result snapshot](../evidence/tir-fod/benchmark_results.json)

## Active manuscript

### TIR-FOD: A Thermal-Infrared Benchmark Dataset for Foreign Object Debris Detection on Airfields

**IEEE Access — manuscript revision in progress, 2026.**

Current manuscript evidence includes 29 training runs, repeated seeds, source-aware splitting, a controlled contamination experiment, acquisition-block generalisation analysis and measured Jetson/TensorRT flight performance. The manuscript is not labelled as published until the publication process is complete.

## Current research directions

- supervised UAV–GCS–UGV runway FOD detection and retrieval;
- edge AI and deployment validation;
- multimodal RGB/LWIR sensing;
- adversarial robustness / resilient perception;
- GNSS interference suppression and CRPA arrays;
- AI-assisted engineering/product workflows;
- retrieval-augmented systems with explicit provenance and evaluation;
- sensor-enhanced digital-twin concepts;
- GPU/HPC infrastructure for applied engineering research.

## Independent verification

The two 2025 ICoDT2 papers have public DOI records. The TIR-FOD dataset has a public Zenodo DOI. Google Scholar provides the author-level research identity record. Citation counts are intentionally not copied because they are mutable.

[Back to portfolio](../README.md)
