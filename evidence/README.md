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

Measured state recorded in the working private system: **209 source documents, 2,945 embedded chunks, 34 hand-checked retrieval queries, 1/34 top-5 expected-source misses (2.9%), 53 backend tests, 17/17 stress/abuse cases and 12/12 concurrent full flows.**

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

**Start here:** [`tir-fod/README.md`](tir-fod/README.md)

The public reproducibility slice now includes **29 sanitized seed-level run records**, the exact current training/evaluation protocol, the current 12-class acquisition-block split manifest, the recorded relevant environment, a GPU training harness and a zero-dependency recomputation script. Run:

```bash
python evidence/tir-fod/reproducibility/recompute_results.py
```

That public check independently recomputes the multi-seed means/SDs and paired contamination/generalisation effects used by the current revision. Full GPU retraining still requires the public dataset, frozen split files, pretrained weights and compatible ML hardware/software.

The older [single-run benchmark snapshot](tir-fod/benchmark_results.json) is retained for historical traceability. Historical Jetson flight performance is separately documented in the [deployment evidence boundary](tir-fod/deployment/README.md), which records the author-confirmed ten-run summaries while explicitly stating that the raw per-run logs and historical engine were not retained. The public dataset record is linked from the [TIR-FOD / Clear Run case study](../projects/tir-fod-clear-run.md).

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
