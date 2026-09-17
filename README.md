# M. Umair Raza — Aerospace AI & Autonomous Systems

**Applied AI · computer vision · RAG / retrieval · edge deployment · aerospace systems engineering**

I build and lead AI-enabled engineering systems that have to work outside the notebook: on embedded hardware, across sensors and interfaces, through verification, and into field trials. My background combines current hands-on applied AI with 18+ years in aircraft systems integration, V&V, fleet engineering and programme delivery.

> **Primary differentiator:** model/data engineering + edge deployment + physical-system integration + aerospace V&V.

## 60-second technical proof

| Capability | What is actually implemented | Evidence |
|---|---|---|
| **Deployed edge AI / computer vision** | LWIR model development; multi-model YOLO work; TensorRT deployment on Jetson Orin Nano; RGB + passive-IR concurrent inference; YOLO + SAHI sliced inference; geolocation; MAVLink/REST; GCS integration | **3,499 LWIR source frames · 5,593 objects · 23 classes · 29 controlled training runs · 25.0 FPS TensorRT inference · 15.6 FPS end-to-end** → [case study](projects/tir-fod-clear-run.md) · [deployment-code evidence](evidence/clear-run/README.md) |
| **Grounded RAG / GenAI systems** | FastAPI; BGE embeddings; PostgreSQL + `pgvector`; HNSW + lexical retrieval; RRF; authority-aware reranking; citable evidence objects; LLM-provider abstraction; full-stack testing | **209 documents · 2,945 embedded chunks · 2.9% top-5 retrieval-grounding error · 53 backend tests · 12/12 concurrent flows** → [case study](projects/lodestar.md) · [implementation evidence](evidence/lodestar/README.md) |
| **AI assurance / governed workflows** | Independent builder-reviewer model workflow; mutation checks; deterministic evidence/provenance gates around AI-assisted generation | **Two public working tools** → [Codex Adversarial Review Lite](projects/codex-adversarial-review-lite.md) · [JobLooper](projects/joblooper-jobpilot.md) |

## Start here by role

| If you are hiring for… | Review first | Why |
|---|---|---|
| **Aerospace AI / Applied AI Lead** | [Clear Run / TIR-FOD](projects/tir-fod-clear-run.md), then [Lodestar](projects/lodestar.md) | Shows model development, deployment, physical integration, evaluation and broader AI systems depth |
| **Computer Vision / Edge AI / Autonomy** | [Clear Run / TIR-FOD](projects/tir-fod-clear-run.md) | Strongest evidence from dataset design through Jetson/TensorRT flight deployment and UAV–GCS–UGV integration |
| **GenAI / RAG / AI Platform** | [Lodestar](projects/lodestar.md), then [AI assurance](projects/codex-adversarial-review-lite.md) | Retrieval, grounding, APIs, evaluation, testing and responsible model integration |
| **AI Engineering Manager / Systems Architect** | [Project inventory](projects/README.md) | Breadth across AI software, embedded deployment, autonomy, HPC and aerospace systems |

## Flagship 1 — runway AI from benchmark to aircraft

**TIR-FOD / Clear Run** is the strongest example of my end-to-end applied-AI work.

- Real-runway LWIR acquisition and annotation: **3,499 source frames, 5,593 objects, 23 FOD classes**.
- **29 controlled training runs** across YOLOv8, YOLO11 and YOLO12 configurations, plus current multi-model LWIR fusion work.
- Source-lineage leakage controls, repeated seeds, contamination studies and acquisition-block generalisation—not just a best-checkpoint result.
- Detector converted to **TensorRT** and flight-tested onboard **Jetson Orin Nano**.
- Clear Run expands the deployed stack to **concurrent RGB + passive-IR FP16 TensorRT inference**, small-object sliced inference, geolocation, MAVLink/REST telemetry, synchronized recording and GCS mission integration.
- Current system work closes the final UAV–GCS–UGV target hand-off, terminal alignment and physical-retention validation loop.

**Deep dive:** [TIR-FOD / Clear Run case study](projects/tir-fod-clear-run.md) · [sanitized deployment implementation](evidence/clear-run/README.md)

## Flagship 2 — grounded RAG as an engineering system

**Lodestar** is a working private full-stack RAG/evidence system with public sanitized implementation evidence.

- Python / FastAPI backend with PostgreSQL and `pgvector`.
- Legal-structure-aware chunking and BGE query/passage embeddings.
- Hybrid vector + lexical retrieval with HNSW, PostgreSQL FTS and Reciprocal Rank Fusion.
- Deterministic authority-aware reranking and citable evidence objects.
- Independent retrieval-grounding evaluation so fluent LLM output cannot hide weak retrieval.
- Reliability work includes pooled DB connections, guarded embedding initialization, citation checks, audit paths, browser tests, stress/abuse tests and concurrent flows.

**Deep dive:** [Lodestar case study](projects/lodestar.md) · [inspectable implementation evidence](evidence/lodestar/README.md)

## AI engineering beyond the two flagships

- **Codex Adversarial Review Lite** — independent builder/reviewer AI workflow with review contracts, model fallback, mutation checks and human approval. [Case study](projects/codex-adversarial-review-lite.md)
- **JobLooper** — local-first evidence/provenance and release controls around optional AI-assisted document generation. [Case study](projects/joblooper-jobpilot.md)
- **Counter-UAS Phase I** — computer-vision drone-detection demonstrator with indoor/outdoor physical trials. [Case study](projects/counter-uas.md)
- **ATLAS GPU/HPC environment** — research compute, containers, monitoring and reproducibility infrastructure. [Case study](projects/atlas-hpc.md)

## Aerospace systems context

My AI work sits inside a wider engineering career spanning aircraft hardware/software integration, avionics, requirements/interfaces, FAT/SAT and acceptance testing, flight-line fault isolation, fleet sustainment, configuration management and international OEM coordination. Current CAE/NUST responsibilities include technical governance of **100+ multidisciplinary engineering and R&D initiatives** across avionics, radar/RF, communications, embedded systems, UAV/autonomy and AI.

That background changes how I approach AI: deployment constraints, interfaces, failure modes, traceability, verification and operational behaviour are treated as engineering requirements rather than post-processing concerns.

## Research

- **Low-Latency Architectures for Real-Time Multi-Stream Object Detection** — IEEE ICoDT2 2025 · DOI `10.1109/ICoDT269104.2025.11360736`
- **TK-Patch: Universal Top-K Adversarial Patches for Cross-Model Person Evasion** — IEEE ICoDT2 2025 · DOI `10.1109/ICoDT269104.2025.11360694`
- **Adaptive Interference Suppression in GNSS Using an 8-Element CRPA Antenna Array** — IBCAST 2026
- **TIR-FOD** — public Zenodo dataset v1.2; IEEE Access manuscript revision in progress

[Research record](research/README.md)

## Technical stack evidenced in the projects

**AI / ML / retrieval:** Python · PyTorch/Ultralytics · YOLOv8/11/12 · SAHI · OpenCV · TensorRT · BGE embeddings · RAG · `pgvector` · HNSW · PostgreSQL FTS · RRF · LLM/provider integration

**ML lifecycle / evaluation:** configuration-driven experiment orchestration · deterministic multi-seed training · checkpoint selection · held-out evaluation · leakage/generalisation testing · manifests/checksums · model conversion · edge profiling · field validation

**Backend / product:** FastAPI · PostgreSQL · Supabase · REST APIs · Next.js/TypeScript · Flask · Git/GitHub · Playwright · automated/concurrency/stress testing

**Edge / autonomy / systems:** NVIDIA Jetson Orin Nano / Jetson Nano · FP16 TensorRT · ROS/ROS2 · MAVLink · Pixhawk/GNSS · Linux/containers · MATLAB · GPU/HPC · embedded/real-time systems · requirements/interfaces · V&V · configuration control

## Technical evidence index

For reviewers who want code and measured artefacts rather than narrative, start at **[evidence/](evidence/README.md)**. The portfolio contains sanitized implementation where it is safe to publish; complete programme/product repositories remain private where they contain personal, institutional or programme material.

---

**GitHub:** [razaumair2203-ux](https://github.com/razaumair2203-ux) · **Google Scholar:** [Muhammad Umair Raza](https://scholar.google.com/citations?user=0EVckyAAAAAJ&hl=en) · **LinkedIn:** [M. Umair Raza](https://www.linkedin.com/in/mumairaza)
