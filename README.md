# M. Umair Raza — Applied AI Engineering for Aerospace & High-Integrity Systems

[![Portfolio evidence smoke checks](https://github.com/razaumair2203-ux/applied-ai-portfolio/actions/workflows/portfolio-evidence.yml/badge.svg)](https://github.com/razaumair2203-ux/applied-ai-portfolio/actions/workflows/portfolio-evidence.yml)

**Edge computer vision · RAG / retrieval · autonomous systems · AI assurance · aerospace systems engineering**

I work on AI where the model is only one part of the engineering problem: real sensors, edge hardware, interfaces, data provenance, evaluation, failure modes and verification all matter. My current work combines hands-on applied AI with **18+ years** across aircraft development, operational systems, V&V, fleet engineering and programme delivery.

> **Core signal:** model/data engineering + deployment + physical-system integration + evidence-driven V&V.

I am not presenting this portfolio as proof of being a conventional career software engineer. Its differentiator is the ability to engineer AI inside multidisciplinary systems where an impressive offline metric is not enough.

## What I personally own

- **Lodestar:** product constraints, retrieval/grounding architecture, evaluation gates, acceptance criteria, and hands-on **AI-assisted Python implementation, testing and hardening**.
- **TIR-FOD:** experiment/evaluation strategy, model-comparison direction, deployment validation and research leadership.
- **Clear Run:** systems architecture, interfaces, integration gates, KPI definition and multidisciplinary technical direction. **Clear Run is team-developed**; team source is not presented as sole authorship.
- **AI assurance / governed workflows:** public tools that keep model output inside explicit review, evidence and release boundaries.

<p align="center">
  <img src="visuals/clear_run_system_evidence.jpg" alt="Authentic Clear Run system evidence: UAV, field detections, GCS, UGV, retrieval mechanism and documented architecture" width="100%">
</p>

<p align="center"><sub><b>Clear Run — field-to-system evidence.</b> Repository-original photographs, recorded detections, GCS output, CAD and architecture. No generated imagery or synthetic detections.</sub></p>

## What “impact” means in this portfolio

For aerospace / edge AI, impact is not a generic revenue or “innovation” claim. It is evidence that the work **removed technical uncertainty, changed an engineering decision, created a reusable asset, advanced system maturity, or exposed a failure mode before it became false confidence**.

Examples:

- a contamination experiment showed that an apparently stronger detector result was **invalidly inflated by 8.52 ± 0.19 percentage points**;
- a harder acquisition-block split showed that frame-level validation was optimistic;
- onboard measurements separated detector throughput from complete-pipeline throughput, exposing integration overhead;
- Lodestar keeps source authority, citations and release decisions outside the LLM rather than trusting fluent generation;
- public datasets, fixtures, tests and CI make key claims inspectable instead of asking a reviewer to trust portfolio prose.

[How impact is evaluated here →](docs/IMPACT_MODEL.md)

## 60-second technical proof

| Capability | Proven evidence | Engineering significance / boundary |
|---|---|---|
| **Edge AI / computer vision** | **3,499 LWIR source frames · 5,593 objects · 23 classes · 29 controlled training runs**; public source-aware splits and scalar recomputation; TensorRT deployment on Jetson Orin Nano; RGB + passive-IR inference; YOLO/SAHI; geolocation; MAVLink/REST; GCS integration | Evaluation explicitly tests leakage and capture-session dependence. Historical flight summary: **25.0 FPS TensorRT / 15.6 FPS end-to-end over 10 runs** *(author-confirmed; raw per-run logs not retained)*. Final GCS→UGV physical hand-off and verified retention remain under validation. [Case study](projects/tir-fod-clear-run.md) |
| **Grounded RAG / GenAI systems** | FastAPI · BGE · PostgreSQL/pgvector · HNSW + FTS · RRF · authority-aware retrieval/reranking · structured evidence controls · **209 documents · 2,945 chunks · 1/34 top-5 expected-source misses (2.9%)** on the recorded private corpus | Retrieval quality, source authority and output grounding are separate from fluent generation. Public CI runs a real PostgreSQL/pgvector fixture and adversarial structured-output evaluation; the private corpus result is not claimed as independently reproducible. [Case study](projects/lodestar.md) |
| **AI assurance / governed workflows** | Public independent builder/reviewer workflow plus deterministic evidence/provenance and release gates around optional AI assistance | Demonstrates how model output is constrained when truth, mutation state or release authority matters. No claim that a second model guarantees correctness. [Codex review](projects/codex-adversarial-review-lite.md) · [JobLooper](projects/joblooper-jobpilot.md) |

**Evidence boundary.** Public code, data records, visuals and result extracts are linked directly. TIR-FOD training results have a public 29-run scalar recomputation path. The historical Jetson figures are author-confirmed summaries with **raw per-run logs not retained**; the historical engine and exact checkpoint are not reconstructed after the fact. Lodestar full-corpus/test counts remain bounded private-system measurements. See the [headline evidence matrix](docs/HEADLINE_EVIDENCE_MATRIX.md) and [technical evidence index](evidence/README.md).

## Start here by role

| If you are reviewing for… | Open first | Signal |
|---|---|---|
| **Aerospace AI / Applied AI Lead** | [TIR-FOD / Clear Run](projects/tir-fod-clear-run.md), then [Lodestar](projects/lodestar.md) | Model/evaluation depth, edge deployment, physical integration and broader AI systems engineering |
| **Computer Vision / Edge AI / Autonomy** | [TIR-FOD / Clear Run](projects/tir-fod-clear-run.md) | Real dataset → controlled experiments → TensorRT/Jetson flight deployment → UAV/GCS integration |
| **GenAI / RAG / AI Platform** | [Lodestar](projects/lodestar.md), then [AI assurance](projects/codex-adversarial-review-lite.md) | Hybrid retrieval, grounding, database architecture, evaluation, APIs and controlled model integration |
| **AI Engineering Manager / Systems Architect** | [Project inventory](projects/README.md) | AI plus V&V, interfaces, deployment, research computing and multidisciplinary technical governance |

## Flagship 1 — TIR-FOD / Clear Run

A runway FOD programme spanning **data/model development → airborne edge deployment → UAV–GCS–UGV integration**.

What makes it technically useful is not only the detector score:

- public TIR-FOD dataset: **3,499 LWIR frames, 5,593 annotations, 23 classes**;
- **29 controlled runs** across YOLOv8 / YOLO11 / YOLO12 configurations;
- source-lineage leakage and acquisition-block generalisation experiments;
- FP16 TensorRT deployment on **Jetson Orin Nano** during UAV runway trials;
- active dual RGB/IR inference, geolocation, telemetry and GCS mission integration;
- final target hand-off, terminal alignment, collection and retention are still being quantitatively closed.

![Authentic TIR-FOD evidence: real LWIR detections, UAV payload, Jetson runtime, class coverage, training curves and confusion matrix](visuals/tir_fod_evidence.jpg)

**Deep dive:** [TIR-FOD / Clear Run](projects/tir-fod-clear-run.md) · [reproducible model-result bundle](evidence/tir-fod/reproducibility/README.md) · [deployment boundary](evidence/tir-fod/deployment/README.md)

## Flagship 2 — Lodestar

A working private full-stack RAG / evidence-assessment system built around a simple constraint: **the LLM is not allowed to become the source of truth**.

Implemented engineering includes:

- legal-structure-aware chunking and BGE query/passage embeddings;
- PostgreSQL + pgvector, HNSW and PostgreSQL full-text retrieval;
- multi-lane lexical/vector retrieval and Reciprocal Rank Fusion;
- deterministic authority policy and citable evidence objects;
- structured downstream assessment with refusal and citation controls;
- backend, database, browser, stress/abuse and concurrency testing.

![Authentic Lodestar product UI captured from the working application](visuals/lodestar_product_ui.jpg)

The frozen private-system retrieval check recorded **1/34 top-5 expected-source misses (2.9%)** on **209 documents / 2,945 chunks**. That is a targeted regression check, not a universal RAG accuracy claim. The public repository separately executes a real PostgreSQL/pgvector mini-corpus path and structured-output guardrail evaluation.

**Deep dive:** [Lodestar](projects/lodestar.md) · [implementation evidence](evidence/lodestar/README.md)

## Additional evidence

- **Codex Adversarial Review Lite** — independent builder/reviewer AI workflow with frozen review scope, model fallback, mutation checks and human approval. [Case study](projects/codex-adversarial-review-lite.md)
- **JobLooper** — deterministic truth, provenance, workflow state and release controls around optional AI assistance. [Case study](projects/joblooper-jobpilot.md)
- **Counter-UAS Phase I** — physical computer-vision drone-detection demonstrator with indoor/outdoor trials. [Case study](projects/counter-uas.md)
- **ATLAS GPU/HPC** — shared research computing, SLURM/Linux/CUDA/Docker support and controlled technical operations. [Case study](projects/atlas-hpc.md)

## Why the aerospace systems background matters

My wider engineering career covers requirements and interfaces, hardware/software integration, qualification and acceptance testing, flight-line fault isolation, configuration management, fleet sustainment and international OEM coordination. Current responsibilities include technical governance of **100+ multidisciplinary engineering and R&D initiatives** across avionics, radar/RF, communications, embedded systems, sensing, UAV/autonomy and AI.

That experience changes the questions I ask of AI systems:

- Is the dataset split actually representative of future operating conditions?
- Is the measured latency model-only or end-to-end?
- What happens when a sensor, embedding path or model provider is unavailable?
- Which outputs are allowed to become system state?
- What evidence is needed before the next integration or release gate?
- What is demonstrated, what is inferred, and what remains unverified?

## Research

- **Low-Latency Architectures for Real-Time Multi-Stream Object Detection** — IEEE ICoDT2 2025 · DOI 10.1109/ICoDT269104.2025.11360736
- **TK-Patch: Universal Top-K Adversarial Patches for Cross-Model Person Evasion** — IEEE ICoDT2 2025 · DOI 10.1109/ICoDT269104.2025.11360694
- **Adaptive Interference Suppression in GNSS Using an 8-Element CRPA Antenna Array** — accepted/presented at IBCAST 2026; no DOI/Xplore claim until independently verified
- **TIR-FOD** — public Zenodo dataset v1.2; related IEEE Access manuscript remains under revision

[Research record](research/README.md)

## Technical stack evidenced here

**AI / ML / retrieval:** Python · PyTorch/Ultralytics · YOLOv8/11/12 · SAHI · OpenCV · TensorRT · BGE · RAG · pgvector · HNSW · PostgreSQL FTS · RRF

**Evaluation / ML lifecycle:** multi-seed experiments · source-aware splits · leakage/generalisation tests · held-out evaluation · manifests/checksums · reproducible result recomputation · adversarial output-contract evaluation

**Backend / product:** FastAPI · PostgreSQL · REST APIs · Next.js/TypeScript · Flask · Playwright · automated/concurrency/stress testing

**Edge / systems:** Jetson Orin Nano · FP16 TensorRT · MAVLink · Pixhawk/GNSS · Linux · CUDA · Docker · SLURM · requirements/interfaces · V&V · configuration control

## What is deliberately not claimed

- completed autonomous physical FOD recovery;
- measured improvement in runway safety or mission effectiveness;
- public reproducibility of historical Jetson ten-run performance;
- semantic/legal correctness from Lodestar's software guardrails;
- sole authorship of team-developed Clear Run source;
- production adoption, revenue or user-scale metrics where they have not been measured;
- AI/ML significance for projects that are ordinary software engineering.

For a claim-by-claim proof map, see [HEADLINE_EVIDENCE_MATRIX.md](docs/HEADLINE_EVIDENCE_MATRIX.md). For the final maintainer release decision, see [FINAL_RELEASE_AUDIT_2026-09-18.md](docs/FINAL_RELEASE_AUDIT_2026-09-18.md).

---

**GitHub:** [razaumair2203-ux](https://github.com/razaumair2203-ux) · **Google Scholar:** [Muhammad Umair Raza](https://scholar.google.com/citations?user=0EVckyAAAAAJ&hl=en) · **LinkedIn:** [M. Umair Raza](https://www.linkedin.com/in/mumairaza)

**Repository rights:** [portfolio evidence license / rights notice](LICENSE)
