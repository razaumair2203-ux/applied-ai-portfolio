# Domain map — applied AI systems, product verticals and engineering foundations

This portfolio is organized around **technical identity and product niche**, not chronology. The common thread is **Applied AI Systems Engineering**: building AI as part of a complete, testable system with explicit data, interfaces, deployment, verification and operational boundaries.

## 1. Autonomous, embedded and edge AI

This is the strongest current engineering domain and the closest continuation of the aerospace/systems background: computer vision, sensing, edge deployment, UAV/UGV integration and system-level verification.

| Project family | System / product value | Core architecture | My role | Current state |
|---|---|---|---|---|
| **[Clear Run / TIR-FOD](01-autonomy-edge-ai/clear-run-tir-fod.md)** | Integrated airfield robotics programme from airborne FOD sensing through geolocation, GCS review/tasking and developing UGV physical recovery | RGB/LWIR · YOLO/SAHI · Jetson Orin Nano/TensorRT · Pixhawk/MAVLink/GNSS · GCS · UGV · evidence-linked MBSE | research/programme leadership, architecture/integration, experiment & V&V strategy, deployment review | flight-tested edge AI; active UAV–GCS–UGV integration; end-to-end retention verification open |
| **[Counter-UAS Phase I](01-autonomy-edge-ai/counter-uas.md)** | Physical AI-vision drone-detection prototype taken from model training into constructed sensing hardware and real trial conditions | laser–camera mount · computer vision model · ~14,000 training images · 1,500-image test set | Principal Investigator / research direction, prototype and systems-integration oversight | Phase I completed; RF/acoustic/multisensor extension remains research |

### Research supporting this domain

- **Low-Latency Architectures for Real-Time Multi-Stream Object Detection** — peer-reviewed computer-vision research.
- **TK-Patch: Universal Top-K Adversarial Patches for Cross-Model Person Evasion** — peer-reviewed adversarial computer-vision research.
- **TIR-FOD v1.2** — public 23-class thermal runway-FOD dataset and associated research.
- Current work is increasingly UAV-centric, combining sensing, edge inference, geolocation, autonomous-system interfaces and verification.

## 2. Compliance and regulatory intelligence

This is a deliberate product niche: converting fragmented authoritative data and evidence into traceable, bounded decision-support systems.

| Project family | System / product value | Core architecture | My role | Current state |
|---|---|---|---|---|
| **[i-MSHA](02-compliance-regtech/i-msha.md)** | U.S. mine-safety compliance and decision-intelligence platform spanning mine/controller intelligence, violations, penalties, inspections, safety/injury, legal outcomes, occupational exposure, contractors and acquisition due diligence | Next.js · FastAPI · PostgreSQL · DuckDB / typed Parquet · public-data ingestion · Canary AI | product/programme direction, systems architecture, AI/data workflow definition, technical review, validation framing | 8 active modules · 25 frontend features · 100 backend handlers; pre-deployment hardening |
| **[Lodestar](02-compliance-regtech/lodestar.md)** | EB-2 NIW / EB-1A evidence-assessment SaaS that maps applicant evidence to legal criteria, retrieves authority, identifies gaps and produces cited bounded assessments | Next.js · FastAPI · PostgreSQL/pgvector · BGE · FTS/HNSW · RRF · authority-aware retrieval · structured refusal controls | system architecture, retrieval/evaluation design, implementation direction, reliability controls | working private full-stack product with real corpus and public-safe implementation/evaluation evidence |

### Reusable compliance-tech pattern

**Authoritative source consolidation → structured evidence model → retrieval/analytics → bounded AI reasoning → cited/traceable decision support → human-controlled action.**

The domain changes; the engineering pattern stays reusable.

## 3. Practical agentic AI products and everyday work tools

This is an **independent and growing product stream**: useful AI/agentic software for recurring real-world work, with public/free releases where appropriate. The goal is not prompt demos; it is tools people can repeatedly use with visible state, bounded agent action and human control.

| Project family | System / product value | Core architecture | My role | Current state |
|---|---|---|---|---|
| **[JobLooper](03-practical-ai-products/joblooper-jobpilot.md)** | Evidence-governed job-search/application operating system from career truth and exact JD capture through gap analysis, AI-assisted tailoring, human approval, deterministic document build and outcome learning | local-first Python · deterministic state machine · provenance/hashes · DOCX/PDF validation · optional model assistance | product/system design, AI-workflow governance, evaluation and release controls | public implementation plus private evaluation/development lineage |
| **[BuildSignal AI](03-practical-ai-products/buildsignal-ai.md)** | AI-native research-to-publication operating system with source, rights, QA, review and publication-state governance across text and media | Next.js · TypeScript · MDX · research/source registry · validation commands · admin workflow | product direction, AI workflow design, source/review policy, quality governance | active private platform; local operating workflow implemented |
| **[Adversarial Review Lite](03-practical-ai-products/adversarial-review-lite.md)** | Everyday agentic review tools that make independent second-model review repeatable during AI-assisted coding | Claude↔Codex companion tools · self-test · model fallback · test/rubric context · file hashes · structured report | product/workflow design, assurance logic, human-control model | two public cross-platform companion tools |

## 4. AI assurance, evaluation and digital engineering

This is a **cross-cutting capability layer**, not a separate product stream. It carries verification, evidence, evaluation, configuration and release discipline across autonomy, compliance products and practical agentic tools, and bridges current AI work to the earlier high-integrity aerospace systems background.

| Project / capability | System value | Evidence / scale | Status |
|---|---|---|---|
| **[AI Systems Assurance / MBSE — Clear Run](01-autonomy-edge-ai/ai-systems-assurance-mbse.md)** | Evidence-linked verification layer for the Clear Run mission chain, turning interface and boundary failures into explicit requirements and regressions | Capella/Arcadia · functional exchanges · interface replay · evidence mapping | current assurance case; INCOSE IACS submission pending review |
| **[Evaluation-Driven AI Workflow Engineering](04-assurance-digital-engineering/ai-evaluation-workflows.md)** | Frozen evaluation and release-control framework for AI workflow changes rather than intuition-led prompt iteration | train/validation/held-out cases · fabrication/date/metric checks · parser rescoring · release safeguards | retained engineering evidence |
| **[Super Mushshak digital engineering](04-assurance-digital-engineering/super-mushshak-digital-engineering.md)** | Completed first-three-prototype glass-cockpit integration programme now reconstructed into an evidence-linked digital thread | requirements · interfaces · configurations · verification · decisions · historical prototype evidence | retrofit completed; digital-thread backbone implemented; executable-twin functions remain future work |
| **[ATLAS GPU/HPC environment](04-assurance-digital-engineering/atlas-hpc.md)** | Research-computing platform supporting AI, simulation and reproducible engineering workflows | 22-node GPU/HPC environment · Linux/Ubuntu · SLURM · CUDA · Docker | current accountable technical leadership |

## How the domains fit together

The domains reinforce one engineering profile:

- **Autonomous / edge AI** is the primary technical specialization.
- **Compliance / regulatory intelligence** is a deliberate and actively growing independent product niche across regulated, evidence-heavy domains.
- **Practical agentic work tools** are a second independent and growing product stream for everyday engineering, career, research and knowledge work.
- **AI assurance, evaluation and digital engineering** are cross-cutting disciplines used across both product streams and the professional autonomy work.
- The aerospace record supplies the systems-engineering foundation: requirements, interfaces, configuration, qualification, airworthiness, acceptance and lifecycle responsibility.

## Supporting engineering background

Broader work includes aircraft development, avionics integration, radar/RF, embedded sensing, configuration management, airworthiness and technical programme delivery. These are foundations for the current AI/autonomy work rather than relabelled AI projects.

[Back to main portfolio](../README.md)
