# GE Aerospace — AI Lead Developer (Warsaw) requirement → evidence map

This page maps the role to **inspectable evidence**. It is not a keyword mirror. Where evidence is partial, it is labelled partial.

## Role fit in one line

**Operational aerospace engineer + current applied-AI/R&D lead + hands-on RAG, computer vision, edge deployment and GenAI product engineering.**

## Requirement map

| GE requirement | Evidence | Strength |
|---|---|---|
| Develop AI / ML solutions for engineering and business use cases | TIR-FOD / Clear Run; Lodestar; JobLooper/JobPilot; current 100+ R&D portfolio | **Direct** |
| Python + AI/ML frameworks | YOLO benchmarking/deployment; Lodestar Python retrieval stack; FastAPI; BGE embeddings | **Direct** |
| Machine learning / computer vision | 3,499-frame LWIR dataset, 29 YOLO runs, edge deployment; two AI/CV IEEE papers | **Direct** |
| NLP / GenAI applications | Lodestar grounded LLM assessment; Codex AR-L; JobPilot cross-provider generation/review | **Direct** |
| RAG applications | Structure-aware chunking → BGE embeddings → pgvector + FTS → RRF → reranking → citable evidence | **Direct** |
| Embeddings / vector databases / semantic search | BGE; 2,945 embedded chunks; `pgvector`; HNSW cosine; hybrid lexical/semantic search | **Direct** |
| Prompt-driven / chat / model integrations | Codex AR-L builder/reviewer workflow; JobPilot Claude/Codex adapters; Lodestar grounded assessment | **Direct** |
| APIs and integration | FastAPI in Lodestar; loopback/browser-extension architecture in JobPilot; product integration work | **Direct / transferable** |
| Experimentation / prototyping / validation | 29 YOLO runs, repeat seeds, leakage study, acquisition-block generalisation, field deployment; current R&D role | **Direct** |
| Production support / troubleshooting | Lodestar connection-pool/batching/embedder hardening; 53 tests, 17/17 stress, 12/12 concurrent flows; aerospace operational background | **Direct + operational depth** |
| Testing / evaluation / monitoring | Retrieval grounding evaluation; stress/E2E/concurrency tests; TIR-FOD benchmark discipline; adversarial review workflow | **Direct** |
| Multimodal AI / document intelligence | RGB/LWIR research; Lodestar document/retrieval pipeline | **Direct** |
| Responsible AI / secure implementation | provenance, citation grounding, fail-closed validation, privacy boundaries, human approval controls | **Direct** |
| Agile delivery | PMI-ACP; applied R&D delivery; iterative prototype/validation cycles | **Direct** |
| Mentor / lead technical tasks | Leads applied R&D portfolio and engineering teams; technical direction across AI/autonomy projects | **Direct** |
| Cloud platforms (Azure/AWS/GCP) | No strong production-cloud evidence published here | **Partial / gap** |
| MLOps / LLMOps | versioned code/tests/evaluation/deployment controls and model-provider abstraction; no claim of mature enterprise Kubeflow/MLflow-style platform ownership | **Transferable / partial** |

## Proof path for a technical reviewer

1. **RAG / retrieval:** [Lodestar](projects/lodestar.md) → [sanitized code](evidence/lodestar/README.md) → [grounding evaluation](evidence/lodestar/grounding-eval.md)
2. **ML / edge AI:** [TIR-FOD / Clear Run](projects/tir-fod-clear-run.md) → [public dataset DOI](https://doi.org/10.5281/zenodo.22546586)
3. **GenAI engineering:** [Codex AR-L](projects/codex-adversarial-review-lite.md) → [public repository](https://github.com/razaumair2203-ux/codex-adversarial-review-lite)
4. **Governed AI product:** [JobLooper / JobPilot](projects/joblooper-jobpilot.md) → [public JobLooper code](https://github.com/razaumair2203-ux/Pub-JobLooper)
5. **Research depth:** [publications + dataset](research/README.md)

## Aerospace context that changes the profile

The role is inside GE Aerospace, not a generic AI startup. My earlier 18+ years cover aircraft systems integration, international OEM development, verification/validation, fleet engineering, maintenance/sustainment and programme management. That gives the current AI work a domain layer: requirements, interfaces, failure modes, deployment constraints, safety/reliability thinking and operational users are familiar engineering problems rather than abstractions.

I do **not** claim 18 years as an AI developer. The evidence above shows the current applied-AI work directly; the aerospace career explains the environments in which I know how to deploy engineering solutions.

[Back to portfolio](README.md)
