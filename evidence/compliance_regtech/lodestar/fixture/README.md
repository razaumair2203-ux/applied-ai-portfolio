# Lodestar PostgreSQL + pgvector public fixture

This fixture closes the gap between the zero-dependency Lodestar logic checks and the real database-backed retrieval path.

## What it exercises

The test imports the portfolio's published [`hybrid_retrieval.py`](../hybrid_retrieval.py) directly and executes:

- PostgreSQL generated full-text vectors and `websearch_to_tsquery`;
- pgvector cosine ordering on **1024-dimensional** vectors;
- visa-class and criterion-tag array filters;
- ordinary lexical/vector candidate lanes;
- high-authority lexical/vector candidate lanes;
- Reciprocal Rank Fusion;
- database hydration into citable retrieval objects;
- authority-weighted reranking;
- non-precedent source labeling.

The only substituted component is the heavyweight sentence-transformer model. The fixture provider deterministically maps three test queries to 1024-dimensional vectors so CI can test the database/retrieval engineering without downloading a multi-GB ML stack.

## Run locally

Start the same pgvector image family used by Lodestar development:

```bash
docker run --rm --name lodestar-fixture \
  -e POSTGRES_USER=eb -e POSTGRES_PASSWORD=eb -e POSTGRES_DB=eb \
  -p 5432:5432 -d pgvector/pgvector:pg16
```

Install the small test dependency and run:

```bash
pip install -r evidence/compliance_regtech/lodestar/fixture/requirements.txt
LODESTAR_FIXTURE_DSN=postgresql://eb:eb@localhost:5432/eb \
  python -m evidence.compliance_regtech.lodestar.fixture.postgres_fixture_test
```

GitHub Actions runs the same test against a `pgvector/pgvector:pg16` service container.

## Boundary

This is a non-sensitive miniature corpus. It proves that the published retrieval implementation executes end to end against real PostgreSQL/pgvector; it does **not** reproduce the private 209-document corpus or upgrade the recorded 1/34 full-corpus result into a public measurement.


## Authority-weighting ablation

Authority enters twice: once through dedicated high-authority lexical/vector lanes and again through the final reranking multiplier. The public ablation characterizes both stages explicitly.

Run:

```bash
python -m evidence.compliance_regtech.lodestar.fixture.authority_ablation
```

The fixture compares ordinary two-lane RRF, four-lane RRF, and four-lane RRF plus the final authority multiplier. CI asserts that the high-authority lanes increase the controlling-source score advantage and that the reranker increases it again.

This is a **mechanistic ablation**, not evidence that the policy improves retrieval quality on the private 209-document corpus. It proves how strong the policy is and prevents the portfolio from describing it as merely a near-tie tiebreaker.
