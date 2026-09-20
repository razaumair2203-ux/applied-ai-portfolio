# Claim sources and limits

This page distinguishes public implementation evidence, retained project summaries and owner-reported career scope. A passing repository check validates the published material's consistency; it does not independently certify historical aircraft work, product deployment or personal authorship.

| Claim family | Inspectable source | What remains bounded |
|---|---|---|
| TIR-FOD: 3,499 frames, 5,593 annotations, 23 classes, 29 runs and repeated-run results | [Protocol, scalar runs and recomputation](autonomy_edge_ai/tir_fod/reproducibility/README.md) | Recomputing recorded scalars is not retraining. Capture-block and frame-split results use different protocols. |
| Historical Jetson 25.0 FPS inference / 15.6 FPS system throughput | [Historical measurement record](autonomy_edge_ai/tir_fod/deployment/historical_measurement_status.json) and runtime screenshot in the case | Author-reported ten-run aggregate; raw timing logs and exact engine/checkpoint are unavailable. |
| Clear Run: eight videos, twelve events, mission status | [Field snapshot](autonomy_edge_ai/clear_run/field_trial_snapshot.json), [mission matrix](autonomy_edge_ai/clear_run/mission_verification_matrix.json) | Event counts and confidence scores do not establish accuracy, surveyed geolocation error or end-to-end recovery success. |
| ROS2 / Nav2 / SLAM Toolbox integration | Recovered navigation implementation record in the private Clear Run source archive, `ground_unit/auto_navigation.md`, inspected at source commit `7697822` | Describes the hybrid ROS1/ROS2 stack. No public trajectory-error, autonomous-success or intervention-rate result; implementation/integration remains ongoing. [Request a focused review](../PRIVATE_REPOSITORY_ACCESS.md). |
| Counter-UAS Phase I training and tracking scope | [Case and hardware provenance](../domains/01-autonomy-edge-ai/counter-uas.md) | Historical presentation/video summaries under PI leadership. No public reproducible accuracy, tracking-error, range or operational-effectiveness benchmark. |
| Lodestar corpus and 1/34 retrieval misses | [Recorded evaluation](compliance_regtech/lodestar/grounding-eval.md), [public code and fixtures](compliance_regtech/lodestar/README.md) | The full result depends on a private corpus. Public fixtures exercise mechanisms, not legal correctness or customer outcomes. |
| i-MSHA module, handler and test counts | [Dated source summary](compliance_regtech/i_msha/README.md) | May 2026 retained development state; not a new full-product test run or production deployment. |
| Agentic workflow evaluation | [Frozen evaluation summary](assurance_digital_engineering/ai_evaluation/evaluation_summary.json) and linked public tools | No adoption, time-saved or recruiter-conversion claim. Agent assistance is part of development. |
| 100+ initiatives, 60+ supervised projects, 22-node ATLAS environment | Approved career statements and retained CV records; [career profile](../profile/AI_BASE_RESUME.md), [ATLAS scope](../domains/04-assurance-digital-engineering/atlas-hpc.md) | Owner-reported scope, not an independently audited count or evidence of sole delivery. The two project counts describe different responsibilities and must not be added. |
| 150+ aircraft, 93 upgrade actions, 135+ subsystem units | Approved career statements; [career profile](../profile/AI_BASE_RESUME.md) | Programme-scale owner reports. Upgrade actions are not distinct aircraft; fleet and production outcomes are not sole-authorship claims. |
| First three Super Mushshak prototypes and Lead Systems Engineer role | Approved career statement plus [aircraft evidence register](https://github.com/razaumair2203-ux/Super-Mushshak-Glass-Cockpit-Modification/blob/main/docs/evidence-register.md), especially E-24/E-25 | Three aircraft prototypes and two principal avionics paths describe different things. Later export configurations and sales remain programme context. |
| National-scale trials and patenting | Programme-lead stated plan | Future path only. No completed national deployment, filed application or granted patent is claimed. |

## Ownership and review

Clear Run, Counter-UAS and ATLAS are institutional work delivered with teams. Compliance products and practical agentic tools are independent development. Product architecture, acceptance and release decisions are owner-directed; agent-assisted code and team output are not described as sole manual implementation.

[Request a project-specific technical review](../PRIVATE_REPOSITORY_ACCESS.md) · [Portfolio](../README.md)
