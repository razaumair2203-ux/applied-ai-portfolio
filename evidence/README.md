# Technical evidence — organized by domain

This directory contains public implementation slices, evaluation fixtures and reproducibility records behind the portfolio. Evidence is grouped by the same technical hierarchy used in the public domain map.

## Autonomous, embedded and edge AI

- **[Clear Run](autonomy_edge_ai/clear_run/README.md)** — sanitized edge-runtime extract, field-evidence snapshot and detection-to-retention verification matrix.
- **[TIR-FOD](autonomy_edge_ai/tir_fod/README.md)** — 29-run reproducibility bundle, source-aware split records and historical Jetson/TensorRT deployment provenance.
- **[Counter-UAS Phase I](autonomy_edge_ai/counter_uas/hardware_provenance.json)** — hardware provenance and publication-derivative hashes.
- **[AI Systems Assurance / MBSE](autonomy_edge_ai/mbse/telemetry_replay_cases.json)** — producer-consumer replay cases and validation logic.

## Compliance and regulatory intelligence

- **[Lodestar](compliance_regtech/lodestar/README.md)** — structure-aware chunking, PostgreSQL/pgvector retrieval, RRF, authority-aware reranking, reliability regression, real-DB fixture and adversarial structured-output evaluation.

Run the Lodestar public checks from the repository root:

```bash
python -m evidence.compliance_regtech.lodestar.public_smoke_test
python -m evidence.compliance_regtech.lodestar.reliability_regression
python -m evidence.compliance_regtech.lodestar.fixture.postgres_fixture_test
python -m evidence.compliance_regtech.lodestar.fixture.authority_ablation
python -m evidence.compliance_regtech.lodestar.assessment_eval.run_eval
```

## AI assurance and digital engineering

- **[AI workflow evaluation](assurance_digital_engineering/ai_evaluation/evaluation_summary.json)** — public-safe frozen train/validation/held-out, sensitivity, parser-rescore and release-safeguard aggregates.
- Public Adversarial Review Lite implementation remains in its dedicated public repositories and is linked from the domain case study.

## Practical AI products

JobLooper and BuildSignal are represented primarily through public/source-derived product surfaces and their case studies. JobLooper's public implementation is maintained in its dedicated repository.

## Public source repositories

- **Codex Adversarial Review Lite:** <https://github.com/razaumair2203-ux/codex-adversarial-review-lite>
- **Claude Adversarial Review Lite:** <https://github.com/razaumair2203-ux/claude-adversarial-review-lite>
- **JobLooper:** <https://github.com/razaumair2203-ux/Pub-JobLooper>

## Scope boundary

The repository publishes enough code, fixtures and measured artefacts to inspect the engineering path without exposing private programme, institutional or personal material. Team-developed work is identified as such, and private-corpus or historical-device measurements are separated from results that can be rerun directly here.

[Domain map](../domains/README.md) · [Back to portfolio](../README.md)
