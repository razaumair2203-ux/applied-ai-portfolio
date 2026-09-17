# AI Portfolio Inspection Contract

**Audit date:** 2026-09-18  
**Audit target:** a cold AI/ML recruiter, applied-AI hiring manager, senior ML engineer, or aerospace/autonomy technical reviewer.

This is a technical-evidence audit, not a résumé-style polish review. The portfolio passes only when a first-time reviewer can understand the role signal quickly, inspect the strongest evidence, distinguish personal ownership from team work, and tell which claims are public/reproducible versus measured in private programme systems.

## 1. Hard-stop integrity rules

Any one of these is a release blocker:

1. A metric, deployment claim, publication status, role, or technology is stated more strongly than the evidence supports.
2. Generated or reconstructed media is presented as real project evidence.
3. Team-developed work is presented as sole authorship.
4. A future/proposed capability is described as already demonstrated.
5. A public evidence bundle is described as runnable/reproducible when its published files are internally inconsistent.
6. Private programme/product evidence is described as independently reproducible from the public repository when it is not.

## 2. Evidence grades

| Grade | Meaning | Suitable wording |
|---|---|---|
| **A — reproducible public proof** | Public code/data/test can be run or independently checked | “public check”, “reproduced by…” |
| **B — inspectable public proof** | Representative source, visual, log or result artefact is public, but the full system is not | “sanitized implementation”, “inspectable evidence” |
| **C — external public record** | DOI, dataset record, publication or other independent record | “published/released at…” |
| **D — bounded private/team-system evidence** | Real measurement/source exists but cannot be fully published | “recorded programme measurement”, “private-system result” |

A recruiter should not have to reverse-engineer which category a headline number belongs to.

## 3. Scoring contract

| Dimension | Weight | Pass condition |
|---|---:|---|
| Truth / evidence integrity | 15 | Claims are evidence-bounded and technically consistent |
| 60-second role signal | 10 | Aerospace/applied-AI/edge-autonomy positioning is immediately clear |
| Ownership clarity | 8 | “Led/integrated/reviewed” vs “implemented” is unambiguous |
| AI/ML technical depth | 12 | Data, model, retrieval, inference, deployment and engineering decisions are visible |
| Evaluation / data rigor | 10 | Splits, leakage, metrics, limitations and test protocol are credible |
| Reproducibility / runnability | 12 | At least one meaningful public technical path can be executed/checkable |
| Production / deployment depth | 10 | Runtime, hardware, interfaces, constraints and field behavior are concrete |
| Software / MLOps engineering | 7 | Tests, CI/repeatable checks, dependencies, configuration and reliability are visible |
| Impact / system outcome | 5 | Work connects to an engineering outcome, not just a model score |
| Visual / demo proof | 5 | Authentic visuals/demo evidence rapidly establish reality |
| Repository hygiene | 3 | No target-JD files, staging payloads, unexplained clutter or obvious dead evidence |
| External verification | 3 | Publications/datasets/releases link to independent records where available |

**Total: 100**

Interpretation:
- **85–100:** recruiter-ready and technically persuasive.
- **70–84:** strong, but proof/reproducibility gaps can still cost a technical review.
- **55–69:** credible work but too trust-dependent.
- **<55:** presentation materially weakens credibility.

## 4. Severity

- **S0 — integrity blocker**
- **S1 — technical credibility blocker**
- **S2 — conversion blocker**
- **S3 — polish**

## 5. Baseline observations on current `main`

### F01 — S1 — Lodestar public retrieval bundle is internally inconsistent
`grounding_eval.py` calls `hybrid_search(..., visa_class=...)`, while the published `hybrid_retrieval.py` exposes no `visa_class` argument or filtering path. The authoritative private Lodestar implementation **does** support `visa_class` and `criterion_tags`, so the public extraction—not the underlying system—is wrong.

### F02 — S1 — No meaningful public reproduction path
The repo provides source excerpts and measured summaries but no zero-dependency smoke check, environment contract or CI workflow that lets a reviewer execute even the pure retrieval-control logic.

### F03 — S1 — Clear Run SAHI framework identifier is stale/wrong for the current unpinned API
The public excerpt uses `AutoDetectionModel.from_pretrained(model_type="yolov8", ...)`. Current SAHI/Ultralytics integration uses the `"ultralytics"` framework identifier. Either pin a historical dependency that accepts the old identifier or publish the current API form.

### F04 — S1 — Headline precision is stronger than public reproduction scope
Exact values—25.0 FPS, 15.6 FPS, 2.9% grounding error, 53 tests, 12/12 concurrent flows—are legitimate recorded results, but the landing page does not clearly distinguish private/team-system measurements from public reproducible checks.

### F05 — S2 — Authority reranking is described imprecisely
The public Lodestar prose calls authority a “near-tie preference,” but the published code applies a continuous multiplicative score adjustment. It behaves as a bounded nudge, not a literal tie-window mechanism.

### F06 — S1/S2 — GCS-to-UGV hand-off wording is stronger than the inspected programme source
The private Clear Run architecture record explicitly says the reviewed GCS dispatch route updates in-memory target/rover state and does **not** establish physical goal delivery to the rover. Public wording should keep the UAV/GCS integration strength while marking GCS→UGV physical hand-off as still under end-to-end validation.

### F07 — S2 — Root technical stack overstates recruiter-useful proof breadth
The landing page lists Supabase, ROS/ROS2 and Jetson Nano in the headline stack although the strongest reviewer-facing flagship evidence is PostgreSQL/FastAPI/RAG plus Jetson Orin Nano/MAVLink/TensorRT. The root stack should optimize for demonstrated depth, not keyword count.

### F08 — S2 — Flagships need explicit failures/trade-offs
The underlying work has unusually good material—dataset contamination inflation, acquisition-block generalisation drop, model-vs-system FPS gap, authority-lane design, private-corpus evaluation limits—but these are not surfaced as engineering judgment.

### F09 — PASS — Authentic visual evidence is strong
The latest `main` includes real Clear Run/TIR-FOD field evidence, a working Lodestar UI render and public-tool evidence composites with an explicit non-synthetic provenance policy. Preserve this.

### F10 — PASS — Ownership boundaries are strong
Clear Run correctly states team development and Umair’s systems/technical-leadership role rather than presenting all source as sole authorship.

### F11 — S2 — Reproducibility language needs sharper boundaries
The public portfolio should say exactly what a reviewer can run from this repository and what requires the private corpus/product/programme state.

### F12 — S3 — No CI/repeatable public evidence check
A lightweight CI job would materially improve software-engineering credibility without pretending the complete private systems are public.

## 6. Baseline score

**76 / 100 — strong work and strong visual reality, but the technical proof layer still asks the reviewer to trust too much.**

The largest remaining deficit is **public verification mechanics**, not AI breadth or project substance.

## 7. Remediation order

1. Correct public code inconsistencies and stale API usage.
2. Add one honest runnable public check + CI.
3. Label public proof versus private/team-system measurements.
4. Tighten integration boundaries and over-broad stack keywords.
5. Surface engineering failures, trade-offs and unresolved limits.
6. Add a claim-to-evidence matrix and re-score.
