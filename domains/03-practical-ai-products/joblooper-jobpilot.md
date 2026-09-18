# JobLooper — evidence-governed job-application operating system

**Public implementation:** [Pub-JobLooper](https://github.com/razaumair2203-ux/Pub-JobLooper)

**Private development / evaluation lineage:** [Request technical review access →](https://github.com/razaumair2203-ux/applied-ai-portfolio/issues/new?template=access-joblooper-private.yml)

JobLooper is a local-first system for managing the **entire evidence-bearing job-application lifecycle**, not an AI CV generator. It starts with a candidate-approved record of career truth, captures the exact employer advert, exposes unresolved fit gaps before drafting, allows AI assistance only inside that governed context, requires complete human review, builds deterministic employer-facing documents, records the exact files submitted, and carries observed outcomes forward into later applications.

The design principle is simple but demanding: **truth, provenance, workflow state, release authority and observed outcomes are software responsibilities; the model may assist reasoning but does not own those states.**

<p align="center">
  <a href="https://github.com/razaumair2203-ux/Pub-JobLooper"><img src="../../visuals/practical-ai-products/joblooper/app-icon.svg" alt="Official JobLooper project mark" width="13%"></a>
</p>

[![JobLooper application workspace](../../visuals/practical-ai-products/joblooper/dashboard-surface.svg)](https://github.com/razaumair2203-ux/Pub-JobLooper)

*The official project mark comes from the public JobLooper project; the dashboard surface is rendered from the current public dashboard source.*

## End-to-end governed lifecycle

[![JobLooper governed workflow](../../visuals/practical-ai-products/joblooper/workflow.svg)](https://github.com/razaumair2203-ux/Pub-JobLooper)

The implemented lifecycle is:

**signed career truth → exact JD capture → JD confirmation → requirement/gap preflight → evidence-bounded drafting → complete document review → explicit approval → deterministic DOCX/PDF build → hash-bound submission record → employer response → outcome/lesson history**.

That architecture addresses a recurring failure mode in AI-assisted career tools: a chat can generate plausible text, but it usually does not know which facts are authorized, which advert was actually used, which file was finally submitted, or whether later “lessons” are evidence or speculation.

## Public implementation

The application is a local-first **Python 3.10+** system built primarily on the standard library. It can operate without an AI provider; optional Codex assistance is additive rather than a hard runtime dependency.

Implemented controls include:

- candidate-reviewed career truth represented as approved anchors with provenance;
- exact job-description capture rather than an inferred summary;
- deterministic requirement/preflight state and explicit proceed/stop decisions;
- AI assistance that cannot silently rewrite approved truth;
- complete CV/letter presentation before user sign-off;
- deterministic DOCX/PDF generation and text/package validation;
- content hashes, generation fingerprints and stale-input detection;
- exact submission receipts bound to the files actually sent;
- employer response and outcome records separated from inferred explanations;
- retained lessons only after evidence/counter-evidence review.

## Evaluation and release discipline

The wider private development record includes a frozen **20 train / 15 validation / 15 held-out** evaluation harness with fabrication/date/metric checks, parser rescoring, prompt-version comparison and release safeguards. One retained candidate optimization was **blocked** because its measured improvement was not statistically significant—an example of release governance overriding the assumption that a newer AI prompt must be better.

A public-safe aggregate is documented in **[Evaluation-Driven AI Workflow Engineering](../04-assurance-digital-engineering/ai-evaluation-workflows.md)**.

## Why this is an AI systems project

The central engineering problem is **model containment inside a traceable state machine**. AI can interpret a role and propose wording, but it cannot convert a hypothesis into candidate truth, claim unsupported experience, release a document, mutate submission state, or turn an employer outcome into a causal story without evidence.

Hiring predictions, synthetic ATS scores and unverified recruiter explanations remain outside the authority model.

[Back to domain index](README.md)
