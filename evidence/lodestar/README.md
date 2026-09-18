# Lodestar — inspectable RAG engineering evidence

This folder is a sanitized evidence bundle extracted from the working private **Lodestar** codebase. Its purpose is to let a technical reviewer inspect representative implementation, tests and evaluation rather than infer capability from a résumé keyword.

## Current measured state

| Evidence | State |
|---|---:|
| Real source corpus | **209 documents** |
| Embedded retrieval units | **2,945 chunks** |
| Hand-checked retrieval evaluation | **34 query / expected-source pairs** |
| Top-5 expected-source miss rate | **1 / 34 (2.9%)** |
| Python/backend tests | **53 green** |
| Stress / abuse cases | **17 / 17 passed** |
| Browser E2E | **3 / 3 Playwright flows passed** |
| Concurrent full flows after hardening | **12 / 12 passed** |

The retrieval metric asks a specific engineering question: **did hybrid retrieval surface an accepted authority/citation marker within the top five results?** The recorded result is **1 miss in 34 frozen queries (2.9%)**. This is a targeted regression set, not a population estimate of general RAG error. Retrieval is evaluated independently from generation so fluent model output cannot hide weak evidence retrieval.

## Public reproduction boundary

This directory is a sanitized evidence bundle, not a standalone copy of the private product. A reviewer can reproduce the published pure-logic checks from the repository root with:

```bash
python -m evidence.lodestar.public_smoke_test
```

That zero-dependency check exercises RRF fusion, authority-weighted reranking, retrieval metadata filters, structure-aware chunking and the frozen 34-pair evaluation specification.

A second public path now executes the **actual published hybrid retrieval SQL against PostgreSQL + pgvector** using a small non-sensitive fixture corpus:

```bash
python -m evidence.lodestar.fixture.postgres_fixture_test
```

A third public path evaluates the **downstream structured assessment contract** under adversarial model outputs:

```bash
python -m evidence.lodestar.assessment_eval.run_eval
```

That evaluation checks citation validity, hallucinated-citation dropping, refusal behavior, evidence-ID validity, five-state schema enforcement and removal of unauthorized numeric authority fields. It is explicitly an output-contract evaluation, not a claim of automated legal correctness.

See the [database fixture README](fixture/README.md) and [assessment evaluation README](assessment_eval/README.md). CI runs all public paths on pull requests.

The reported **1/34 top-5 expected-source miss rate (2.9%)** is a recorded full-system measurement from the private **209-document / 2,945-chunk** corpus. The public repository exposes the frozen query/expected-source set and evaluation logic, but it does **not** publish the complete corpus/database and therefore does not claim that the 2.9% full-system result can be reproduced from this repository alone.

## Representative implementation

- [`legal_chunking.py`](legal_chunking.py) — deterministic legal-structure-aware chunking.
- [`embedding_provider.py`](embedding_provider.py) — provider contract, BGE query/passage behavior, model provenance and dimension validation.
- [`chunks_schema.sql`](chunks_schema.sql) — PostgreSQL retrieval plane with `pgvector`, HNSW cosine ANN, full-text search and metadata indexes.
- [`hybrid_retrieval.py`](hybrid_retrieval.py) — lexical + vector retrieval, high-authority candidate lanes, Reciprocal Rank Fusion and citable evidence hydration.
- [`rerank.py`](rerank.py) — deterministic authority-weighted reranking; relevance remains dominant.
- [`grounding_pairs.json`](grounding_pairs.json) — the 34 hand-checked evaluation queries and accepted markers.
- [`grounding_eval.py`](grounding_eval.py) — retrieval-grounding evaluation gate.
- [`retrieval_integration_test.py`](retrieval_integration_test.py) — representative private-product database-backed test shape.
- [`fixture/postgres_fixture_test.py`](fixture/postgres_fixture_test.py) — **publicly runnable real PostgreSQL/pgvector integration test** over the published hybrid retrieval code.
- [`grounding-eval.md`](grounding-eval.md) — current measured result log.

## Design decisions visible in the code

- Preserve source/legal structure before applying size-based splitting.
- Use lexical and vector retrieval because they fail differently.
- Fuse rank positions with RRF rather than pretending lexical and cosine scores share a meaningful numeric scale.
- Add high-authority candidate lanes before reranking instead of hoping a downstream prompt repairs weak retrieval.
- Apply a small authority-weighted multiplier so stronger sources are favored without mechanically overriding a clear relevance advantage.
- Stamp embedding model/version/dimension as provenance and treat embeddings/indexes as rebuildable derived state.
- Return source metadata and citation labels with retrieval objects so evidence survives into downstream assessment.
- Use DB integration, browser, stress/abuse and concurrent-flow tests in addition to unit-level behavior.
- Fall back to lexical retrieval instead of making the application unusable while embeddings are unavailable.

## Operationalization work visible in the private system

The working application includes pooled database connections, batched inserts, guarded embedding initialization, audit logging, deletion paths, authentication scaffolding and test/evaluation gates. Current engineering continues to deepen observability, security and regression automation as the system evolves.

The complete application remains private because it contains product internals and personal/candidate data structures. This folder contains selected non-sensitive implementation evidence only.

[Back to Lodestar case study](../../projects/lodestar.md) · [Back to portfolio](../../README.md)
