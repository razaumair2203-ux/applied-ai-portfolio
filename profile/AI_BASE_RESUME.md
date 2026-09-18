# Muhammad Umair Raza — AI Systems & Aerospace Engineering Profile

**Applied AI · Edge Computer Vision · Autonomous Systems · Grounded RAG · AI Assurance · Aerospace Systems Engineering · V&V**

[LinkedIn](https://www.linkedin.com/in/mumairaza/) · [GitHub](https://github.com/razaumair2203-ux) · [Google Scholar](https://scholar.google.com/citations?user=0EVckyAAAAAJ&hl=en) · [Applied AI portfolio](../README.md)

## Profile

Applied-AI and aerospace systems-engineering leader with **18+ years** across aircraft development, avionics integration, flight-line MRO, international OEM integration, fleet-scale programme governance and current multidisciplinary R&D leadership.

Current work combines modern AI engineering with the requirements, interfaces, configuration, verification, qualification, safety and lifecycle discipline of high-integrity aerospace systems. The portfolio spans edge computer vision and autonomy, grounded retrieval/RAG, AI-assurance workflows and GPU/HPC research infrastructure.

## AI / ML / autonomy evidence

### TIR-FOD / Clear Run

**Role:** technical direction, experiment/evaluation strategy, systems architecture/integration, deployment review and multidisciplinary team leadership. Clear Run is team-developed work.

- **3,499** LWIR source frames, **5,593** annotated objects, **23** classes and **29** controlled YOLO training runs.
- Source-lineage and leakage analysis includes a controlled contamination experiment producing an invalid **+8.52 percentage-point** mAP@[.50:.95] uplift.
- Acquisition-block-disjoint evaluation produced **0.7410 ± 0.0423** versus **0.8223 ± 0.0070** under frame-level partitioning on the shared 12-class experiment.
- Jetson Orin Nano / FP16 TensorRT UAV deployment with historical **25.0 FPS TensorRT-stage** and **15.6 FPS end-to-end** ten-run summaries.
- Clear Run integrates RGB + passive-IR inference, YOLO/SAHI, geolocation, MAVLink/REST, synchronized recording, GCS handling and a developing UGV retrieval layer.
- Current field-evidence snapshot: **8 unique trial videos** and **12 structured RGB events across 8 reported classes**; target-coordinate, image-location, UAV-pose and altitude fields are recorded.
- GCS→UGV acknowledgement, terminal alignment, physical capture and post-movement retention remain explicit quantitative verification gates.

[Case study](../projects/tir-fod-clear-run.md) · [Dataset DOI 10.5281/zenodo.22546586](https://doi.org/10.5281/zenodo.22546586)

### Lodestar — grounded RAG / evidence assessment

**Role:** system architecture, retrieval/evaluation design, implementation direction, reliability controls, technical validation and product integration.

- Python / FastAPI / PostgreSQL / pgvector / HNSW / PostgreSQL FTS / BGE embeddings.
- Hybrid lexical + vector retrieval with Reciprocal Rank Fusion and deterministic authority-sensitive reranking.
- Recorded private-system state: **209 documents**, **2,945 embedded chunks**, **34 frozen retrieval queries**, **1/34 top-5 expected-source misses (2.9%)**.
- Public evidence includes a real PostgreSQL + pgvector fixture, authority-policy ablation, an **11-invariant reliability regression**, and a **10-case adversarial structured-output evaluation**.
- Output controls include citation validation, evidence-ID filtering, five canonical states, refusal behavior and rejection of unsupported numeric approval fields.

[Case study](../projects/lodestar.md) · [Public implementation evidence](../evidence/lodestar/README.md)

### AI assurance and governed AI workflows

- **Codex Adversarial Review Lite:** independent builder/reviewer workflow with frozen scope, environment checks, mutation detection, rubrics, structured findings and human approval before fixes.
- **JobLooper:** local-first evidence-governed system in which candidate truth, provenance, workflow state, deterministic validation and release authority remain outside unconstrained model output.
- **Counter-UAS Phase I:** completed computer-vision demonstrator with physical sensor integration and indoor/outdoor trials.
- **ATLAS:** accountable technical leadership for a **22-node GPU/HPC** research environment using SLURM, Linux, CUDA and Docker workflows.

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
