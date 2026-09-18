# Lodestar — published RAG implementation slice

This directory contains sanitized implementation, fixtures and evaluation code extracted from the working private Lodestar system.

## Recorded system state

| Item | Recorded state |
|---|---|
| Source documents | **209** |
| Embedded chunks | **2,945** |
| Frozen retrieval queries | **34** |
| Top-5 expected-source misses | **1 / 34 (2.9%)** |
| Public real-DB path | PostgreSQL + pgvector fixture |
| Reliability regression | **11 public invariants** |
| Structured-output evaluation | **10 adversarial cases** |

The 34-query metric asks whether an accepted authority/citation marker appears within the top five results. It is a focused retrieval regression set, not a population estimate of general RAG accuracy.

## Run the public checks

```bash
python -m evidence.compliance_regtech.lodestar.public_smoke_test
python -m evidence.compliance_regtech.lodestar.reliability_regression
python -m evidence.compliance_regtech.lodestar.fixture.postgres_fixture_test
python -m evidence.compliance_regtech.lodestar.fixture.authority_ablation
python -m evidence.compliance_regtech.lodestar.assessment_eval.run_eval
```

The zero-dependency reliability regression publishes **11 control invariants** distilled from the working system: RRF overlap/top-rank behavior, bounded authority preference, relevance override, identity reranking, metadata filters, structure-aware chunking, hallucinated-citation refusal, evidence-ID filtering, canonical output fields and invalid-state rejection. The real-DB fixture then executes the published hybrid retrieval SQL against PostgreSQL + pgvector on a small non-sensitive corpus. The structured-output evaluation separately tests citation validity, evidence-ID filtering, refusal behaviour and schema constraints over frozen adversarial cases.

## Representative implementation

- [legal_chunking.py](legal_chunking.py) — structure-aware chunking
- [embedding_provider.py](embedding_provider.py) — local embedding provider, provenance and dimensionality checks
- [chunks_schema.sql](chunks_schema.sql) — PostgreSQL schema, FTS and HNSW vector index
- [hybrid_retrieval.py](hybrid_retrieval.py) — lexical/vector candidate lanes, RRF and evidence hydration
- [rerank.py](rerank.py) — deterministic authority-sensitive reranking
- [grounding_pairs.json](grounding_pairs.json) — frozen retrieval evaluation set
- [grounding_eval.py](grounding_eval.py) — retrieval-grounding evaluation
- [reliability_regression.py](reliability_regression.py) — 11 zero-dependency reliability/control invariants
- [fixture/postgres_fixture_test.py](fixture/postgres_fixture_test.py) — real PostgreSQL/pgvector integration path
- [fixture/authority_ablation.py](fixture/authority_ablation.py) — two-lane vs four-lane vs reranked policy comparison
- [assessment_eval/run_eval.py](assessment_eval/run_eval.py) — adversarial structured-output evaluation

## Design choices visible in the code

- lexical and vector rankings remain separate until **Reciprocal Rank Fusion**;
- high-authority lexical/vector lanes keep controlling sources in the candidate pool;
- deterministic authority reranking occurs after fusion;
- citable evidence objects carry source and citation metadata downstream;
- provider metadata and embedding dimensionality are validated;
- unsupported structured assessments can be forced to a refusal path.

## Public / private scope

The private corpus and complete product database are not published, so the exact **1/34** full-system result cannot be independently recreated from this repository alone. The public fixture and evaluation code validate the published retrieval and output-control mechanisms on non-sensitive data.

[Back to Lodestar case study](../../../domains/02-compliance-regtech/lodestar.md) · [Back to technical implementation](../../README.md)
