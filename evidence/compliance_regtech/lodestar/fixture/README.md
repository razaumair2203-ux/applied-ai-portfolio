# Lodestar PostgreSQL + pgvector test

## What this code shows

The published [hybrid retrieval code](../hybrid_retrieval.py) running end to end against a real PostgreSQL + pgvector database: full-text search, 1024-dimension vector search, metadata filters, high-authority lanes, Reciprocal Rank Fusion and reranking. A small fixed embedder stands in for the BGE model, so no large ML download is needed.

The authority ablation compares plain two-lane fusion, four-lane fusion and four-lane fusion with reranking, and shows how much each stage favours controlling sources.

## How to run

```bash
docker run --rm --name lodestar-fixture \
  -e POSTGRES_USER=eb -e POSTGRES_PASSWORD=eb -e POSTGRES_DB=eb \
  -p 5432:5432 -d pgvector/pgvector:pg16

pip install -r evidence/compliance_regtech/lodestar/fixture/requirements.txt
LODESTAR_FIXTURE_DSN=postgresql://eb:eb@localhost:5432/eb \
  python -m evidence.compliance_regtech.lodestar.fixture.postgres_fixture_test
python -m evidence.compliance_regtech.lodestar.fixture.authority_ablation
```

[Back to Lodestar code](../README.md) · [Back to portfolio](../../../../README.md)
