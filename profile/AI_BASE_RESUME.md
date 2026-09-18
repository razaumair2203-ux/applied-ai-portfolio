# Muhammad Umair Raza — Applied AI Systems & Aerospace Engineering Profile

**Autonomous & Edge AI · Computer Vision · Compliance / Regulatory Intelligence · AI Assurance · Aerospace Digital Engineering**

[LinkedIn](https://www.linkedin.com/in/mumairaza/) · [GitHub](https://github.com/razaumair2203-ux) · [Google Scholar](https://scholar.google.com/citations?user=0EVckyAAAAAJ&hl=en) · [Applied AI portfolio](../README.md)

## Profile

Applied-AI systems and aerospace-engineering leader with **18+ years** across aircraft development, avionics integration, flight-line MRO, international OEM integration, fleet-scale programme governance and current multidisciplinary R&D leadership.

My primary current technical domain is **autonomous / embedded / edge AI**, especially computer vision, UAV/UGV systems, RGB/LWIR sensing, Jetson/TensorRT deployment and system-level verification. In parallel, I am building a deliberate product niche in **compliance and regulatory intelligence**, applying retrieval, structured evidence models, analytics and bounded AI reasoning to regulated decision environments.

The wider portfolio also includes an **independent and growing practical-agentic product stream** for everyday engineering, career, research and knowledge work, alongside cross-cutting AI assurance, evaluation/release controls, GPU/HPC research infrastructure and aerospace digital engineering. The common thread is **Applied AI Systems Engineering**: AI treated as part of a complete engineered system with explicit data, interfaces, configuration, verification and operational boundaries.

## Applied AI evidence by domain

### Autonomous, embedded and edge AI

#### TIR-FOD / Clear Run

**Role:** technical direction, experiment/evaluation strategy, systems architecture/integration, deployment review and multidisciplinary team leadership. Clear Run is team-developed work.

- **3,499** LWIR source frames, **5,593** annotated objects, **23** classes and **29** controlled YOLO training runs.
- Source-lineage and leakage analysis includes a controlled contamination experiment producing an invalid **+8.52 percentage-point** mAP@[.50:.95] uplift.
- Acquisition-block-disjoint evaluation produced **0.7410 ± 0.0423** versus **0.8223 ± 0.0070** under frame-level partitioning on the shared 12-class experiment.
- Jetson Orin Nano / FP16 TensorRT UAV deployment with historical **25.0 FPS TensorRT-stage** and **15.6 FPS end-to-end** ten-run summaries.
- Clear Run integrates RGB + passive-IR inference, YOLO/SAHI, geolocation, MAVLink/REST, synchronized recording, GCS handling and a developing UGV retrieval layer.
- Current field-evidence snapshot: **8 unique trial videos** and **12 structured RGB events across 8 reported classes**; target-coordinate, image-location, UAV-pose and altitude fields are recorded.
- GCS→UGV acknowledgement, terminal alignment, physical capture and post-movement retention remain explicit quantitative verification gates.

[Case study](../domains/01-autonomy-edge-ai/clear-run-tir-fod.md) · [Dataset DOI 10.5281/zenodo.22546586](https://doi.org/10.5281/zenodo.22546586)

#### Counter-UAS Phase I — physical AI-vision research prototype

**Role:** Principal Investigator / research direction and systems-integration oversight.

- Constructed laser–camera sensing mount and visual drone-detection prototype taken from model development into preliminary indoor/outdoor trials.
- Historical experiment record: approximately **14,000 training images**, **1,500-image test set**, **200 epochs** at 640×640 input.
- Follow-on visual/RF/acoustic multisensor work remains a research direction and is not back-claimed as completed Phase-I capability.

[Case study](../domains/01-autonomy-edge-ai/counter-uas.md)

### Compliance and regulatory intelligence

#### i-MSHA — U.S. mine-safety intelligence and MSHA decision platform

**Role:** product/programme direction, systems architecture, AI/data workflow definition, technical review, feature prioritisation and validation framing.

- Consolidates fragmented MSHA public data into a national→state→mine/controller decision environment across **8 active modules, 25 frontend features and 100 backend handlers**.
- Scope spans mine/controller profiles, violations, penalties, inspections, injury/safety, legal intelligence, occupational exposure, contractor intelligence, acquisition due diligence, comparison and Weekly Pulse.
- Full-stack architecture: **Next.js / TypeScript · FastAPI / Python · PostgreSQL · DuckDB over typed Parquet**, with scheduled ingestion/validation and refresh workflows.
- **Canary AI** operates across the governed product data paths using context-first routing and deterministic feature handlers rather than acting as the regulatory source of truth.
- Recorded validation state: **385 Canary unit tests and 839 full backend tests passing** (20 May 2026).
- A retained performance audit covered **152 surfaces**; cumulative cold latency improved from **100.1 s to 50.8 s** and warm latency from **66.8 s to 18.3 s** after query-batching work.
- Current maturity is pre-deployment hardening; production deployment/UAT are not claimed.

[Case study](../domains/02-compliance-regtech/i-msha.md)

#### Lodestar — EB-2 NIW / EB-1A evidence-assessment SaaS

**Role:** system architecture, legal-RAG retrieval/evaluation design, implementation direction, reliability controls, technical validation and product integration.

- Working browser product for applicant evidence assessment against **Matter of Dhanasar** (EB-2 NIW) and **Kazarian** (EB-1A) legal frameworks.
- User flow: onboarding → PDF/DOCX/TXT evidence upload → targeted gap questions → user-confirmed evidence mapping → grounded assessment.
- Produces evidence matrices, gap analysis, cited assessment states and drafting aids; deliberately excludes fabricated approval probabilities, numeric legal scores and finished petition generation.
- **Next.js / TypeScript · FastAPI / Python · PostgreSQL / pgvector · HNSW · PostgreSQL FTS · BGE embeddings**.
- Recorded private-system state: **209 documents**, **2,945 embedded chunks**, **34 frozen retrieval queries**, **1/34 top-5 expected-source misses (2.9%)**.
- Hybrid lexical + vector retrieval uses Reciprocal Rank Fusion and deterministic authority-sensitive reranking so source authority is a system concern, not prompt decoration.
- Public evidence includes a real PostgreSQL + pgvector fixture, authority-policy ablation, an **11-invariant reliability regression** and adversarial structured-output evaluation with citation/refusal controls.

[Case study](../domains/02-compliance-regtech/lodestar.md) · [Public implementation evidence](../evidence/compliance_regtech/lodestar/README.md)

### Independent practical agentic AI products and everyday work tools

These are independent product-building efforts, separate from NUST/CAE employment. They form a growing part of the applied-AI identity and are intended to become usable public/free tools where appropriate.

#### JobLooper — evidence-governed job-application operating system

- Governs the lifecycle from **signed career truth and exact JD capture through gap/preflight decisions, AI-assisted tailoring, full human review, deterministic DOCX/PDF build, hash-bound submission records and outcome learning**.
- Truth, provenance, workflow state and release authority remain deterministic; AI can assist reasoning but cannot silently rewrite facts, approve documents or manufacture outcome explanations.
- Public local-first implementation plus a private frozen **20 train / 15 validation / 15 held-out** evaluation lineage with fabrication/date/metric checks and release safeguards.

[Case study](../domains/03-practical-ai-products/joblooper-jobpilot.md)

#### BuildSignal AI — governed research-to-publication operations

- Active AI-native workflow platform spanning research/source capture, articles, media, video, audio, YouTube, social variants, QA, rights/provenance, review and explicit owner-controlled publication.
- Treats generative AI as one worker inside a governed content-production system rather than allowing generated output to move directly to publication.

[Case study](../domains/03-practical-ai-products/buildsignal-ai.md)

#### Adversarial Review Lite — everyday agentic review tools with assurance built in

- Two public companion tools implement **Claude builds → Codex reviews** and **Codex builds → Claude reviews**.
- Primary product identity is practical utility for normal AI-assisted coding; frozen review scope, tests/fixtures/rubrics, self-test/model fallback, repository mutation/hash checks and human approval provide the assurance layer.
- The bounded-agent / independent-check / human-approval pattern also transfers into compliance and regulated AI products.

[Case study](../domains/03-practical-ai-products/adversarial-review-lite.md)

### Cross-cutting AI assurance, evaluation and research infrastructure

#### ATLAS — GPU/HPC research infrastructure

- Accountable technical leadership for a **22-node GPU/HPC** research environment supporting AI, simulation and reproducible engineering workflows.
- Operating stack includes **Linux / Ubuntu, SLURM, CUDA and Docker**, with responsibility extending to research-computing operations and associated technical staff.

## Current engineering / R&D leadership

### Officer In Charge Projects / R&D & Systems Engineering Lead  
**College of Aeronautical Engineering, NUST / NUTECH assignments · 2023–present**

- Leads governance and engineering delivery across a **100+ project** portfolio covering avionics, radar/RF, communications, embedded systems, sensing, UAV/autonomy and AI.
- Has supervised **60+ advanced engineering projects** and teaches Systems Engineering, Project Management and Avionics System Design.
- Leads or supervises work in edge AI, multi-stream computer vision, thermal/RGB sensing, adversarial robustness, radar/signal processing, autonomous systems and digital-engineering applications.
- Accountable for ATLAS research-computing operations and associated technical staff.
- Governs requirements, architecture, interfaces, formal reviews, procurement, RAID, integration, capability demonstrations and technical acceptance.

## Aerospace systems engineering and programme experience

### Deputy Director Avionics / PMO — JF-17 Programme  
**Pakistan Air Force · 2019–2022**

- Architected and deployed a fleet configuration-management system controlling hardware/software baselines and modification status while **93 upgrade actions** were embodied across **150+ aircraft** and four concurrent configurations.
- Managed programme-level integration, qualification, airworthiness, flight-test, MRO, sustainment, obsolescence and lifecycle dependencies.
- Led cross-functional IPT activity across engineering, software, flight test, maintenance, logistics, depots, OEMs, suppliers and operational users.
- Contributed to fleet-readiness initiatives sustaining aircraft serviceability above **90%**.
- Worked through military airworthiness / PACA approval routes, technical investigation and Safety Management System responsibilities.

### Systems Engineering Lead — International OEM Assignment  
**Chengdu Aircraft Design Institute, China · 2017–2019**

- Spent more than two years embedded in the lead design institute as customer-side systems-engineering lead for JF-17 Block III and dual-seat development.
- Coordinated requirements, architecture, hardware/software interfaces, integration-rig V&V, test readiness, defect closure and acceptance evidence.
- Authored/reviewed acceptance-test specifications and supported FAT/SAT, drawing-set acceptance and technology/production transfer.
- Worked across international OEM/customer interfaces, design change, qualification and configuration control.

### Maintenance Support Engineer — ZDK-03 AEW&C  
**Pakistan Air Force · 2015–2017**

- Led flight-line MRO engineering for avionics/C2 mission systems, including fault isolation, planned/corrective maintenance, recovery planning and functional checks.
- Used MTBF/MTTR and failure trends to support preventive-maintenance, spares and OEM decisions.
- Supported major-overhaul activity from the avionics/systems side, defect closure, configuration status and return-to-service coordination.

### Full-time MS study — Avionics Engineering  
**Air University · 2013–2015; degree conferred 2017**

- Signal & Image Processing focus.
- Research addressed ECCM techniques for legacy radar under pulse-jamming conditions.

### Avionics Development & Integration Engineer  
**Pakistan Aeronautical Complex Kamra / Pakistan Air Force · 2008–2013**

- Developed and fielded an indigenous backup computer subsystem for JF-17 from requirements/design through qualification, airworthiness evidence, flight-test support and production handover; **135+ units fielded**.
- Led avionics integration of the **first three Super Mushshak glass-cockpit prototypes**, including Dynon/Garmin evaluation, interface analysis, installation, testing, compliance evidence, configuration control and production handover.
- Delivered avionics development/integration across trainer and fighter platforms from requirements and interfaces through ground/functional testing and configuration control.

## Systems-engineering depth

- Requirements engineering, architecture, interfaces and traceability.
- Verification & validation, qualification, test plans/procedures, FAT/SAT and acceptance evidence.
- Configuration management, baseline control and change-impact analysis.
- Hardware/software/aircraft integration and hardware-in-the-loop / integration-rig testing.
- Airworthiness, safety, technical investigation and lifecycle assurance.
- Flight-line and depot MRO, reliability, MTBF/MTTR, obsolescence and sustainment.
- Programme delivery: WBS, EVM, RAID, procurement, OEM/supplier management and executive reporting.
- MBSE / systems tools include IBM Rational DOORS, Cameo/Capella and SysML-oriented workflows.

## Technical stack

**AI / computer vision:** Python · PyTorch / Ultralytics YOLO · SAHI · OpenCV · RGB/LWIR sensing

**Edge / autonomy:** NVIDIA Jetson Orin Nano · TensorRT · CUDA · GStreamer · Pixhawk · MAVLink · GNSS · UAV/UGV integration

**RAG / backend:** FastAPI · PostgreSQL · pgvector · HNSW · PostgreSQL FTS · BGE / sentence-transformers · REST APIs

**Research computing:** Linux / Ubuntu · SLURM · Docker · CUDA · GPU/HPC operations

**Engineering:** systems architecture · requirements · V&V · configuration management · technical programme management · safety / airworthiness interfaces

## Education

- **BE Avionics Engineering**, National University of Sciences and Technology / College of Aeronautical Engineering, 2008 — CGPA **3.25**.
- **MS Avionics Engineering — Signal & Image Processing**, Air University; full-time study 2013–2015, degree conferred 2017.

## Professional credentials and development

- Project Management Professional (**PMP**).
- PMI Agile Certified Practitioner (**PMI-ACP**).
- Professional Engineer (**PE**), Pakistan Engineering Council.
- Systems Engineering development through Chengdu Aircraft Design Institute and University of Colorado Boulder coursework/specialization.
- Engineering Project Management — Rice University.
- Aircraft technology-transfer / software-configuration training.
- ZDK-03 military-aircraft type qualification.
- Technical Investigation Course.
- HEC/NAHE capacity-building and quality-assurance development.
- Google Data Analytics Foundations and University of Michigan Python coursework.

## Research and public technical record

- **Low-Latency Architectures for Real-Time Multi-Stream Object Detection**, IEEE ICoDT2 2025 — DOI [10.1109/ICoDT269104.2025.11360736](https://doi.org/10.1109/ICoDT269104.2025.11360736).
- **TK-Patch: Universal Top-K Adversarial Patches for Cross-Model Person Evasion**, IEEE ICoDT2 2025 — DOI [10.1109/ICoDT269104.2025.11360694](https://doi.org/10.1109/ICoDT269104.2025.11360694).
- **Adaptive Interference Suppression in GNSS Using an 8-Element CRPA Antenna Array** — accepted/presented at IBCAST 2026; no DOI/indexing claim is made here.
- **TIR-FOD v1.2** public dataset — DOI [10.5281/zenodo.22546586](https://doi.org/10.5281/zenodo.22546586).
- TIR-FOD IEEE Access manuscript — revision in progress in 2026.

## Selected recognition

- Chief of the Air Staff Commendation for exceptional services during an avionics integration / retrofit programme.
- Chairman, Pakistan Aeronautical Complex Board Commendation for devotion to duty and valuable services to Pakistan Aeronautical Complex.
- Chengdu Aircraft Design Institute leadership recognition for aircraft-development and systems-integration contributions.

---

This public profile summarizes verified career and project evidence. It intentionally omits private contact details, internal evidence identifiers and restricted programme details. Project-specific ownership and maturity boundaries remain authoritative in the linked case studies.
