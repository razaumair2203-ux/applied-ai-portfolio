# Sources, ownership and measurement boundaries

Evidence reviewed 20 September 2026. Public artefacts below are directly inspectable. Private source locators identify the underlying record; request a relevant extract through [technical review](../PRIVATE_REPOSITORY_ACCESS.md) or [LinkedIn](https://www.linkedin.com/in/mumairaza/). A private record reviewed for this portfolio is not independent public verification.

## Institutional AI and autonomy

| Claim / project | Inspectable evidence | Source and boundary |
|---|---|---|
| TIR-FOD: 3,499 source frames, 5,593 boxes, 23 classes; 29 runs and split/leakage results | [Training protocol and scalar results](autonomy_edge_ai/tir_fod/reproducibility/README.md), [dataset DOI](https://doi.org/10.5281/zenodo.22546586) | Published scalar run records and frozen protocol; this review recomputes summaries, not model training. Acquisition/annotation/model work is team-developed under technical leadership. |
| Jetson: 25.0 FPS inference-stage / 15.6 FPS end-to-end | [Historical measurement record](autonomy_edge_ai/tir_fod/deployment/historical_measurement_status.json) | Author-confirmed ten-run historical summary. Original engine and raw per-run logs were not retained; no independently reproduced deployment benchmark. |
| Clear Run: 8 videos / 12 RGB events / 8 classes | [Aggregate field snapshot](autonomy_edge_ai/clear_run/field_trial_snapshot.json), [mission matrix](autonomy_edge_ai/clear_run/mission_verification_matrix.json), [detector extract](autonomy_edge_ai/clear_run/edge_detector_excerpt.py) | Counts describe retained evidence, not precision/recall, coordinate accuracy or recovery success. |
| ROS2/Nav2/SLAM Toolbox with ROS1 motor bridge | [Public architecture and integration status](../domains/01-autonomy-edge-ai/clear-run-tir-fod.md) | Private `clear-run`, commit `7697822027248fb320ba954734e01894f3415008`, `00_PHASE_II_CONTEXT/RECOVERED_DOCS/ground_unit/auto_navigation.md`, re-inspected 20 Sep 2026. Contains launch/configuration and node implementation. Code inspection does not validate navigation accuracy or unattended recovery. |
| National-scale trials / patenting | [Programme transition statement](../domains/01-autonomy-edge-ai/clear-run-tir-fod.md) | Programme-lead-reported direction: trials and subsequent patent filing planned; no national deployment, filed application or patent grant claimed. |
| Counter-UAS Phase I: hardware, tracking and reported training scale | [Hardware provenance](autonomy_edge_ai/counter_uas/hardware_provenance.json), [case and original trial outputs](../domains/01-autonomy-edge-ai/counter-uas.md) | Private `Anti-Drone_P1`, commit `3ecf64fbe2f3ef1052d578babe26691f0bce961c`, original presentation/video archive and evidence manifest. ~14,000 training images, 1,500 test images and 200 epochs are archive-reported; not a reproduced field benchmark. PI leadership and team implementation are separate. |

## Independent compliance and agentic products

| Claim / project | Source | Boundary |
|---|---|---|
| i-MSHA: 8 active modules, 25 frontend features, 100 backend handlers, 385 Canary / 839 backend tests | Private `Test_1`, commit `1d53064584f1c980a85d088bf4c6ec87c510a1a7`, `MSHA App/project_status.md`, session dated 20 May 2026; re-read 20 Sep 2026 | Historical developer-reported test counts; no fresh suite execution or production/UAT claim. [Public UI and architecture](../domains/02-compliance-regtech/i-msha.md). |
| i-MSHA latency: 100.1→50.8 s cold / 66.8→18.3 s warm | Retained earlier portfolio performance snapshot; underlying timing logs are not published | Aggregate across 152 surfaces, not per-request latency. Not independently rerun in this review; supporting raw measurements remain a review-request item. |
| Lodestar: 209 documents, 2,945 chunks, 1/34 top-5 expected-source misses | Private `lodestar`, commit `f941a3a991411a66bece57a23e43ae45c3f15327`, `docs/grounding-eval.md`, measurement dated 10 July 2026; [public regression definition](compliance_regtech/lodestar/grounding-eval.md) | Expected-source retrieval check on one frozen corpus/query set, not legal correctness. The private corpus is necessary to reproduce that exact result. |
| Lodestar implementation / output controls | [Public code and fixtures](compliance_regtech/lodestar/README.md) | Reproducible public logic/fixture checks are separate from historical corpus results. Owner-directed architecture/evaluation and coding-agent-assisted implementation; no sole manual authorship claim. |
| JobLooper and Adversarial Review Lite | [Public JobLooper source](https://github.com/razaumair2203-ux/Pub-JobLooper), [public review tools](../domains/03-practical-ai-products/adversarial-review-lite.md) | Independent product/workflow design. Public source establishes inspectability; adoption, productivity gains and universal correctness are not claimed. |
| JobLooper historical 50-case evaluation / blocked prompt candidate | [Aggregate summary](assurance_digital_engineering/ai_evaluation/evaluation_summary.json) | May 2026 development snapshot with private input pairs; no hiring-outcome claim. |
| BuildSignal AI | [Product state and contribution](../domains/03-practical-ai-products/buildsignal-ai.md) | Independent owner-reported local workflow; source-derived UI illustration. Hosted authentication and selected integrations remain open. |

## Career and aerospace foundation

The candidate evidence register is private. The identifiers below are stable source locators available for a relevant technical-review request. They distinguish candidate-attested scope from publicly reproducible project results.

| Career statement | Source identifier / evidence | Ownership boundary |
|---|---|---|
| 18+ years in aerospace engineering | Candidate role chronology, service beginning in 2007 | Career duration, not years spent training AI models |
| 100+ project portfolio | `RND-001` / `ROLE-006`, verified candidate record based on base CV | Governance and engineering delivery scope; not 100 personally implemented AI systems |
| 60+ advanced engineering projects | `TEACH-001`, approved record, signed recommendation from Dr Sohail Ahmed; scope corrected 25 Aug 2026 | Supervision/mentoring; no certification-output inference |
| 22-node ATLAS GPU/HPC | `RND-006`, approved accountable-lead record, user confirmation 21 Aug 2026 | Shared institutional environment and technical staff; no utilization or individual job-performance claim |
| 150+ aircraft / 93 upgrade actions | `PMO-003`, approved record, signed recommendation and candidate correction | Fleet configuration-system leadership; no disclosure of aircraft configuration details |
| 135+ units fielded | `DEV-001`, controlled candidate record | Neutral “backup computer subsystem”; qualification/airworthiness evidence support, not approval authority |
| First three Super Mushshak prototypes / lead systems role / sensor and harness scope | Programme-lead retrospective account; [E-24/E-25 and period evidence](https://github.com/razaumair2203-ux/Super-Mushshak-Glass-Cockpit-Modification/blob/main/docs/evidence-register.md) | Three airframes are candidate-reported; two principal avionics paths are distinct. No exact prototype/year mapping inferred from photographs. |

[Research status and contribution](../research/README.md) · [Visual provenance](../visuals/README.md) · [Portfolio](../README.md)
