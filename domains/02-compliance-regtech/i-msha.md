# i-MSHA — U.S. mine-safety intelligence and MSHA decision platform

**Private product; technical review available:** [Request review →](https://github.com/razaumair2203-ux/applied-ai-portfolio/issues/new?template=access-i-msha.yml)

**Public evidence snapshot:** 19 September 2026. Quantitative product/test counts cited below remain tied to the retained 20 May 2026 source-of-truth state where specified.

<p align="center">
  <a href="https://github.com/razaumair2203-ux/applied-ai-portfolio/issues/new?template=access-i-msha.yml"><img src="../../visuals/compliance-regtech/i-msha/logo-wordmark.svg" alt="i-MSHA project wordmark" width="34%"></a>
</p>

i-MSHA is an active full-stack product programme built around a difficult data problem in U.S. mining: **MSHA publishes extensive authoritative public data, but the operational picture is fragmented across datasets, entities, time periods and regulatory workflows**. i-MSHA consolidates that information into one national→state→mine/controller decision environment and then layers governed analytics and AI assistance on top of the source data.

It is therefore not just an “MSHA chatbot” or a dashboard wrapper. The system connects **mine/controller identity, violations, penalties, inspections, injury/safety, legal outcomes, occupational exposure, contractor history and acquisition due diligence** so a user can move from portfolio-level questions to a specific mine, enforcement issue or risk history without rebuilding the data relationship manually.

## System scale

| Dimension | Current project state |
|---|---|
| Product scale | **8 active modules · 25 frontend features · 100 backend handlers** |
| Analytical scope | national · state · mine/controller · peer/comparison · date/commodity filtering |
| Frontend | Next.js · TypeScript · component dashboard UI |
| Backend | FastAPI · Python |
| Data architecture | PostgreSQL application state + DuckDB over typed Parquet analytics |
| Source pipeline | scheduled MSHA public-data ingestion, validation, typed transformation and refresh workflows |
| AI layer | **Canary AI** across the product, with context-first routing and deterministic feature-handler access to live data |
| Validation | **385 Canary unit tests · 839 full backend tests passing** in the 20 May 2026 source-of-truth state |
| Performance engineering | **152 surfaces** audited; retained cumulative cold latency improved **100.1 s → 50.8 s (-49.3%)** and warm latency **66.8 s → 18.3 s (-72.6%)** after query-batching work |
| Current maturity | private product in pre-deployment hardening; production deployment/UAT are not claimed |

## What the platform consolidates

The active module set covers:

- **Mine & Controller Profiles** — mine search, controller/operator portfolio views and acquisition due diligence;
- **Violation Management** — compliance intelligence, regulation intelligence, good-faith eligibility and normalized violation rates;
- **Penalty & Assessment Tracking** — Pattern of Violations screening, penalty lifecycle, component breakdown, reduction advisory and mine-size monitoring;
- **Inspection Management** — outcomes, readiness, activity intelligence and district enforcement context;
- **Safety & Incidents** — integrated injury intelligence;
- **Legal Intelligence** — contest outcomes, judge tendencies and conference effectiveness;
- **Occupational Exposure** — respirable dust/silica, noise/hearing and chemical-exposure views;
- **Contractor Intelligence** — consolidated contractor safety/enforcement analysis.

Cross-cutting tools include **mine comparison, Weekly Pulse intelligence, export/download workflows, entity search, tier controls and drill-down navigation**.

## Product differentiation

The system-level differentiator is the **breadth of decisions supported by one governed data model**. Mine identity, enforcement history, inspections, penalties, legal outcomes, exposure, contractor performance and acquisition context are not isolated demos; they are traversable parts of the same product, with Canary providing a natural-language interface across those deterministic data paths. That product shape is more important than any single model or framework.

## Product surface

[![i-MSHA dashboard regression snapshot](../../visuals/compliance-regtech/i-msha/dashboard-regression.png)](https://github.com/razaumair2203-ux/applied-ai-portfolio/issues/new?template=access-i-msha.yml)

*Authentic browser-regression snapshot from the project repository. It is shown as product/UI evidence, not as a production-deployment claim.*

## Canary AI — AI as an interface to governed data

Canary is designed to sit **across** the product rather than replace the underlying data model. The current implementation uses context-first routing, intent classification, feature-location knowledge, adversarial/golden-path tests and deterministic handlers so questions such as S&S rate, POV proximity, controller identity, legal outcomes or feature navigation resolve against the relevant product data path.

The engineering boundary matters: **the LLM is not the regulatory database**. Public MSHA records, typed transformations and deterministic feature logic remain the source of truth; AI is used to help a user reach, interpret and navigate that evidence.

## Contribution boundary

- **Direct responsibility:** product/programme direction, systems architecture, AI/data workflow definition, feature prioritisation, technical review and validation framing.
- **Product-development scope:** the case represents the integrated product and its measured engineering state; individual feature implementation is not presented as sole manual coding.
- **Decision authority:** source data, deterministic analytics, validation and release gates remain outside unconstrained model output.

## Boundary

The product remains under active development and its own status record still lists deployment work as pending. This case does not claim completed customer UAT, production hosting, regulatory certification or replacement for professional/legal judgment.

[Back to portfolio](../../README.md) · [Domain index](README.md)
