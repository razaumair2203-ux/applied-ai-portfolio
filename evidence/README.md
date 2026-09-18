# Technical implementation and reproducibility

This directory contains the public implementation slices, evaluation fixtures and reproducibility records behind the main project pages.

## Lodestar — RAG / retrieval

Published components include structure-aware chunking, BGE embedding behaviour, PostgreSQL/pgvector schema, hybrid lexical/vector retrieval, RRF, authority-aware reranking, retrieval evaluation, a real PostgreSQL + pgvector fixture and adversarial structured-output evaluation.

Run from the repository root:

```bash
python -m evidence.lodestar.public_smoke_test
python -m evidence.lodestar.reliability_regression
python -m evidence.lodestar.fixture.postgres_fixture_test
python -m evidence.lodestar.fixture.authority_ablation
python -m evidence.lodestar.assessment_eval.run_eval
```

The working private system records **209 source documents, 2,945 embedded chunks and 34 hand-checked retrieval queries with 1 top-5 expected-source miss (2.9%)**. Public evidence now includes an **11-invariant zero-dependency reliability regression**, the real PostgreSQL/pgvector fixture, an authority-policy ablation and the structured-output adversarial evaluation. These validate mechanisms and controls without recreating the private corpus.

## Clear Run — edge deployment and field verification

[evidence/clear-run](clear-run/README.md) publishes a sanitized detector/runtime slice plus a non-location-sensitive field-evidence snapshot and machine-readable detection-to-retention verification matrix. The snapshot covers **8 unique trial videos** and **12 structured RGB events across 8 reported classes**; the verification matrix keeps geolocation accuracy, GCS→UGV acknowledgement, terminal approach, capture and retention explicitly open until measured.

## Counter-UAS Phase I — hardware provenance

The public hardware views are traced to the original Phase-I project archive in [hardware_provenance.json](counter-uas/hardware_provenance.json). The record carries the source and publication-derivative SHA-256 hashes, dimensions and the exact non-semantic image transformations applied for web presentation.

## TIR-FOD — repeated experiments and deployment records

The [reproducibility bundle](tir-fod/reproducibility/README.md) contains **29 sanitized seed-level run records**, the training/evaluation protocol, source-aware split manifest, recorded environment, a GPU training harness and a zero-dependency result recomputation script.

```bash
python evidence/tir-fod/reproducibility/recompute_results.py
```

Historical Jetson measurements are documented separately in [deployment provenance](tir-fod/deployment/README.md). The raw historical ten-run logs and engine were not retained, so those summaries remain historical measurements rather than reconstructed benchmarks.

## Public source repositories

- **Codex Adversarial Review Lite:** <https://github.com/razaumair2203-ux/codex-adversarial-review-lite>
- **JobLooper:** <https://github.com/razaumair2203-ux/Pub-JobLooper>

## Public / private implementation scope

The repository publishes enough code, fixtures and measured artefacts to inspect the engineering path without exposing private programme, institutional or personal material. Team-developed work is identified as such, and private-corpus or historical-device measurements are separated from results that can be rerun directly from this repository.

[Back to main page](../README.md)


## AI systems assurance / MBSE

- [Telemetry replay evidence](mbse/telemetry_replay_cases.json) — three constructed formatter/parser boundary cases and the derived R-COORD / R-ORIGIN requirements.
- [Validator](mbse/validate_mbse_evidence.py) — CI guard for schema, claim boundary, replay classifications and required controls.


## AI workflow evaluation

- [Aggregate historical evaluation summary](ai-evaluation/evaluation_summary.json) — public-safe train/validation/held-out, sensitivity, parser-rescore and safeguard aggregates from the retained JobLoop-AI evaluation workspace.
- [Validator](ai-evaluation/validate_evaluation_summary.py) — CI guard for split counts, disclosed limitations and retained release-blocking safeguard.
