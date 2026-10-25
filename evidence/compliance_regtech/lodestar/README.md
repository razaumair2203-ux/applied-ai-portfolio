# Lodestar: retrieval and guardrail code

## What this code shows

The retrieval and output-checking core of Lodestar, runnable on a small public test corpus.

- [legal_chunking.py](legal_chunking.py) — structure-aware chunking
- [embedding_provider.py](embedding_provider.py) — local embedding interface with dimension checks
- [chunks_schema.sql](chunks_schema.sql) — PostgreSQL schema with full-text and HNSW vector indexes
- [hybrid_retrieval.py](hybrid_retrieval.py) — lexical and vector search fused with Reciprocal Rank Fusion
- [rerank.py](rerank.py) — authority-aware reranking
- [grounding_eval.py](grounding_eval.py) and [grounding_pairs.json](grounding_pairs.json) — the 34-query retrieval test ([results](grounding-eval.md))
- [reliability_regression.py](reliability_regression.py) — 11 control invariants
- [fixture/](fixture/README.md) — real PostgreSQL + pgvector test
- [assessment_eval/](assessment_eval/README.md) — 10 adversarial output cases

On the full private corpus (209 documents, 2,945 chunks), **33 of 34** queries return the expected source in the top 5.

## How to run

From the repository root (standard library only):

```bash
python -m evidence.compliance_regtech.lodestar.public_smoke_test
python -m evidence.compliance_regtech.lodestar.reliability_regression
python -m evidence.compliance_regtech.lodestar.assessment_eval.run_eval
```

Database tests: see [fixture setup](fixture/README.md).

[Lodestar case study](../../../domains/02-compliance-regtech/lodestar.md) · [Back to portfolio](../../../README.md)
