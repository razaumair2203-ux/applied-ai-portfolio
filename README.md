# Muhammad Umair Raza — AI / R&D Programme Leader · Applied AI Engineer · Aerospace Systems Engineer

**Engineering AI systems from data and models through deployment, interfaces, verification and field evidence.**

**Current role:** Officer In Charge Projects / R&D & Systems Engineering Lead, College of Aeronautical Engineering, NUST · NUTECH assignments · **2023–present**

I lead multidisciplinary engineering and applied-AI programmes while remaining technically hands-on in **system architecture, Python/backend implementation and review, computer vision, RAG/retrieval, AI evaluation, Jetson/TensorRT deployment, interfaces, verification and release controls**.

My foundation is **18+ years in aircraft systems development, avionics integration, V&V, configuration/lifecycle engineering and technical programme delivery**. Current work extends that discipline into edge AI, autonomous systems, grounded GenAI/RAG, AI assurance, digital engineering and data-intensive products.

**Career profile:** [AI-focused base resume](profile/AI_BASE_RESUME.md) · **LinkedIn:** [Profile](https://www.linkedin.com/in/mumairaza/) · **Research:** [Google Scholar](https://scholar.google.com/citations?user=0EVckyAAAAAJ&hl=en) · **Dataset:** [TIR-FOD v1.2](https://doi.org/10.5281/zenodo.22546586)

## At a glance

| Leadership scale | Hands-on technical work | Differentiating foundation |
|---|---|---|
| Leads R&D / systems-engineering activity across a **100+ project portfolio** spanning AI, autonomy, avionics, radar/RF, communications, sensing and embedded systems | Python/backend implementation and review, retrieval/evaluation logic, computer-vision experiments, structured AI workflows, interface analysis and test evidence | **18+ years** across aircraft development, avionics integration, flight-line/MRO engineering, international OEM integration, configuration, qualification and airworthiness |
| Supervised **60+ advanced engineering projects** | Jetson Orin Nano / TensorRT deployment, RGB/LWIR sensing, YOLO/SAHI, FastAPI, PostgreSQL/pgvector, BGE embeddings and RRF | Systems architecture, requirements, interfaces, V&V, configuration control, qualification and acceptance |
| Accountable technical leadership for the **22-node ATLAS GPU/HPC environment** | Held-out evaluation, failure analysis, deterministic guardrails, MBSE/Capella, regression criteria and system-boundary verification | Aircraft/fleet programmes spanning prototype development through production, fielding, upgrades and sustainment |

The through-line is **programme leadership + hands-on AI engineering + aerospace-grade systems discipline**: model performance matters, but so do data lineage, interfaces, configuration identity, evidence quality, failure modes and the boundary between a subsystem result and a verified system capability.

## Applied AI, autonomy and digital engineering

The work spans deployed edge vision, grounded RAG, AI assurance, regulatory intelligence, local-first AI workflows, autonomy integration and digital engineering. Each case states the current system maturity and the verification that remains open.

| Project family | What it is | My role | Current maturity |
|---|---|---|---|
| **[Clear Run / TIR-FOD](projects/tir-fod-clear-run.md)** | Edge computer vision and supervised UAV–GCS–UGV runway-FOD system | research/programme leadership, systems architecture & integration, experiment/V&V strategy, deployment review | flight-tested edge AI; active field integration; end-to-end retrieval verification still open |
| **[Lodestar](projects/lodestar.md)** | Grounded RAG / evidence-assessment system with explicit source authority and refusal controls | system architecture, retrieval/evaluation design, implementation direction, reliability controls | working private full-stack system with public implementation/evaluation evidence |
| **[i-MSHA / MSHA Compliance SaaS](projects/msha-compliance-ai.md)** | AI-enabled regulatory/compliance intelligence platform over structured MSHA public data | product/programme direction, AI/data workflow definition, technical review, validation framing | private product in pre-deployment hardening; production/UAT not claimed |
| **[JobLooper / JobLoop-AI](projects/joblooper-jobpilot.md)** | Local-first AI-assisted application system with deterministic truth, provenance and release authority | product/system design, AI-workflow governance, evaluation and release controls | public implementation plus private evaluation/development lineage |
| **[Adversarial Review Lite](projects/codex-adversarial-review-lite.md)** | Independent Claude↔Codex review toolchain for AI-written code | AI-assurance workflow design, review contracts, human-release controls | two public companion tools |
| **[BuildSignal AI](projects/buildsignal-ai.md)** | AI research/editorial/media operations platform with source, QA and publish governance | product direction, AI workflow design, source/review policy | active private platform |
| **[Counter-UAS Phase I](projects/counter-uas.md)** | Physical computer-vision drone-detection demonstrator | research direction, systems/integration oversight | Phase I completed; later RF/acoustic/multisensor work remains research |
| **[AI Systems Assurance / MBSE](projects/mbse-ai-assurance.md)** | Evidence-linked Capella/Arcadia assurance case within Clear Run | systems modelling, interface/V&V framing, evidence applicability | current assurance case; INCOSE IACS submission pending review |
| **[Super Mushshak digital engineering](projects/super-mushshak-digital-engineering.md)** | Completed glass-cockpit retrofit record extended into an evidence-linked digital thread | historical lead systems/avionics integration role; current retrospective modelling | retrofit completed; public digital-thread backbone implemented; executable twin functions remain future work |

[Complete project inventory and maturity map →](projects/README.md)

## Flagship systems and evidence

Original hardware, field media, product UI and public technical evidence are shown wherever they can be released. Source-derived interface renders are labelled directly when the underlying product remains private.

### Clear Run / TIR-FOD — edge AI moved into a real UAV/autonomy programme

**Scope:** thermal/RGB perception, dataset engineering, source-aware evaluation, TensorRT/Jetson deployment, target geolocation, GCS integration and developing UGV retrieval.

<p align="center">
  <img src="visuals/tir-fod/airborne_platform.png" alt="TIR-FOD airborne edge-AI UAV platform" width="49%">
  <img src="visuals/clear-run/field_trial_evidence.png" alt="Representative Clear Run recorded RGB and passive-IR field detections" width="49%">
</p>

*Airborne prototype and representative recorded RGB/LWIR inference outputs from field trials.*

Key engineering evidence:

- **3,499 source frames · 5,593 annotations · 23 classes · 29 controlled training runs**.
- Controlled leakage experiment: **+8.52 percentage-point invalid mAP uplift** when source lineage is violated.
- Jetson Orin Nano / FP16 TensorRT historical measurement: **25.0 FPS model stage · 15.6 FPS complete pipeline**.
- Current Clear Run evidence snapshot: **8 unique trial videos** and **12 structured RGB events across 8 reported classes**, with image location, target coordinates, UAV pose and altitude recorded.
- GCS→UGV acknowledgement, terminal alignment, physical capture and post-movement retention remain explicit verification gates rather than assumed mission success.
- Clear Run also has an [evidence-linked MBSE assurance case](projects/mbse-ai-assurance.md) covering system boundaries, interface requirements and regression obligations.

[Open the Clear Run / TIR-FOD case →](projects/tir-fod-clear-run.md)

### AI Systems Assurance / MBSE — evidence linked to system boundaries

![Clear Run evidence-linked system architecture](visuals/mbse/clear_run_system_architecture.svg)

*Evidence-linked Clear Run architecture from the current Capella/Arcadia assurance case.*

The assurance case separates detection, geolocation, operator review, ground-vehicle tasking, terminal approach, capture and retained removal into distinct claims with distinct evidence obligations. The current model records **3 mission components · 14 allocated logical functions · 13 logical functional exchanges** and a reproducible formatter/parser replay that exposed interface failure modes without treating constructed software cases as flight incidents. The practitioner case was submitted to **INCOSE Applications & Case Studies on 16 September 2026**; review remains pending.

[Open the AI Systems Assurance / MBSE case →](projects/mbse-ai-assurance.md)

### Lodestar — grounded RAG with explicit retrieval and refusal controls

**Scope:** FastAPI, BGE embeddings, PostgreSQL/pgvector, full-text retrieval, HNSW, RRF, authority-aware candidate handling, citable evidence objects and structured output control.

![Lodestar product surface](visuals/lodestar_product_surface.svg)

*Source-derived rendering of the current Lodestar landing page. The private product does not expose a distributable product screenshot or separate logo asset.*

Recorded engineering state includes **209 documents · 2,945 chunks · a 34-query frozen retrieval regression set · 1 top-5 expected-source miss**. Public fixtures exercise PostgreSQL + pgvector retrieval, authority-policy ablation, an 11-invariant reliability regression and adversarial structured-output controls.

[Open the Lodestar case →](projects/lodestar.md) · [Inspectable implementation evidence →](evidence/lodestar/README.md)

### i-MSHA — full-stack regulatory intelligence with AI inside a larger data product

<p align="center">
  <img src="visuals/msha/logo-wordmark.svg" alt="i-MSHA official project wordmark" width="30%">
</p>

![i-MSHA dashboard regression snapshot](visuals/msha/dashboard-regression.png)

*Official project wordmark and an authentic browser-regression dashboard snapshot from the product test suite.*

The active product combines **Next.js + FastAPI + PostgreSQL + DuckDB/Parquet**, MSHA public-data ingestion/validation, risk/inspection/compliance modules and the Canary AI assistant. The current source-of-truth status records **8 active modules · 25 frontend features · 100 backend handlers**, with **385 Canary unit tests and 839 full backend tests passing** as of 20 May 2026.

**Current boundary:** deployment work remains open in the product plan; production deployment, customer UAT and regulatory certification are not claimed.

[Open the i-MSHA case →](projects/msha-compliance-ai.md)

### JobLooper / JobLoop-AI — AI assistance bounded by deterministic truth and release controls

<p align="center">
  <img src="visuals/joblooper/app-icon.svg" alt="Official JobLooper project mark" width="12%">
</p>

![JobLooper application workspace](visuals/joblooper/dashboard-surface.svg)

*Official JobLooper mark and a source-derived rendering of the current public dashboard.*

The public system keeps career truth, provenance, workflow state and release authority outside unconstrained model output. The wider development/evaluation lineage includes frozen **20 train / 15 validation / 15 held-out** cases, separate fabrication/date/metric checks, parser rescoring and safeguards that can block statistically unsupported changes.

[Open the JobLooper case →](projects/joblooper-jobpilot.md) · [Evaluation case →](projects/ai-evaluation-workflows.md) · [Public repository →](https://github.com/razaumair2203-ux/Pub-JobLooper)

### Adversarial Review Lite — independent AI review as an engineering control

![Adversarial Review Lite report preview](visuals/codex/audit-report-preview.jpg)

*Original report preview from the public Codex Adversarial Review Lite project.*

The companion public tools support both directions:

- [Claude builds → Codex reviews](https://github.com/razaumair2203-ux/codex-adversarial-review-lite)
- [Codex builds → Claude reviews](https://github.com/razaumair2203-ux/claude-adversarial-review-lite)

Both retain frozen review scope, mutation checks, structured findings, builder verification and human authority before fixes.

[Open the AI-assurance case →](projects/codex-adversarial-review-lite.md)

### Counter-UAS Phase I — physical computer vision demonstrator

<p align="center">
  <img src="visuals/counter-uas/outdoor_detection.png" alt="Outdoor Counter-UAS Phase-I detection trial" width="49%">
  <img src="visuals/counter-uas/indoor_detection.png" alt="Indoor Counter-UAS Phase-I detection trial" width="49%">
</p>

*Indoor and outdoor outputs retained from the completed Phase-I computer-vision demonstrator.*

Phase I demonstrates model training moved into a physical sensing setup with real trial conditions and hardware integration. Passive-RF, acoustic and wider multisensor concepts remain separate future research directions.

[Open the Counter-UAS case →](projects/counter-uas.md)

### BuildSignal AI — governed AI research / editorial operations

![BuildSignal AI admin workspace](visuals/buildsignal/admin-surface.svg)

*Source-derived rendering of the current BuildSignal admin workspace. Research, media, QA and publication remain separate reviewable states with owner-controlled release.*

[Open the BuildSignal AI case →](projects/buildsignal-ai.md)

### Super Mushshak — aircraft integration experience carried into digital engineering

<p align="center">
  <img src="https://raw.githubusercontent.com/razaumair2203-ux/Super-Mushshak-Glass-Cockpit-Modification/main/assets/dynon-cockpit-prototype-sanitized.jpg" alt="Original Super Mushshak Dynon SkyView prototype cockpit" width="72%">
</p>

*Original Dynon SkyView prototype cockpit from the public project record.*

The completed retrofit covered aircraft-level sensing, avionics/display integration, interfaces, electrical installation, configuration, installed-aircraft checks and flight-test feedback. The current follow-on has converted releasable historical records into a structured public digital thread linking requirements, interfaces, configurations, verification and decisions; executable twin behaviour remains future work.

[Open the digital-engineering case →](projects/super-mushshak-digital-engineering.md) · [Public source repository →](https://github.com/razaumair2203-ux/Super-Mushshak-Glass-Cockpit-Modification)

## Research and external technical validation

| Public record | Status |
|---|---|
| **Low-Latency Architectures for Real-Time Multi-Stream Object Detection** | IEEE ICoDT2 2025 · [DOI 10.1109/ICoDT269104.2025.11360736](https://doi.org/10.1109/ICoDT269104.2025.11360736) |
| **TK-Patch: Universal Top-K Adversarial Patches for Cross-Model Person Evasion** | IEEE ICoDT2 2025 · [DOI 10.1109/ICoDT269104.2025.11360694](https://doi.org/10.1109/ICoDT269104.2025.11360694) |
| **TIR-FOD v1.2** | public 23-class LWIR runway-FOD dataset · [DOI 10.5281/zenodo.22546586](https://doi.org/10.5281/zenodo.22546586) |
| **Adaptive Interference Suppression in GNSS Using an 8-Element CRPA Antenna Array** | accepted/presented at IBCAST 2026; no DOI/indexing claim until independently verifiable |
| **Evidence-linked MBSE for Clear Run** | submitted to INCOSE Applications & Case Studies on 16 September 2026; editorial review pending |
| **TIR-FOD manuscript** | IEEE Access revision in progress; not represented as published |

[Full research record →](research/README.md)

## Aerospace systems foundation behind the AI work

The AI work sits on top of a longer record of system development, integration and lifecycle responsibility.

- **Aircraft development / systems integration:** JF-17 development and fleet programmes, international OEM systems-engineering work, AEW&C maintenance engineering and trainer-aircraft avionics development.
- **Configuration / lifecycle engineering:** programme-level configuration, upgrade and airworthiness work across a **150+ aircraft** fleet.
- **Prototype-to-field experience:** an indigenous aircraft subsystem progressed through development, qualification and production with **135+ units fielded**.
- **Aircraft retrofit:** led systems engineering / avionics integration for the **first three Super Mushshak glass-cockpit prototypes**.
- **Research infrastructure:** accountable technical leadership for the **22-node ATLAS GPU/HPC environment**, supporting AI, simulation and reproducible engineering workflows.

This background is why the portfolio repeatedly separates **model output from system behaviour, demonstration from verification, and technical possibility from evidence-backed maturity**.

## Engineering approach

- **Evaluation before claims:** source-aware splits, held-out sets, leakage checks, failure cases and explicit metric boundaries.
- **Deployment on the target platform:** model-stage timing is separated from complete pipeline throughput and field behaviour.
- **Interfaces as first-class engineering objects:** producer/consumer contracts, telemetry limits, GCS/vehicle hand-offs and configuration state are explicit.
- **Bounded AI authority:** provenance, source policy, validation, release and human approval stay outside unconstrained model output.
- **Inspectable evidence:** where disclosure permits, this repository publishes code extracts, fixtures, regression cases, data summaries and project-authentic visuals.

## Engineering evidence and reproducibility

[![Engineering validation](https://github.com/razaumair2203-ux/applied-ai-portfolio/actions/workflows/engineering-validation.yml/badge.svg)](https://github.com/razaumair2203-ux/applied-ai-portfolio/actions/workflows/engineering-validation.yml)

The public CI exercises PostgreSQL + pgvector integration, Lodestar retrieval/control regressions, Clear Run field-evidence consistency, MBSE replay evidence, aggregate AI-evaluation evidence and TIR-FOD reproducibility/measurement boundaries.

## Technical stack

**AI / computer vision:** Python · PyTorch / Ultralytics YOLO · SAHI · OpenCV · RGB/LWIR sensing · adversarial/evaluation workflows

**Edge / autonomy:** NVIDIA Jetson Orin Nano · TensorRT · CUDA · GStreamer · Pixhawk · MAVLink · GNSS · UAV/UGV integration

**RAG / backend / data:** FastAPI · PostgreSQL · pgvector · HNSW · PostgreSQL FTS · BGE / sentence-transformers · RRF · DuckDB · Parquet · REST APIs

**Product / platform:** Next.js · TypeScript · local-first Python/Node workflows · CI · structured provenance and release gates

**Systems / validation:** MBSE / Capella · requirements · interfaces · V&V · configuration management · qualification · test/acceptance evidence

## Repository map

- **[profile/AI_BASE_RESUME.md](profile/AI_BASE_RESUME.md)** — AI-focused career profile with full engineering chronology
- **[projects/](projects/README.md)** — project families, roles, maturity and links
- **[evidence/](evidence/README.md)** — implementation extracts, evaluation fixtures and reproducibility records
- **[visuals/](visuals/README.md)** — original project media, official assets, product surfaces and engineering visuals
- **[research/](research/README.md)** — publications, datasets and active research status

## Provenance and claim boundary

Public implementation, dataset records, experiment summaries and sanitized code are linked directly where disclosure permits. Measurements that depend on private corpora or historical hardware runs are identified as such. Team-developed work is not presented as sole authorship, active work is separated from completed results, and private programme material remains outside this repository.

**License / rights:** [LICENSE](LICENSE)
