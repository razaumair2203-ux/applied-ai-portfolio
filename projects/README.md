# Project portfolio — organized by technical domain

This portfolio is organized around **technical identity and product niche**, not chronology. The common thread is **Applied AI Systems Engineering**: building AI as part of a complete, testable system with explicit data, interfaces, deployment, verification and operational boundaries.

## 1. Autonomous, embedded and edge AI

This is the strongest current engineering domain and the closest continuation of the aerospace/systems background: computer vision, sensing, edge deployment, UAV/UGV integration and system-level verification.

| Project family | System / product value | Core architecture | My role | Current state |
|---|---|---|---|---|
| **[Clear Run / TIR-FOD](tir-fod-clear-run.md)** | Integrated airfield robotics programme from airborne FOD sensing through geolocation, GCS review/tasking and developing UGV physical recovery | RGB/LWIR · YOLO/SAHI · Jetson Orin Nano/TensorRT · Pixhawk/MAVLink/GNSS · GCS · UGV · evidence-linked MBSE | research/programme leadership, architecture/integration, experiment & V&V strategy, deployment review | flight-tested edge AI; active UAV–GCS–UGV integration; end-to-end retention verification open |
| **[Counter-UAS Phase I](counter-uas.md)** | Physical AI-vision drone-detection prototype taken from model training into constructed sensing hardware and real trial conditions | laser–camera mount · computer vision model · ~14,000 training images · 1,500-image test set | Principal Investigator / research direction, prototype and systems-integration oversight | Phase I completed; RF/acoustic/multisensor extension remains research |
| **[AI Systems Assurance / MBSE](mbse-ai-assurance.md)** | Evidence-linked assurance model for the Clear Run mission chain, turning interface and boundary failures into explicit requirements and regressions | Capella/Arcadia · functional exchanges · interface replay · evidence mapping | systems modelling, interface/V&V framing, evidence applicability, regression logic | current assurance case; INCOSE IACS submission pending review |

### Research supporting this domain

- **Low-Latency Architectures for Real-Time Multi-Stream Object Detection** — peer-reviewed computer-vision research.
- **TK-Patch: Universal Top-K Adversarial Patches for Cross-Model Person Evasion** — peer-reviewed adversarial computer-vision research.
- **TIR-FOD v1.2** — public 23-class thermal runway-FOD dataset and associated research.
- Current work is increasingly UAV-centric, combining sensing, edge inference, geolocation, autonomous-system interfaces and verification.

## 2. Compliance and regulatory intelligence

This is a deliberate product niche: converting fragmented authoritative data and evidence into traceable, bounded decision-support systems.

| Project family | System / product value | Core architecture | My role | Current state |
|---|---|---|---|---|
| **[i-MSHA](msha-compliance-ai.md)** | U.S. mine-safety compliance and decision-intelligence platform spanning mine/controller intelligence, violations, penalties, inspections, safety/injury, legal outcomes, occupational exposure, contractors and acquisition due diligence | Next.js · FastAPI · PostgreSQL · DuckDB / typed Parquet · public-data ingestion · Canary AI | product/programme direction, systems architecture, AI/data workflow definition, technical review, validation framing | 8 active modules · 25 frontend features · 100 backend handlers; pre-deployment hardening |
| **[Lodestar](lodestar.md)** | EB-2 NIW / EB-1A evidence-assessment SaaS that maps applicant evidence to legal criteria, retrieves authority, identifies gaps and produces cited bounded assessments | Next.js · FastAPI · PostgreSQL/pgvector · BGE · FTS/HNSW · RRF · authority-aware retrieval · structured refusal controls | system architecture, retrieval/evaluation design, implementation direction, reliability controls | working private full-stack product with real corpus and public-safe implementation/evaluation evidence |

### Reusable compliance-tech pattern

**Authoritative source consolidation → structured evidence model → retrieval/analytics → bounded AI reasoning → cited/traceable decision support → human-controlled action.**

The domain changes; the engineering pattern stays reusable.

## 3. Practical AI products and public utility workflows

These projects are intended to solve recurring real-world workflow problems and, where suitable, be released for public use rather than remain portfolio demonstrations.

| Project family | System / product value | Core architecture | My role | Current state |
|---|---|---|---|---|
| **[JobLooper / JobPilot family](joblooper-jobpilot.md)** | Evidence-governed job-search/application operating system from career truth and exact JD capture through gap analysis, AI-assisted tailoring, human approval, deterministic document build and outcome learning | local-first Python · deterministic state machine · provenance/hashes · DOCX/PDF validation · optional model assistance | product/system design, AI-workflow governance, evaluation and release controls | public implementation plus private evaluation/development lineage |
| **[BuildSignal AI](buildsignal-ai.md)** | AI-native research-to-publication operating system with source, rights, QA, review and publication-state governance across text and media | Next.js · TypeScript · MDX · research/source registry · validation commands · admin workflow | product direction, AI workflow design, source/review policy, quality governance | active private platform; local operating workflow implemented |

## 4. AI assurance, evaluation and digital engineering

These are cross-cutting engineering controls and the bridge between current AI work and the earlier high-integrity aerospace systems background.

| Project / capability | System value | Evidence / scale | Status |
|---|---|---|---|
| **[Adversarial Review Lite](codex-adversarial-review-lite.md)** | Cross-model assurance workflow for AI-written software with independent reviewer models, mutation checks and human approval before fixes | Claude↔Codex companion tools · self-test · model fallback · test/rubric context · file hashes · report | two public cross-platform companion tools |
| **[Evaluation-Driven AI Workflow Engineering](ai-evaluation-workflows.md)** | Frozen evaluation and release-control framework for AI workflow changes rather than intuition-led prompt iteration | train/validation/held-out cases · fabrication/date/metric checks · parser rescoring · release safeguards | retained engineering evidence |
| **[Super Mushshak digital engineering](super-mushshak-digital-engineering.md)** | Completed first-three-prototype glass-cockpit integration programme now reconstructed into an evidence-linked digital thread | requirements · interfaces · configurations · verification · decisions · historical prototype evidence | retrofit completed; digital-thread backbone implemented; executable-twin functions remain future work |
| **ATLAS GPU/HPC environment** | Research-computing platform supporting AI, simulation and reproducible engineering workflows | 22-node GPU/HPC environment · Linux/Ubuntu · SLURM · CUDA · Docker | current accountable technical leadership |

## How the domains fit together

The portfolio is intentionally multi-domain, but it is not random.

- **Autonomous / edge AI** is the primary technical specialization.
- **Compliance intelligence** is the deliberate product vertical being built across regulated domains.
- **AI assurance and digital engineering** provide the verification, evidence and lifecycle discipline that differentiates the work from model-only AI projects.
- **Practical AI utilities** demonstrate product-building capability beyond aerospace and regulated environments.
- The aerospace record supplies the systems-engineering foundation: requirements, interfaces, configuration, qualification, airworthiness, acceptance and lifecycle responsibility.

## Supporting engineering background

Broader work includes aircraft development, avionics integration, radar/RF, embedded sensing, configuration management, airworthiness and technical programme delivery. These are foundations for the current AI/autonomy work rather than relabelled AI projects.

[Back to main portfolio](../README.md)
