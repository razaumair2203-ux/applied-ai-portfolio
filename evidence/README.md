# Technical evidence index

This directory is the shortest path for a technical reviewer who wants implementation and measured artefacts rather than portfolio prose.

## 1. Lodestar — RAG / retrieval implementation

**Start here:** [`lodestar/README.md`](lodestar/README.md)

Inspectable evidence includes:

- structure-aware chunking;
- BGE embedding-provider logic;
- PostgreSQL / `pgvector` retrieval schema;
- hybrid lexical + vector retrieval;
- Reciprocal Rank Fusion;
- deterministic authority-weighted reranking;
- hand-checked grounding pairs;
- retrieval evaluation code;
- representative DB-backed integration testing;
- a **zero-dependency public smoke check** for RRF, authority weighting, metadata filters, structure-aware chunking and the frozen evaluation specification.

Run from the repository root:

```bash
python -m evidence.lodestar.public_smoke_test
```

Measured state recorded in the working private system: **209 source documents, 2,945 embedded chunks, 34 hand-checked retrieval queries, 2.9% top-5 retrieval-grounding error, 53 backend tests, 17/17 stress/abuse cases and 12/12 concurrent full flows.**

## 2. Clear Run — edge-AI implementation extract

**Start here:** [`clear-run/README.md`](clear-run/README.md)

This public extract traces the deployment claims to working team-developed source without publishing the complete private programme repository. It documents:

- NVIDIA Jetson / GStreamer camera handling;
- Ultralytics YOLO and optional SAHI sliced inference;
- CUDA device execution;
- `.pt`, ONNX and TensorRT `.engine` model paths;
- normalized detection outputs;
- latency measurement and headless flight execution;
- the telemetry hand-off contract into the broader mission system.

[`clear-run/edge_detector_excerpt.py`](clear-run/edge_detector_excerpt.py) is a reduced, sanitized implementation extract. Ownership is explicitly bounded: Clear Run is team-developed; Umair's role is systems engineering/integration, technical direction, experiment/validation framing and team leadership rather than sole code authorship.

## 3. TIR-FOD — benchmark/result evidence

**Result snapshot:** [`tir-fod/benchmark_results.json`](tir-fod/benchmark_results.json)

The public portfolio summarizes the larger private research record: real-runway LWIR acquisition, 23 classes, 29 controlled training runs, repeated-seed testing, contamination/leakage analysis, acquisition-block generalisation and Jetson/TensorRT flight deployment.

The public dataset record is linked from the [TIR-FOD / Clear Run case study](../projects/tir-fod-clear-run.md).

## 4. Public source repositories

Some portfolio projects are already public in their own repositories and are therefore linked rather than duplicated:

- **Codex Adversarial Review Lite** — public builder/reviewer AI-assurance workflow: <https://github.com/razaumair2203-ux/codex-adversarial-review-lite>
- **JobLooper** — public evidence-governed AI-assisted workflow: <https://github.com/razaumair2203-ux/Pub-JobLooper>

## Publication policy for evidence

The portfolio publishes enough implementation and measurement to make technical claims inspectable without moving private programme, institutional or personal material into a public repository. Public case studies therefore distinguish between:

- **inspectable public implementation**;
- **measured results with a public/sanitized evidence extract**; and
- **team/programme systems whose detailed repositories remain private**.

Claims on the landing page are intended to trace to one of these evidence categories. For the recruiter-facing claim-by-claim mapping, see the **[headline evidence matrix](../docs/HEADLINE_EVIDENCE_MATRIX.md)**.

[Back to portfolio](../README.md)
