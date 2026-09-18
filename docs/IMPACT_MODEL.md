# Impact model for this portfolio

This portfolio uses **engineering impact**, not generic startup or marketing impact, as the primary standard.

For applied AI in aerospace, autonomy and high-integrity workflows, a credible project creates value when it reduces uncertainty about whether a system can be trusted, integrated, deployed or advanced to the next engineering gate.

## What counts as impact here

1. **Operational relevance** — the work reaches real sensors, hardware, interfaces, users or field conditions rather than stopping at an offline notebook.
2. **Technical risk retired** — an experiment or test changes what the team believes about generalisation, latency, grounding, integration or failure modes.
3. **Decision quality improved** — evidence makes a model, architecture, split strategy, interface or release decision more defensible.
4. **Reusable engineering asset created** — dataset, evaluation harness, public code, protocol, test fixture, infrastructure or governed workflow can be reused.
5. **Assurance improved** — unsupported output, data leakage, provenance loss, silent model authority or integration ambiguity is made visible and controlled.
6. **System maturity advanced** — a project moves from model → deployment → integrated subsystem → measured end-to-end capability, with each stage distinguished honestly.
7. **External verification exists where possible** — public dataset, DOI, public repository, runnable fixture or CI-backed evidence reduces dependence on self-report.

## What does not count by itself

- a high model score without a defensible split or failure analysis;
- a demo screenshot without traceable implementation or evidence;
- a large technology list;
- leadership language without a clear personal contribution;
- “production”, “safety”, “autonomous” or “operational” wording that exceeds demonstrated maturity;
- revenue, adoption, safety-improvement or mission-effectiveness claims without attributable measurements.

## Impact ledger

| Work | Technical uncertainty / problem | Evidence-backed impact | Not claimed |
|---|---|---|---|
| **TIR-FOD** | Whether strong detector results survive source dependence and realistic partitioning | Contamination testing exposed an invalid **+8.52 ± 0.19 pp** uplift; acquisition-block-disjoint evaluation reduced mAP@[.50:.95] from **0.8223 ± 0.0070** to **0.7410 ± 0.0423** on the shared experiment. This changed the interpretation of “good” detector performance and made source lineage an evaluation control. Public dataset, split manifest and 29-run recomputation preserve that learning. | No claim that the detector by itself improves runway safety, eliminates FOD events or is a certified operational system. |
| **Jetson / Clear Run perception** | Whether the detector can run inside the aerial inspection chain rather than only on a workstation | TensorRT inference was flight-tested on Jetson Orin Nano; historical evidence showed a material detector-vs-end-to-end throughput gap, making camera/pipeline overhead an explicit system concern. The active Clear Run runtime integrates dual RGB/IR inference, geolocation, telemetry and GCS handling. | Historical 25.0/15.6 FPS summaries are not raw-log-reproducible; final GCS→UGV physical hand-off and verified retention are not complete claims. |
| **Lodestar** | How to keep retrieval authority, citations and evidence state from being hidden by fluent LLM output | Source structure, hybrid retrieval, authority policy, evidence hydration and output grounding are explicit software layers. A frozen 34-query retrieval regression set recorded **1/34 top-5 expected-source misses** on the private corpus; public PostgreSQL/pgvector and adversarial output-contract fixtures make key mechanisms executable. | No claim of universal RAG quality, semantic legal correctness, production adoption or independent reproduction of the private 209-document corpus result. |
| **Codex Adversarial Review Lite** | Whether an AI coding agent should be trusted to review its own work | Separates builder and reviewer roles, freezes audit scope, checks mutation state and requires a human decision before fixes are accepted. | No claim that a second model guarantees correctness. |
| **JobLooper** | How to use AI assistance without allowing generated prose to become factual authority | Keeps candidate truth, provenance, workflow state, deterministic gates, approval and release hashes outside the model. | No hiring prediction, ATS probability or autonomous application claim. |
| **ATLAS** | How to make AI/research compute repeatable for a multi-project engineering environment | Provides shared GPU/HPC execution, containers, workload management, guidance and controlled technical support for current research. | Not presented as hyperscale cloud/platform engineering. |

## Why this matters to an AI hiring reviewer

The recurring pattern is **model + evidence + system**:

- data provenance is treated as part of model validity;
- deployment throughput is separated from model-only throughput;
- retrieval is evaluated separately from generated prose;
- model authority is constrained by deterministic evidence and release rules;
- incomplete integration is presented as the next gate, not rewritten as a completed outcome.

That is the intended career signal: applied AI engineering that can operate inside multidisciplinary systems where incorrect confidence is itself an engineering risk.

[Back to portfolio](../README.md)
