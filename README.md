# M. Umair Raza — Applied AI Engineering Portfolio

**RAG / retrieval · deployed computer vision · edge AI · AI assurance · aerospace systems**

I am an aerospace systems engineer and engineering leader working across applied AI, computer vision, retrieval systems, edge deployment, autonomous systems and AI-assisted software. My earlier 18+ year aerospace career adds aircraft integration, verification and validation, fleet engineering, international OEM work and programme delivery.

This repository is an **engineering evidence index**. It prioritizes inspectable implementation, measured results, field deployment and reproducibility rather than generic AI claims.

## Start with the engineering evidence

| System | Engineering depth | Evidence |
|---|---|---|
| **Lodestar** | Python/FastAPI RAG system; legal-structure-aware chunking; BGE embeddings; PostgreSQL + `pgvector`; HNSW semantic search; PostgreSQL FTS; Reciprocal Rank Fusion; authority-aware reranking; citable evidence objects; LLM-provider abstraction; full-stack tests and hardening | **209 documents / 2,945 embedded chunks; 34 hand-checked retrieval pairs; 2.9% top-5 retrieval-grounding error; 53 backend tests; 17/17 stress/abuse cases; 12/12 concurrent full flows.** [Case study](projects/lodestar.md) · [implementation evidence](evidence/lodestar/README.md) |
| **TIR-FOD / LWIR AI** | Real-runway thermal dataset engineering; **29 controlled training runs across six YOLOv8/YOLO11/YOLO12 configurations**; multi-model LWIR fusion; source-lineage leakage studies; acquisition-block generalisation; reproducible experiment orchestration; TensorRT edge deployment | **3,499 LWIR source frames, 5,593 annotated objects, 23 classes. Flight-tested Jetson Orin Nano / TensorRT pipeline: 25.0 FPS inference / 15.6 FPS end-to-end across ten runs.** [Case study](projects/tir-fod-clear-run.md) · [benchmark snapshot](evidence/tir-fod/benchmark_results.json) · [dataset DOI](https://doi.org/10.5281/zenodo.22546586) |
| **Clear Run** | Deployed UAV edge-AI stack with Jetson Orin Nano; RGB + passive-IR streams; concurrent FP16 TensorRT engines; YOLOv12 + SAHI small-object inference; camera-tagged detections; geolocation; MAVLink/REST telemetry; synchronized recording; GCS integration; UGV mission hand-off | **Working field-integration system with AI inference running on the aerial platform and detections integrated into the mission/GCS workflow.** [Technical case study](projects/tir-fod-clear-run.md) |
| **Codex Adversarial Review Lite** | Independent builder/reviewer AI workflow; review contracts; model preflight/fallback; mutation checks; structured verdict; human approval before changes | **Public working tool.** [Case study](projects/codex-adversarial-review-lite.md) · [source](https://github.com/razaumair2203-ux/codex-adversarial-review-lite) |
| **JobLooper** | Evidence-governed AI-assisted workflow; deterministic release gates; provenance/hashes; local dashboard + CLI; document generation; optional model integration | **Public working software.** [Case study](projects/joblooper-jobpilot.md) · [source](https://github.com/razaumair2203-ux/Pub-JobLooper) |

## Deployed AI and ML lifecycle engineering

The computer-vision work is not limited to training notebooks. TIR-FOD took a detector from controlled model development through TensorRT conversion and repeated UAV runway trials on a Jetson Orin Nano, including onboard inference, communications and operator display. The measured ten-run means are **25.0 FPS for TensorRT inference and 15.6 FPS end-to-end** on the 640 × 512 thermal stream.

Clear Run extends this into a broader deployed autonomy stack. Its aerial unit runs **RGB and IR camera streams on Jetson Orin Nano**, with independent FP16 TensorRT engines, model management, YOLO/SAHI inference, geolocation, MAVLink telemetry, synchronized video/data recording and a Flask/Leaflet GCS that consumes camera-tagged FOD events for mission handling. Physical retrieval and end-to-end collection validation continue as the next systems-integration layer; the perception and mission-integration stack is already deployed and under field testing.

The training/evaluation workflow also contains practical ML lifecycle controls: configuration-driven and resumable experiment queues, deterministic multi-seed runs, preserved run metadata, validation-selected checkpoints, held-out testing, per-class metrics, experiment manifests/checksums, reproducibility artifacts, TensorRT conversion and field performance/power/thermal measurement. This is the operational discipline behind the models.

## Lodestar — RAG built as an evidence system

Lodestar is a working private full-stack RAG system with a FastAPI backend, PostgreSQL/`pgvector` data plane, ingestion pipeline, structure-aware chunking, BGE embeddings, hybrid lexical/vector retrieval, RRF, deterministic authority-aware reranking, citable evidence objects, provider-swappable LLM integration, a Next.js frontend and automated evaluation.

```text
source corpus
   ↓
structure-aware chunking
   ├── BGE embeddings ───────────> pgvector / HNSW ───────┐
   └── PostgreSQL full text ─────> lexical retrieval ─────┤
                                                           ↓
                                            RRF + authority reranking
                                                           ↓
                                            citable evidence objects
                                                           ↓
                                            grounded assessment
```

Its public evidence bundle contains representative retrieval code, schema, embedding logic, the hand-checked grounding set, evaluation harness and database-backed retrieval tests. [Inspect Lodestar evidence](evidence/lodestar/README.md).

## TIR-FOD / Clear Run — computer vision from benchmark to aircraft

TIR-FOD is a leakage-aware LWIR runway benchmark built from real acquisition rather than synthetic project imagery. The released study covers **six detector configurations — YOLOv8n/s/m, YOLO11s/m and YOLO12s — across 29 completed training runs**, repeated seeds, annotation-quality checks, controlled contamination testing and acquisition-block generalisation.

Current project work extends this with **multi-model LWIR fusion across YOLO-family detectors**. Clear Run adds a second axis of integration: concurrent RGB and IR edge inference with independent TensorRT engines, camera-tagged detection events and a common telemetry/GCS mission workflow.

[Detailed TIR-FOD / Clear Run case study](projects/tir-fod-clear-run.md)

## AI assurance and governed software

**Codex Adversarial Review Lite** treats model output as something to verify: builder and reviewer roles are separated, review scope is frozen, the reviewer is preflighted, repository mutation is checked and a human decision is required before fixes are applied.

**JobLooper** uses the same engineering principle in AI-assisted document generation: source evidence, provenance, workflow state and release decisions remain deterministic even when a model assists interpretation or drafting.

## Research and field work

- **Low-Latency Architectures for Real-Time Multi-Stream Object Detection** — IEEE ICoDT2, 2025. DOI `10.1109/ICoDT269104.2025.11360736`.
- **TK-Patch: Universal Top-K Adversarial Patches for Cross-Model Person Evasion** — IEEE ICoDT2, 2025. DOI `10.1109/ICoDT269104.2025.11360694`.
- **Adaptive Interference Suppression in GNSS Using an 8-Element CRPA Antenna Array** — accepted/presented at IBCAST 2026.
- **TIR-FOD** — public Zenodo dataset v1.2; IEEE Access manuscript revision in progress.
- **Counter-UAS Phase I** — computer-vision drone-detection demonstrator with indoor/outdoor trial evidence.

[Research record](research/README.md) · [Project inventory](projects/README.md)

## Engineering context around the AI

Current work sits inside a broader aerospace environment spanning UAV/autonomous systems, radar/RF, GNSS resilience, embedded processing, requirements/interfaces, staged V&V and technical acceptance. I govern **100+ multidisciplinary engineering and R&D initiatives** while directly leading selected applied-AI and systems-integration work.

My earlier aerospace career adds a development-to-operations perspective: aircraft hardware/software integration, flight-line fault isolation, OEM development, acceptance testing, fleet configuration control and lifecycle support. That makes deployment constraints, interfaces, failure modes and verification first-class engineering concerns rather than afterthoughts.

## Technical stack evidenced by the work

**AI / ML / retrieval:** Python, PyTorch/Ultralytics, YOLOv8/YOLO11/YOLO12, SAHI, OpenCV, TensorRT, BGE embeddings, RAG, semantic search, `pgvector`, HNSW, PostgreSQL FTS, RRF, LLM/provider integration.

**ML lifecycle / evaluation:** configuration-driven experiment orchestration, multi-seed training, deterministic runs, checkpoint selection, held-out evaluation, per-class metrics, leakage/generalisation testing, reproducibility manifests/checksums, model conversion, edge profiling and field validation.

**Backend / product:** FastAPI, PostgreSQL, Supabase, REST APIs, Next.js/TypeScript, Flask, Git/GitHub, Playwright, automated tests, concurrency/stress testing, deterministic validation and provenance controls.

**Edge / autonomy / systems:** NVIDIA Jetson Orin Nano and Jetson Nano, FP16 TensorRT engines, ROS/ROS2, MAVLink, Pixhawk/GNSS, GPU/HPC environments, Linux/containers, MATLAB, embedded/real-time systems, requirements/interface engineering, V&V and configuration control.

---

**GitHub:** [razaumair2203-ux](https://github.com/razaumair2203-ux) · **Google Scholar:** [Muhammad Umair Raza](https://scholar.google.com/citations?user=0EVckyAAAAAJ&hl=en) · **LinkedIn:** [M. Umair Raza](https://www.linkedin.com/in/mumairaza)
