# Project inventory — AI engineering, deployment and aerospace systems

The portfolio is organized by the kind of engineering evidence each project provides. Ownership language reflects my actual role: direct implementation where applicable, and technical leadership/systems integration where work is team-developed.

## A. Core AI engineering evidence

| Project | Engineering evidence | Current state |
|---|---|---|
| [Lodestar](lodestar.md) | Python/FastAPI RAG; structure-aware ingestion; BGE embeddings; PostgreSQL/pgvector; HNSW + FTS hybrid retrieval; RRF; authority-weighted reranking; LLM integration; evaluation, stress and browser tests | Working private full-stack system with sanitized implementation, frozen evaluation spec and runnable public pure-logic checks |
| [TIR-FOD / Clear Run](tir-fod-clear-run.md) | Real LWIR dataset; 29-run six-model YOLO study; multi-model LWIR work; reproducible experiment orchestration; Jetson/TensorRT UAV deployment; dual RGB/IR FP16 inference; YOLOv12 + SAHI; geolocation, MAVLink/REST and GCS integration | Flight-tested edge AI plus active field integration; GCS→UGV hand-off and physical retention remain under end-to-end validation |
| [Codex Adversarial Review Lite](codex-adversarial-review-lite.md) | Independent multi-model review workflow; preflight/fallback; mutation checks; structured audit; human release decision | Public working AI-assurance tool |
| [JobLooper](joblooper-jobpilot.md) | Deterministic evidence/provenance controls around optional AI assistance; local workflow, CLI/dashboard, release gates and document generation | Public working software |

These are the main evidence streams for RAG, GenAI integration, computer vision, model evaluation, edge inference, APIs, deployment and AI assurance.

## B. Deployed computer vision and autonomy

### Clear Run UAV–GCS–UGV

The active Clear Run stack includes Jetson Orin Nano aerial compute, RGB and passive-IR cameras, independent FP16 TensorRT engines, YOLO/SAHI inference, geolocation, camera-tagged detections, synchronized recording, MAVLink telemetry and Flask/Leaflet GCS integration. UGV computing/navigation and the retrieval mechanism form the downstream robotic layer. Current trials are closing the GCS→UGV hand-off, terminal-alignment and physical-retention measurements; those final end-to-end steps are not described as completed capability.

### TIR-FOD thermal UAV deployment

The TIR-FOD detector was converted to TensorRT and flight-tested on Jetson Orin Nano over runway surfaces. Historical author-confirmed ten-run summaries are 25.0 FPS TensorRT-stage and 15.6 FPS end-to-end on the 640 × 512 thermal stream. The raw per-run logs and historical engine were not retained, so those figures are explicitly separated from the reproducible model-benchmark evidence and from the newer named-checkpoint measurement protocol.

### Counter-UAS Phase I

[Counter-UAS Phase I](counter-uas.md) provides a separate physical computer-vision demonstrator with indoor/outdoor drone-detection and tracking trials, hardware integration and preserved training/visual evidence.

## C. ML lifecycle, evaluation and reproducibility

TIR-FOD provides the strongest model-lifecycle evidence: configuration-driven resumable experiment queues, deterministic multi-seed training, controlled protocol variations, validation-based checkpoint selection, held-out testing, per-class metrics, run histories, checksums/manifests and deployment profiling. Lodestar adds retrieval evaluation, regression-style gates, concurrency/stress testing and provenance-aware model/retrieval integration.

## D. Research and engineering infrastructure

- [ATLAS GPU/HPC environment](atlas-hpc.md) — GPU/HPC research platform, containers, monitoring, reproducibility and controlled engineering use.
- **GNSS 8-element CRPA interference suppression** — adaptive array / interference-rejection research; accepted/presented IBCAST 2026 work.
- **AERIS-10 radar demonstrator** — RF/antenna/embedded-processing integration and staged V&V.
- **Ku-band phased array, UWB radar and radar/EW laboratories** — RF/signal-processing development and technical education.
- **Sensor-enhanced aircraft digital-twin work** — systems/digital-engineering development with sensing, lifecycle data and staged validation.

## E. Product/software engineering

[BuildSignal](buildsignal-ai.md) is a Next.js/TypeScript/MDX editorial/product platform with validation and publishing workflows. It is included as software/product evidence rather than inflated into a machine-learning claim.

## Portfolio leadership context

In my current CAE/NUST role I govern **100+ multidisciplinary engineering and R&D initiatives** across avionics, radar/RF, communications, embedded systems, sensing, UAV/autonomous systems and AI. That scale demonstrates technical portfolio leadership while the individual project pages identify the implementation and evidence specific to each workstream.

[Back to portfolio](../README.md)
