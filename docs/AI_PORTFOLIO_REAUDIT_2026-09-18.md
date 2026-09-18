# AI Portfolio Independent Re-Audit — 2026-09-18

This re-audit intentionally does **not** inherit the portfolio's previous 88/100 self-score. It evaluates the current public repository as a cold reviewer would: what is visible, technically defensible and independently checkable.

## Inspection contract

The portfolio is judged against the signals repeatedly visible in current applied-AI / ML-engineering roles:

1. **Problem and role signal** — can a recruiter identify the target profile in under 60 seconds?
2. **Hands-on ownership** — are personal architecture, implementation, experimentation and leadership contributions separated from team work?
3. **Model/data depth** — dataset design, training choices, model behavior and experiment design are visible.
4. **Evaluation rigor** — metrics have denominators, baselines, splits, failure analysis and bounded interpretation.
5. **Production software engineering** — code quality, tests, interfaces, reliability and failure handling are visible.
6. **Deployment / systems depth** — hardware, inference runtime, latency, telemetry, physical interfaces and real-world constraints are concrete.
7. **Reproducibility** — a reviewer can run meaningful public checks rather than only read claims.
8. **MLOps / operational maturity** — CI, repeatable configuration, dependency/environment contracts, observability and regression gates are visible.
9. **Impact** — technical work is connected to a real engineering or product outcome.
10. **Evidence integrity** — private measurements, public proof, team ownership and unfinished capability are clearly separated.
11. **Communication / first-screen conversion** — the strongest evidence is easy to find without reading every file.
12. **External verification** — papers, datasets and public projects can be independently checked.

Reference role signals sampled during this audit:
- OpenAI — Machine Learning Engineer, Multimodal Perception and Authentication: https://openai.com/careers/machine-learning-engineer-multimodal-perception-and-authentication-san-francisco/
- OpenAI — Machine Learning Engineer, API Multicloud: https://openai.com/careers/machine-learning-engineer-api-multicloud-san-francisco/
- NVIDIA — Senior Software Engineer, Metropolis Vision AI: https://jobs.nvidia.com/careers/job/893396230233

These are examples, not a claim that every AI recruiter uses an identical rubric.

## Independent baseline score on current `main`

| Dimension | Weight | Score | Critical assessment |
|---|---:|---:|---|
| Truth / evidence integrity | 15 | **14** | Strong evidence boundaries; private vs public claims are unusually explicit. |
| 60-second role signal | 10 | **9** | Aerospace AI / edge-autonomy positioning is immediate and differentiated. |
| Ownership clarity | 8 | **7** | Team boundaries are good, but personal hands-on AI contribution was not prominent enough on the landing page. |
| AI/ML technical depth | 12 | **10** | Strong retrieval, CV, edge inference and evaluation depth; public training implementation is still thin. |
| Evaluation / data rigor | 10 | **8** | TIR-FOD leakage/generalisation work is strong; Lodestar's 34-query result was presented with more statistical-looking precision than the sample supports. |
| Reproducibility / runnability | 12 | **7** | Lodestar pure logic is runnable; full retrieval, training and field-performance measurements are not publicly reproducible. |
| Production / deployment depth | 10 | **9** | One of the strongest dimensions: Jetson/TensorRT, telemetry, cameras, GCS and field trials are concrete. |
| Software / MLOps engineering | 7 | **5** | CI exists, but it originally covered only a narrow subset of published evidence and no full public ML stack. |
| Impact / system outcome | 5 | **4** | Strong engineering outcomes; final Clear Run detection-to-retention mission KPI is still open. |
| Visual / demo proof | 5 | **5** | Authentic visual evidence materially improves credibility. |
| Repository hygiene | 3 | **2** | Good structure, but repository metadata is weak (generic description, no topics, no license) and recent history is staging-heavy. |
| External verification | 3 | **2** | DOI/dataset/public-project links exist, but not every private-system headline claim has an external record. |
| **Total** | **100** | **82** | **Strong and differentiated, but still more inspectable than reproducible.** |

## Findings and treatment

### R01 — S1 — Lodestar 2.9% wording implied more statistical confidence than warranted
The value is exactly **1 miss in a frozen 34-query set**. Calling it only a "2.9% grounding error" can sound like a population-level model-quality estimate.

**Treatment:** changed recruiter-facing wording to **1/34 top-5 expected-source misses (2.9%)** and explicitly labelled the set a targeted regression/evidence-retrieval check.

### R02 — S1/S2 — Authority enters Lodestar retrieval twice
High-authority lexical/vector lanes contribute extra Reciprocal Rank Fusion score, and the final reranker applies a second authority multiplier. The previous prose made this sound like only a small final preference.

**Treatment:** documentation now describes the actual two-stage authority policy and identifies ablation against a two-lane baseline as the correct next validation step.

### R03 — S2 — Personal hands-on contribution was not visible early enough
The portfolio correctly bounded team authorship, but a cold reviewer could still ask: "What did Umair personally implement versus lead?"

**Treatment:** added an up-front contribution statement distinguishing Lodestar hands-on architecture/AI-assisted implementation from TIR-FOD experiment/deployment leadership and team-developed Clear Run systems integration.

### R04 — S1/S2 — CI did not cover enough of the published evidence surface
The original workflow compiled four Lodestar files and ran one pure-logic smoke test. A syntax break in other published Python evidence could pass unnoticed.

**Treatment:** CI now compiles all published Python evidence and runs repository-wide checks for Markdown links, JSON validity, frozen evaluation-contract consistency and key evidence-boundary assertions.

### R05 — S2 — Public model-training reproducibility remains thin — **RESOLVED**
TIR-FOD previously showed strong reported methodology and result evidence without an executable public aggregate-verification path.

**Resolution:** published a sanitized current-revision reproducibility bundle containing 29 seed-level scalar run records, the exact training/evaluation contract, the current acquisition-block split manifest, the recorded relevant environment, a GPU training harness and a zero-dependency recomputation script. CI now recomputes the manuscript headline means/SDs and seed-paired effects and validates the training contract in dry-run mode. Full 29-run GPU retraining is deliberately not performed in portfolio CI.

### R06 — S2 — Full Lodestar retrieval remains non-reproducible publicly — **RESOLVED**
A senior RAG reviewer previously could inspect the SQL but could not execute the published hybrid path against a public database fixture.

**Resolution:** added a non-sensitive PostgreSQL + pgvector fixture using the same `pgvector/pgvector:pg16` database family as the authoritative development setup. CI now executes the published hybrid retrieval implementation end to end across PostgreSQL FTS, 1024-dimensional pgvector ordering, metadata filters, four candidate lanes, RRF, hydration, authority reranking and non-precedent labeling. Only the heavyweight embedding model is substituted by deterministic fixture query vectors; the private 209-document corpus remains correctly bounded as private.

### R07 — S2 — Clear Run performance evidence needs machine-readable recomputation — **RESOLVED BY EVIDENCE DOWNGRADE**
The initial remediation assumed a sanitized raw run-log extract could be published. Inspection of the authoritative flight/reviewer archive showed that the historical ten-run logs and deployed TensorRT engine were **not retained**. Creating a reconstructed CSV from means/ranges would fabricate evidence.

**Resolution:** corrected the portfolio rather than manufacturing data. The 25.0 FPS TensorRT-stage and 15.6 FPS end-to-end values are now explicitly labelled **author-confirmed ten-run historical summaries**; the retained 25.12/15.07 runtime display is distinguished from those means; historical checkpoint identity is marked unavailable; the power wording is corrected so the 16–18 W range is not mislabelled as compute-and-camera-only power; and a machine-readable evidence-status file enforces these boundaries. A separate named-checkpoint measurement protocol is published for future/returned reproducible Jetson evidence, with engine/checkpoint hashes, repeated runs, CUDA-synchronized per-frame timing, separate telemetry and refusal gates.

### R08 — S2 — Answer-level RAG evaluation is missing — **RESOLVED AT THE REAL PRODUCT OUTPUT CONTRACT**
Inspection of the authoritative Lodestar implementation showed that the downstream surface is not a generic free-form QA chatbot; it is a structured per-criterion evidence assessment with a five-state schema and hard grounding gates.

**Resolution:** published a 10-case adversarial evaluation derived from the real assessment invariants. CI now verifies post-gate citation validity, hallucinated/ambiguous citation dropping, unambiguous prefix recovery, refusal when grounding disappears, preservation of `not_applicable` where appropriate, filtering of invented evidence IDs, five-state enforcement, and removal of unauthorized numeric approval/score fields. The portfolio explicitly does **not** convert this into a claim of semantic legal correctness; that remains a human/domain evaluation problem.

### R09 — S3 — Repository metadata under-sells the work
The GitHub repository description is only "Applied Ai portfolio", topics are empty, and there is no repository license. These do not weaken the engineering itself, but they reduce discoverability and polish.

**Status:** open; repository-level metadata must be changed through GitHub settings/API outside the file-content workflow.

## Score after this remediation branch

| Dimension | Score |
|---|---:|
| Truth / evidence integrity | **14 / 15** |
| 60-second role signal | **9 / 10** |
| Ownership clarity | **8 / 8** |
| AI/ML technical depth | **10 / 12** |
| Evaluation / data rigor | **8 / 10** |
| Reproducibility / runnability | **8 / 12** |
| Production / deployment depth | **9 / 10** |
| Software / MLOps engineering | **6 / 7** |
| Impact / system outcome | **4 / 5** |
| Visual / demo proof | **5 / 5** |
| Repository hygiene | **2 / 3** |
| External verification | **2 / 3** |
| **Total** | **85 / 100** |

## Highest-value next work

1. Publish a tiny Lodestar Postgres/pgvector fixture and end-to-end retrieval test.
2. Publish a TIR-FOD experiment-config / partition-manifest excerpt plus an aggregate recomputation script.
3. Publish a sanitized Clear Run latency/FPS CSV and deterministic summary script.
4. Add answer-level RAG evaluation with citation faithfulness, unsupported-claim rate and failure examples.
5. Add environment/dependency contracts for any evidence intended to be runnable beyond the zero-dependency checks.
6. Improve GitHub repository description/topics/license through repository settings.

The portfolio is already differentiated for **applied AI + aerospace/autonomy + edge deployment**. The remaining gains come from converting high-quality private evidence into small, safe, independently executable public proof.
