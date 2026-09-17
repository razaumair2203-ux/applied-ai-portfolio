# Lodestar — grounded RAG and evidence assessment

**Status:** working private system; selected non-sensitive implementation and evaluation evidence is published in this portfolio. The current build is **pre-production** and is not represented as a deployed public service.

## Engineering problem

Lodestar evaluates evidence against a legal corpus where retrieval quality, authority and traceability matter more than fluent text. The LLM is therefore downstream of a retrieval and evidence plane rather than being treated as the source of truth.

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
- automated backend, DB integration and browser tests.

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

The implemented hybrid search does more than combine two result lists. It runs lexical and semantic lanes plus separate high-authority candidate lanes, fuses ranks using RRF, hydrates the resulting IDs into citable evidence objects and then applies an explainable authority-sensitive reranker. The authority weighting is intentionally a near-tie adjustment rather than a rule that can bury a highly relevant lower-authority source.

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

The 2.9% figure is a **retrieval-grounding metric**: for each hand-checked query, the evaluation asks whether an accepted authority/citation marker appears within the top five results. It is not an LLM-answer accuracy figure and it is not a legal-correctness claim.

## Reliability and failure handling already implemented

The working code contains practical hardening that is easy to lose in a high-level RAG diagram:

- pooled PostgreSQL connections rather than repeated remote handshakes;
- batch evidence inserts;
- explicit `pgvector` casting on ANN queries;
- UUID validation before SQL execution;
- lazy embedding-model loading, startup warm-up and a lock around initialization;
- lexical-only fallback while a corpus is not yet embedded;
- separation of retrieval evaluation from LLM output quality;
- citation-resolution checks so an assessment cannot preserve a citation that was not actually retrieved;
- audit logging, real candidate-data deletion paths and an authentication scaffold.

## What is still open before production deployment

The private roadmap deliberately blocks deployment until further work and explicit sign-off. Current open items include:

- CI wiring for the complete test/evaluation gate;
- larger frozen retrieval and downstream answer-evaluation sets;
- storage encryption / signed-URL hardening;
- least-privilege database roles;
- production observability and latency percentile monitoring;
- explicit production deployment sign-off.

That boundary is important: the project demonstrates substantial implementation, evaluation and hardening, but it should not be confused with enterprise production ownership that has not yet occurred.

## Inspectable implementation evidence

The public evidence bundle exposes representative, sanitized implementation rather than a prose-only claim:

- [`legal_chunking.py`](../evidence/lodestar/legal_chunking.py) — deterministic structure-aware chunking;
- [`embedding_provider.py`](../evidence/lodestar/embedding_provider.py) — embedding-provider contract and BGE query/passage behavior;
- [`hybrid_retrieval.py`](../evidence/lodestar/hybrid_retrieval.py) — four-lane hybrid retrieval, RRF and evidence hydration;
- [`rerank.py`](../evidence/lodestar/rerank.py) — deterministic authority-sensitive reranking;
- [`chunks_schema.sql`](../evidence/lodestar/chunks_schema.sql) — retrieval schema, FTS and HNSW vector index;
- [`grounding_eval.py`](../evidence/lodestar/grounding_eval.py) — retrieval-grounding gate;
- [`retrieval_integration_test.py`](../evidence/lodestar/retrieval_integration_test.py) — database-backed retrieval test against known expected sources;
- [`grounding-eval.md`](../evidence/lodestar/grounding-eval.md) — current measured retrieval result.

[Back to portfolio](../README.md) · [Evidence bundle](../evidence/lodestar/README.md)
