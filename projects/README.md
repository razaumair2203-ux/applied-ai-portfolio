# Project portfolio — applied AI, autonomy, AI assurance and digital engineering

This inventory describes each project as an **engineering system or product first**: the problem it solves, the scale of the system, the architecture used to solve it, the user's role, and the evidence-backed maturity. Tools are implementation evidence, not substitutes for product value.

## Active AI / product programmes

| Project family | System / product value | Core architecture | My role | Current state |
|---|---|---|---|---|
| **[Clear Run / TIR-FOD](tir-fod-clear-run.md)** | Integrated airfield robotics programme from airborne FOD sensing through geolocation, GCS review/tasking and developing UGV physical recovery | RGB/LWIR · YOLO/SAHI · Jetson Orin Nano/TensorRT · Pixhawk/MAVLink/GNSS · GCS · UGV · evidence-linked MBSE | research/programme leadership, architecture/integration, experiment & V&V strategy, deployment review | flight-tested edge AI; active UAV–GCS–UGV integration; end-to-end retention verification open |
| **[Lodestar](lodestar.md)** | EB-2 NIW / EB-1A evidence-assessment SaaS that maps applicant evidence to Dhanasar/Kazarian criteria, retrieves legal authority, identifies gaps and produces cited bounded assessments | Next.js · FastAPI · PostgreSQL/pgvector · BGE · FTS/HNSW · RRF · authority-aware retrieval · structured refusal controls | system architecture, retrieval/evaluation design, implementation direction, reliability controls | working private full-stack product with real corpus and public-safe implementation/evaluation evidence |
| **[i-MSHA](msha-compliance-ai.md)** | National MSHA data-consolidation and mine-safety decision platform spanning compliance, penalties, inspections, safety, legal, exposure, contractor and acquisition intelligence | Next.js · FastAPI · PostgreSQL · DuckDB/typed Parquet · scheduled public-data pipeline · Canary AI | product/programme direction, systems architecture, AI/data workflow definition, technical review, validation framing | 8 active modules · 25 frontend features · 100 backend handlers; pre-deployment hardening |
| **[JobLooper](joblooper-jobpilot.md)** | Evidence-governed job-application lifecycle from signed career truth and exact JD capture through AI-assisted tailoring, human approval, deterministic document build, submission trace and outcome learning | local-first Python · deterministic state machine · provenance/hashes · DOCX/PDF validation · optional Codex assistance | product/system design, AI-workflow governance, evaluation and release controls | public implementation plus private evaluation/development lineage |
| **[Adversarial Review Lite](codex-adversarial-review-lite.md)** | Cross-model assurance workflow for AI-written software with independent reviewer models, mutation checks and human approval before fixes | Claude↔Codex · skill/runtime contracts · self-test · model fallback · test/rubric inputs · file hashes · HTML report | AI-assurance workflow design and release controls | two public cross-platform companion tools |
| **[BuildSignal AI](buildsignal-ai.md)** | AI-native research-to-publication operations platform with source, rights, QA, review and publication-state governance across text and media | Next.js · TypeScript · MDX · research/source registry · validation commands · admin workflow | product direction, AI workflow design, source/review policy, quality governance | active private platform; local operating workflow implemented |

## Completed or bounded AI systems and research

| Project | System value | Evidence / scale | Status |
|---|---|---|---|
| **[Counter-UAS Phase I](counter-uas.md)** | Physical AI-vision drone-detection prototype that moved from model training into constructed sensing hardware and real trial conditions | laser–camera mount · ~14,000 training images · 1,500-image test set · indoor/outdoor trials | Phase I completed under PI leadership; RF/acoustic/multisensor extension remains research |
| **[AI Systems Assurance / MBSE](mbse-ai-assurance.md)** | Evidence-linked assurance case for the Clear Run mission chain; turns system-boundary failures into requirements and regression obligations | Capella/Arcadia · 3 mission components · 14 logical functions · 13 exchanges · formatter/parser replay that exposed telemetry truncation behavior | current assurance case; INCOSE IACS submission pending review |
| **[Evaluation-Driven AI Workflow Engineering](ai-evaluation-workflows.md)** | Frozen evaluation and release-control framework for AI workflow changes rather than intuition-led prompt iteration | train/validation/held-out cases · fabrication/date/metric checks · parser rescoring · release safeguards | historical evaluation case retained as engineering evidence |
| **Published AI / sensing research** | Peer-reviewed and public research across multi-stream object detection, adversarial vision, thermal FOD and GNSS/CRPA interference suppression | publications, public dataset, reproducibility records | [Research record](../research/README.md) |

## Digital engineering and supporting infrastructure

- **[Super Mushshak digital engineering](super-mushshak-digital-engineering.md)** — first three glass-cockpit prototypes: aircraft-level avionics/sensor integration, electrical/wiring and ARINC interfaces, installed-aircraft tests, flight-test feedback and customer evaluation; now reconstructed into an evidence-linked public digital thread.
- **ATLAS GPU/HPC environment** — accountable technical leadership for a **22-node GPU/HPC research environment** supporting AI, simulation and reproducible engineering workflows.
- Broader engineering work includes avionics integration, aircraft development, radar/RF, embedded sensing, configuration management, airworthiness and technical programme delivery. These are foundations for the current AI/autonomy work rather than relabelled AI projects.

[Back to main portfolio](../README.md)
