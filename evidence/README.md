# Code and data

Runnable code, test fixtures and result files behind the portfolio. Run everything from the repository root with Python 3.10+.

| Project | What is here | Run |
|---|---|---|
| [Clear Run](autonomy_edge_ai/clear_run/README.md) | Edge detector excerpt, field-log summary, mission verification matrix | `python evidence/autonomy_edge_ai/clear_run/validate_field_evidence.py` |
| [TIR-FOD](autonomy_edge_ai/tir_fod/README.md) | 29 training-run results, frozen splits, training harness | `python evidence/autonomy_edge_ai/tir_fod/reproducibility/recompute_results.py` |
| Clear Run MBSE | [Telemetry replay cases](autonomy_edge_ai/mbse/telemetry_replay_cases.json) | `python evidence/autonomy_edge_ai/mbse/validate_mbse_evidence.py` |
| [Lodestar](compliance_regtech/lodestar/README.md) | Hybrid retrieval, reranking, guardrails, PostgreSQL/pgvector tests | `python -m evidence.compliance_regtech.lodestar.reliability_regression` |
| [i-MSHA](compliance_regtech/i_msha/README.md) | v1 development figures | — |
| AI evaluation | [Aggregate results](assurance_digital_engineering/ai_evaluation/evaluation_summary.json) | `python evidence/assurance_digital_engineering/ai_evaluation/validate_evaluation_summary.py` |

Public repositories:

- [Claude Adversarial Review Lite](https://github.com/razaumair2203-ux/claude-adversarial-review-lite)
- [Codex Adversarial Review Lite](https://github.com/razaumair2203-ux/codex-adversarial-review-lite)
- [JobLooper](https://github.com/razaumair2203-ux/Pub-JobLooper)
- [IN-ARCP radar package](https://github.com/razaumair2203-ux/inarcp)

[Project map](../domains/README.md) · [Back to portfolio](../README.md)
