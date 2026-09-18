# i-MSHA — U.S. mine-safety intelligence and MSHA decision platform

<p align="center">
  <img src="../visuals/msha/logo-wordmark.svg" alt="i-MSHA project wordmark" width="34%">
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
| Performance engineering | site-wide latency audit covered **152 surfaces**; query-batching work cut cumulative recorded cold/warm latency materially |
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

## Product surface

![i-MSHA dashboard regression snapshot](../visuals/msha/dashboard-regression.png)

*Authentic browser-regression snapshot from the project repository. It is shown as product/UI evidence, not as a production-deployment claim.*

## Canary AI — AI as an interface to governed data

Canary is designed to sit **across** the product rather than replace the underlying data model. The current implementation uses context-first routing, intent classification, feature-location knowledge, adversarial/golden-path tests and deterministic handlers so questions such as S&S rate, POV proximity, controller identity, legal outcomes or feature navigation resolve against the relevant product data path.

The engineering boundary matters: **the LLM is not the regulatory database**. Public MSHA records, typed transformations and deterministic feature logic remain the source of truth; AI is used to help a user reach, interpret and navigate that evidence.

## My role

**Product/programme direction, systems architecture, AI/data workflow definition, technical review, feature prioritisation and validation framing** across the product. The work spans market/problem definition, full-stack architecture, data and AI design, quality gates, performance/security review and pre-deployment readiness rather than a single model or feature.

## Boundary

The product remains under active development and its own status record still lists deployment work as pending. This case does not claim completed customer UAT, production hosting, regulatory certification or replacement for professional/legal judgment.

[Back to portfolio](../README.md) · [Project inventory](README.md)
