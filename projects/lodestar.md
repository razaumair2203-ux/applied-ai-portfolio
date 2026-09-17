# Lodestar — grounded RAG and evidence assessment

**Status:** working private full-stack system; selected non-sensitive implementation and evaluation evidence is published in this portfolio.

## Engineering problem

Lodestar evaluates evidence against a legal corpus where retrieval quality, authority and traceability matter more than fluent text. The LLM is downstream of a retrieval and evidence plane rather than being treated as the source of truth.

The working system includes:

- a Python/FastAPI backend;
- PostgreSQL with `pgvector` and full-text search;
- a data-ingestion pipeline and legal-structure-aware chunker;
- BGE query/passage embeddings with provider and dimensionality checks;
- hybrid lexical + vector retrieval;
- Reciprocal Rank Fusion (RRF);
- authority-aware deterministic reranking;
- citable retrieval objects carrying source metadata and binding weight;
- evidence parsing and assessment logic;
- provider-swappable LLM integration;
- a Next.js frontend;
- PostgreSQL and in-memory stores for different execution modes;
- automated backend, database-integration and browser tests.

## Retrieval path

```text
legal / policy corpus
        ↓
structure-aware chunking
        ├─────────────── BGE passage embeddings ──> pgvector / HNSW cosine ─┐
        └─────────────── PostgreSQL tsvector ─────> lexical retrieval ──────┤
                                                                            ↓
                                                     Reciprocal Rank Fusion
                                                                            ↓
                                                     authority-aware rerank
                                                                            ↓
                                                     citable evidence objects
                                                                            ↓
                                                     grounded assessment
```

The hybrid search runs lexical and semantic lanes plus separate high-authority candidate lanes, fuses rank positions using RRF, hydrates the result IDs into citable evidence objects and applies an explainable authority-sensitive reranker. Authority is intentionally a near-tie preference rather than a rule that can bury a highly relevant lower-authority source.

## Measured state

| Measure | Current verified project state |
|---|---:|
| Real source corpus | **209 documents** |
| Embedded corpus | **2,945 chunks** |
| Hand-checked retrieval queries | **34** |
| Retrieval depth | **top-5** |
| Current retrieval-grounding error | **2.9%** |
| Backend/Python tests | **53 green** |
| Stress / abuse cases | **17 / 17 passed** |
| Browser Playwright flows | **3 / 3 passed** |
| Concurrent full flows after hardening | **12 / 12 passed** |

The 2.9% figure is a **retrieval-grounding metric**: for each hand-checked query, the evaluation asks whether an accepted authority/citation marker appears within the top five results. Retrieval quality is measured independently so polished model output cannot hide weak evidence retrieval.

## Reliability and operationalization

The working code includes engineering that is easy to lose in a high-level RAG diagram:

- pooled PostgreSQL connections;
- batched evidence inserts;
- explicit `pgvector` casting on ANN queries;
- UUID validation before SQL execution;
- lazy embedding-model loading, startup warm-up and guarded initialization;
- lexical fallback while a corpus is not yet embedded;
- citation-resolution checks so downstream assessment cannot preserve a citation that was not actually retrieved;
- audit logging and candidate-data deletion paths;
- authentication scaffolding;
- backend, DB integration, browser, stress/abuse and concurrent-flow testing.

The system is designed so retrieval, provenance, evaluation and application logic remain inspectable instead of disappearing behind an LLM call.

## Current engineering focus

Ongoing work expands the frozen evaluation set, downstream grounded-answer evaluation, automated regression gates, observability and security hardening as the system moves through further deployment stages. These are normal evolution items around an already working implementation, not substitutes for the evidence above.

## Inspectable implementation evidence

The public evidence bundle exposes representative, sanitized implementation rather than prose-only claims:

- [`legal_chunking.py`](../evidence/lodestar/legal_chunking.py) — deterministic structure-aware chunking;
- [`embedding_provider.py`](../evidence/lodestar/embedding_provider.py) — embedding-provider contract and BGE query/passage behavior;
- [`hybrid_retrieval.py`](../evidence/lodestar/hybrid_retrieval.py) — four-lane hybrid retrieval, RRF and evidence hydration;
- [`rerank.py`](../evidence/lodestar/rerank.py) — deterministic authority-sensitive reranking;
- [`chunks_schema.sql`](../evidence/lodestar/chunks_schema.sql) — retrieval schema, FTS and HNSW vector index;
- [`grounding_eval.py`](../evidence/lodestar/grounding_eval.py) — retrieval-grounding gate;
- [`retrieval_integration_test.py`](../evidence/lodestar/retrieval_integration_test.py) — database-backed retrieval test against known expected sources;
- [`grounding-eval.md`](../evidence/lodestar/grounding-eval.md) — current measured retrieval result.

[Back to portfolio](../README.md) · [Evidence bundle](../evidence/lodestar/README.md)
