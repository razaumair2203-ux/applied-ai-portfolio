# Project and maturity inventory

This inventory separates **inspectable AI engineering**, **active systems/R&D integration**, and **adjacent engineering leadership**. A project appearing here does not mean every subsystem or line of code was authored personally; ownership language follows the actual role.

## A. Direct, inspectable AI / software engineering evidence

| Project | Evidence depth | Current maturity |
|---|---|---|
| [Lodestar](lodestar.md) | Python/FastAPI backend, structure-aware ingestion/chunking, BGE embeddings, PostgreSQL/pgvector, HNSW + FTS hybrid retrieval, RRF, reranking, LLM integration, automated evaluation/tests and browser flow | Working **pre-production** private system; sanitized implementation/evaluation is public here |
| [TIR-FOD](tir-fod-clear-run.md) | Real LWIR runway dataset, repeated YOLO experiments, leakage/generalisation studies, Jetson Orin Nano/TensorRT, integrated UAV flight trials and public dataset | Public research dataset + **flight-tested prototype**; IEEE Access manuscript under revision |
| [Codex Adversarial Review Lite](codex-adversarial-review-lite.md) | Public skill/source, independent builder-reviewer control flow, model preflight/fallback, mutation checks, structured audit, human approval | Public working tool |
| [JobLooper](joblooper-jobpilot.md) | Public Python local-first workflow, provenance/hashes, deterministic validation/release state, CLI/dashboard/document build, optional assistant integration | Public working software |

These four projects are the main evidence for hands-on AI integration, retrieval, computer vision, evaluation, APIs/software, edge deployment and AI-assurance design.

## B. Active AI / autonomy systems integration

| Workstream | What exists now | What remains in progress |
|---|---|---|
| **Clear Run UAV–GCS–UGV FOD retrieval** | Day/night aerial detection tested; telemetry/video recording; UAV/GCS/UGV experimental platform; UGV hardware/navigation; retrieval CAD; TIR-FOD perception baseline | Complete target hand-off/acknowledgement, retrieval-mechanism integration, terminal alignment, retained-object trials and complete detection-to-retention KPIs |
| [Counter-UAS Phase I](counter-uas.md) | Computer-vision drone-detection demonstrator; indoor/outdoor trials; original visual/training evidence archived with provenance | Passive RF, acoustic and broader multisensor work are proposed research directions, not completed capability |
| **AI imaging / compression and sensing projects** | Current supervised R&D streams inside the CAE project portfolio | Results remain project-specific and should not be promoted to completed public products without evidence |

## C. Research and engineering infrastructure

- [ATLAS GPU/HPC environment](atlas-hpc.md) — GPU/HPC research environment, reproducibility/containers/monitoring/governance work. This is infrastructure leadership, not an AI model claim.
- **GNSS 8-element CRPA interference suppression** — adaptive array / interference-rejection research; accepted/presented IBCAST 2026 work.
- **AERIS-10 radar demonstrator** — RF/antenna/embedded-processing integration and staged V&V.
- **Ku-band phased array, UWB radar and radar/EW teaching labs** — applied RF/signal-processing and engineering-education work.
- **Sensor-enhanced aircraft digital-twin concepts** — systems/digital-engineering work in progress; not represented as a fielded production twin.

## D. Product/software work that is not counted as core AI evidence

[BuildSignal](buildsignal-ai.md) is a Next.js/TypeScript/MDX editorial/product platform with validation and publishing workflows. It demonstrates product/software engineering, but it is intentionally **not** used as a flagship AI credential merely because its subject matter involves AI content.

## Current portfolio leadership context

In my current CAE/NUST role I govern **100+ multidisciplinary engineering and R&D initiatives** across avionics, radar/RF, communications, embedded systems, sensing, UAV/autonomous systems and AI. That number describes portfolio responsibility and technical governance. It does **not** imply personal authorship of every project algorithm, dataset, circuit, mechanical design or codebase.

For recruiter or technical review, start with the direct-evidence projects in Section A and use Sections B–D as systems context rather than mixing all work into one undifferentiated "AI portfolio."

[Back to portfolio](../README.md)
