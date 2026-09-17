# Lodestar — inspectable RAG engineering evidence

This folder is a sanitized evidence bundle extracted from the working private **Lodestar** codebase. Its purpose is to let a technical reviewer inspect representative implementation, tests and evaluation rather than infer capability from a résumé keyword.

## Current measured state

| Evidence | State |
|---|---:|
| Real source corpus | **209 documents** |
| Embedded retrieval units | **2,945 chunks** |
| Hand-checked retrieval evaluation | **34 query / expected-source pairs** |
| Top-5 retrieval-grounding error | **2.9%** |
| Python/backend tests | **53 green** |
| Stress / abuse cases | **17 / 17 passed** |
| Browser E2E | **3 / 3 Playwright flows passed** |
| Concurrent full flows after hardening | **12 / 12 passed** |

The retrieval metric asks a specific engineering question: **did hybrid retrieval surface an accepted authority/citation marker within the top five results?** Retrieval is evaluated independently from generation so fluent model output cannot hide weak evidence retrieval.

## Representative implementation

- [`legal_chunking.py`](legal_chunking.py) — deterministic legal-structure-aware chunking.
- [`embedding_provider.py`](embedding_provider.py) — provider contract, BGE query/passage behavior, model provenance and dimension validation.
- [`chunks_schema.sql`](chunks_schema.sql) — PostgreSQL retrieval plane with `pgvector`, HNSW cosine ANN, full-text search and metadata indexes.
- [`hybrid_retrieval.py`](hybrid_retrieval.py) — lexical + vector retrieval, high-authority candidate lanes, Reciprocal Rank Fusion and citable evidence hydration.
- [`rerank.py`](rerank.py) — deterministic authority-sensitive reranking; relevance remains dominant.
- [`grounding_pairs.json`](grounding_pairs.json) — the 34 hand-checked evaluation queries and accepted markers.
- [`grounding_eval.py`](grounding_eval.py) — retrieval-grounding evaluation gate.
- [`retrieval_integration_test.py`](retrieval_integration_test.py) — representative database-backed test using known expected sources.
- [`grounding-eval.md`](grounding-eval.md) — current measured result log.

## Design decisions visible in the code

- Preserve source/legal structure before applying size-based splitting.
- Use lexical and vector retrieval because they fail differently.
- Fuse rank positions with RRF rather than pretending lexical and cosine scores share a meaningful numeric scale.
- Add high-authority candidate lanes before reranking instead of hoping a downstream prompt repairs weak retrieval.
- Keep authority as a near-tie preference so relevance is not overridden mechanically.
- Stamp embedding model/version/dimension as provenance and treat embeddings/indexes as rebuildable derived state.
- Return source metadata and citation labels with retrieval objects so evidence survives into downstream assessment.
- Use DB integration, browser, stress/abuse and concurrent-flow tests in addition to unit-level behavior.
- Fall back to lexical retrieval instead of making the application unusable while embeddings are unavailable.

## Operationalization work visible in the private system

The working application includes pooled database connections, batched inserts, guarded embedding initialization, audit logging, deletion paths, authentication scaffolding and test/evaluation gates. Current engineering continues to deepen observability, security and regression automation as the system evolves.

The complete application remains private because it contains product internals and personal/candidate data structures. This folder contains selected non-sensitive implementation evidence only.

[Back to Lodestar case study](../../projects/lodestar.md) · [Back to portfolio](../../README.md)
