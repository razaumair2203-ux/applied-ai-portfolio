# Lodestar grounding evaluation

| Date | Hand-checked query / expected-citation pairs | Retrieval depth | Error rate | Corpus |
|---|---:|---:|---:|---:|
| 2026-07-10 | **34** | top-5 | **2.9%** | **209 docs / 2,945 chunks** |

For each query, the expected authority/citation is known in advance. Retrieval succeeds when an accepted source marker appears within the top-5 result set.

This measures **retrieval grounding**, not legal correctness, LLM answer quality, user success, or immigration outcome probability.

## Representative frozen pairs

| Query | Accepted source marker(s) |
|---|---|
| `lesser nationally or internationally recognized prizes or awards for excellence` | `(h)(3)(i)` / `(i)` |
| `membership in associations requiring outstanding achievements judged by experts` | `(h)(3)(ii)` / `(ii)` |
| `two step analysis count the criteria then final merits determination` | `Kazarian` / `F.2` |
| `proposed endeavor has substantial merit and national importance` | `Dhanasar` / `F.5` |
| `on balance beneficial to waive the job offer and labor certification requirements` | `Dhanasar` / `F.5` |

## Pipeline under test

```text
query
  -> BGE query embedding
  -> semantic pgvector retrieval
  -> PostgreSQL full-text retrieval
  -> high-authority semantic + lexical lanes
  -> Reciprocal Rank Fusion
  -> authority-aware reranking
  -> top-k citable chunks
```

## Additional test state

- **53** backend/Python tests green.
- **17 / 17** stress and abuse cases pass.
- **3 / 3** Playwright browser E2E flows pass.
- **12 / 12** concurrent full flows passed after connection-pool, batching, embedder warm-up/locking, UUID-validation and lexical-fallback hardening.

[Implementation evidence](README.md) · [Lodestar case study](../../projects/lodestar.md)
