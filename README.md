# M. Umair Raza — Applied AI Engineering Portfolio

**RAG / retrieval · computer vision · edge AI · AI assurance · aerospace systems**

I am an aerospace systems engineer and engineering leader whose current work includes hands-on applied AI, computer vision, retrieval systems, edge deployment and AI-assisted software workflows. My earlier 18+ year aerospace career adds aircraft integration, verification and validation, fleet engineering, international OEM work and programme delivery.

This repository is an **evidence index**, not a catalogue of AI keywords. It separates what is implemented and measured from what is still being integrated or proposed. Where the complete working repository is private, I publish selected non-sensitive implementation evidence, measurements and status boundaries rather than synthetic demonstrations.

## Start with the engineering evidence

| System | What is implemented / measured | Evidence and maturity |
|---|---|---|
| **Lodestar** | Python/FastAPI RAG system; legal-structure-aware chunking; BGE embeddings; PostgreSQL + `pgvector`; HNSW semantic retrieval; PostgreSQL FTS; reciprocal-rank fusion; authority-aware reranking; citable retrieval objects; LLM-provider abstraction; tests and browser flow | **Working pre-production system.** 209 documents / 2,945 embedded chunks; 34 hand-checked retrieval pairs; 2.9% top-5 retrieval error; 53 backend tests; 17/17 stress/abuse cases; 12/12 concurrent flows. [Case study](projects/lodestar.md) · [sanitized implementation evidence](evidence/lodestar/README.md) |
| **TIR-FOD** | LWIR runway dataset engineering; repeated YOLO benchmarking; source-lineage leakage tests; acquisition-block generalisation; Jetson Orin Nano / TensorRT deployment; UAV runway trials | **Flight-tested research prototype and public dataset.** 3,499 source frames, 5,593 annotated objects, 23 classes; 29 training runs; ten-run mean 25.0 FPS TensorRT inference / 15.6 FPS end-to-end during integrated UAV trials. [Case study](projects/tir-fod-clear-run.md) · [benchmark snapshot](evidence/tir-fod/benchmark_results.json) · [dataset DOI](https://doi.org/10.5281/zenodo.22546586) |
| **Codex Adversarial Review Lite** | Independent builder/reviewer workflow; review contract; model preflight/fallback; repository mutation checks; structured verdict; human approval before changes | **Public working tool.** [Case study](projects/codex-adversarial-review-lite.md) · [source repository](https://github.com/razaumair2203-ux/codex-adversarial-review-lite) |
| **JobLooper** | Local evidence-governed application workflow; deterministic generation gates; provenance/hashes; dashboard + CLI; document build and submission-record controls; optional AI assistant integration | **Public working software.** Python 3.10+ standard-library runtime; AI is optional rather than trusted as the source of truth. [Case study](projects/joblooper-jobpilot.md) · [source repository](https://github.com/razaumair2203-ux/Pub-JobLooper) |

## Lodestar — RAG built as a retrieval system, not a prompt demo

The working Lodestar codebase contains a FastAPI backend, PostgreSQL/pgvector data plane, ingestion pipeline, structure-aware chunking, embedding-provider abstraction, hybrid retrieval, deterministic reranking, evidence assessment, provider-swappable LLM integration, a Next.js frontend and automated tests.

```text
source corpus
   ↓
structure-aware chunking
   ├── BGE passage embeddings ──> pgvector / HNSW cosine ─┐
   └── PostgreSQL tsvector ─────> lexical retrieval ──────┤
                                                          ↓
                                   reciprocal-rank fusion (RRF)
                                                          ↓
                                   authority-aware reranking
                                                          ↓
                                   citable retrieval objects
                                                          ↓
                                   grounded assessment
```

The public evidence bundle includes representative retrieval code, schema, embedding logic, the evaluation harness and DB-backed retrieval tests. The current build is **not represented as a public production deployment**: CI wiring and parts of security hardening remain open before deployment sign-off. [Inspect Lodestar evidence](evidence/lodestar/README.md).

## TIR-FOD — model accuracy plus the harder deployment questions

TIR-FOD started with real runway LWIR acquisition and was developed as a leakage-aware detection benchmark rather than a single best-checkpoint result. The work includes frozen source-grouped partitions, a second annotation pass, repeated-seed training, controlled contamination tests, acquisition-block generalisation and size/class analysis.

The detector was then integrated with a thermal payload, Pixhawk/GNSS and Jetson Orin Nano, converted to TensorRT and exercised in repeated UAV runway trials. The current manuscript reports ten-run means of **25.0 FPS inference** and **15.6 FPS end-to-end** on a 640×512 LWIR stream.

**Clear Run is the next integration layer, not a completed claim.** UAV sensing, telemetry recording, UGV hardware/navigation and retrieval CAD exist, while complete target hand-off, terminal alignment, fabricated-mechanism integration and detection-to-retention performance are still being integrated and measured. [Technical case study and maturity boundary](projects/tir-fod-clear-run.md).

## AI assurance and governed software

**Codex Adversarial Review Lite** addresses a different AI problem: how to use one coding model without automatically trusting its output. It separates builder and reviewer roles, freezes review scope, preflights the reviewer, detects repository mutation and requires a human decision before fixes are applied.

**JobLooper** applies a similar engineering principle to AI-assisted document generation: deterministic evidence, provenance and release state stay outside the model. The public implementation is deliberately useful without AI and adds an assistant only as an optional reasoning layer.

These projects are included because they expose AI integration, failure containment, testing and human-in-the-loop design—not because every software workflow is being relabelled as AI.

## Research and field work

- **Low-Latency Architectures for Real-Time Multi-Stream Object Detection** — IEEE ICoDT2, 2025. DOI `10.1109/ICoDT269104.2025.11360736`.
- **TK-Patch: Universal Top-K Adversarial Patches for Cross-Model Person Evasion** — IEEE ICoDT2, 2025. DOI `10.1109/ICoDT269104.2025.11360694`.
- **Adaptive Interference Suppression in GNSS Using an 8-Element CRPA Antenna Array** — accepted/presented at IBCAST 2026; no IEEE Xplore/DOI claim is made here until independently verifiable.
- **TIR-FOD** — public Zenodo dataset v1.2; IEEE Access manuscript revision in progress, not represented as published.
- **Counter-UAS Phase I** — completed computer-vision demonstrator with preserved trial evidence; later RF/acoustic/multisensor work remains proposed research, not completed capability.

[Research record](research/README.md) · [Project and maturity inventory](projects/README.md)

## Engineering context around the AI

Current R&D work sits inside a broader aerospace/sensing environment: UAV/autonomous systems, radar/RF, GNSS interference suppression, embedded processing, requirements/interfaces, staged V&V and technical acceptance. I currently govern 100+ multidisciplinary initiatives; that scale is **leadership evidence**, not a claim that I personally authored every model or codebase.

The earlier career context matters for applied aerospace AI: aircraft hardware/software integration, flight-line fault isolation, OEM development, acceptance testing, fleet configuration control and lifecycle support make deployment constraints, interfaces, failure modes and operational validation familiar engineering problems.

## Technical stack evidenced in the projects

**AI / retrieval:** Python, YOLO-family detectors, OpenCV, TensorRT, BGE embeddings, RAG, semantic search, `pgvector`, HNSW, PostgreSQL full-text search, RRF, LLM/provider integration.

**Backend / product:** FastAPI, PostgreSQL, Supabase, REST/API integration, Next.js/TypeScript in Lodestar, Git/GitHub, Playwright, automated tests, concurrency/stress testing, deterministic validation and provenance controls.

**Deployment / systems:** NVIDIA Jetson, GPU/HPC research environments, Linux/containers, MATLAB, embedded/real-time systems, requirements and interface engineering, V&V and configuration control.

## Evidence boundaries

- Lodestar is a **working pre-production system**, not a claimed public production service.
- TIR-FOD has **real UAV flight-test evidence**; Clear Run's complete autonomous retrieval loop is **still under integration and measurement**.
- RGB/LWIR work should not be read as a completed multimodal-fusion product unless a project page explicitly says so.
- I do not claim mature enterprise ownership of Azure/AWS/GCP or a Kubeflow/MLflow-class MLOps platform where evidence does not exist.
- Private repositories remain private where they contain personal, institutional or programme material; public evidence is selected for technical inspectability without disclosing that material.

---

**GitHub:** [razaumair2203-ux](https://github.com/razaumair2203-ux) · **Google Scholar:** [Muhammad Umair Raza](https://scholar.google.com/citations?user=0EVckyAAAAAJ&hl=en) · **LinkedIn:** [M. Umair Raza](https://www.linkedin.com/in/mumairaza)
