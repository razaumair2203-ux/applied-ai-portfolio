# Project portfolio — applied AI, autonomy, AI assurance and digital engineering

Projects are grouped by engineering system or product, with role, technical scope, current maturity and open verification stated on each case page.

## Active AI / product programmes

| Project family | My role | Technical scope | Current state |
|---|---|---|---|
| **[Clear Run / TIR-FOD](tir-fod-clear-run.md)** | Research / programme leadership, systems architecture & integration, experiment and validation strategy, deployment review | LWIR dataset engineering, YOLO experiments, Jetson/TensorRT, RGB/LWIR inference, geolocation, MAVLink/REST, GCS, UGV, MBSE | Flight-tested edge-AI work with active UAV–GCS–UGV integration; end-to-end retrieval verification remains open |
| **[Lodestar](lodestar.md)** | System architecture, retrieval/evaluation design, implementation direction, reliability controls | FastAPI, BGE embeddings, PostgreSQL/pgvector, FTS + HNSW, RRF, authority-aware retrieval, structured evidence output | Working private full-stack system with public implementation/evaluation evidence |
| **[i-MSHA / MSHA Compliance SaaS](msha-compliance-ai.md)** | Product/programme direction, AI/data workflow definition, technical review, validation framing | Next.js, FastAPI, PostgreSQL, DuckDB/Parquet, regulatory analytics, risk/inspection workflows, Canary AI | Private product in pre-deployment hardening; production/UAT not claimed |
| **[JobLooper / JobLoop-AI](joblooper-jobpilot.md)** | Product/system design, AI-workflow governance, evaluation and release controls | local-first workflow, deterministic truth/provenance, AI-assisted drafting, held-out evaluation, release gates | Public JobLooper implementation plus private evaluation/development lineage |
| **[Adversarial Review Lite](codex-adversarial-review-lite.md)** | AI-assurance workflow design and cross-model review controls | Claude↔Codex independent review, frozen scope, mutation checks, rubrics, structured findings, human release authority | Two public companion tools: Codex AR-L and Claude AR-L |
| **[BuildSignal AI](buildsignal-ai.md)** | Product direction, AI workflow design, source/review policy, quality governance | Next.js/TypeScript/MDX, research sourcing, media ops, QA, editorial approval and publish gates | Active private editorial / AI research operations platform |

## Completed or bounded AI systems and research

| Project | Scope | Status |
|---|---|---|
| **[Counter-UAS Phase I](counter-uas.md)** | Physical computer-vision drone-detection demonstrator with hardware integration and indoor/outdoor trials | Phase I completed; later RF/acoustic/multisensor work remains research direction |
| **[AI Systems Assurance / MBSE](mbse-ai-assurance.md)** | Capella/Arcadia reconstruction, evidence applicability, interface replay and regression obligations for Clear Run | Current assurance case within the Clear Run programme; INCOSE IACS submission pending review |
| **[Evaluation-Driven AI Workflow Engineering](ai-evaluation-workflows.md)** | Frozen train/validation/held-out evaluation, failure-mode checks, parser rescoring and release safeguards | Historical evaluation case retained as engineering evidence |
| **Published AI / sensing research** | multi-stream object detection, adversarial vision, TIR-FOD, GNSS/CRPA interference suppression | [Research record](../research/README.md) |

## Digital engineering and supporting infrastructure

- **[Super Mushshak digital engineering](super-mushshak-digital-engineering.md)** — completed aircraft-level retrofit record extended into an evidence-linked digital thread; the structured public backbone exists, while executable/parametric twin behaviour remains future work.
- **ATLAS GPU/HPC environment** — accountable technical leadership for a 22-node GPU/HPC research environment supporting AI, simulation and reproducible engineering workflows.
- Broader engineering work includes avionics integration, aircraft development, radar/RF, embedded sensing, configuration management, airworthiness and technical programme delivery. These are foundations for the current AI/autonomy work rather than relabelled AI projects.

[Back to main portfolio](../README.md)
