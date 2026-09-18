# i-MSHA / MSHA Compliance SaaS — AI-enabled regulatory intelligence platform

<p align="center">
  <img src="../visuals/msha/logo-wordmark.svg" alt="i-MSHA project wordmark" width="34%">
</p>

i-MSHA is an active private product programme for Mine Safety and Health Administration (MSHA) compliance intelligence. It combines a structured public-data pipeline, risk/inspection workflows, regulatory analytics and a guarded AI assistant inside a full-stack SaaS architecture.

## Current implementation

| Layer | Current project state |
|---|---|
| Frontend | Next.js · TypeScript · Tailwind / component UI |
| Backend | FastAPI · Python |
| Data | PostgreSQL application state + DuckDB over typed Parquet analytics |
| Source pipeline | MSHA public-data ingestion, validation, typed Parquet analytics and scheduled refresh workflows |
| Product scope | mine intelligence, citations, inspections, incidents, health hazards, contractor safety, peer benchmarking, legal/enforcement views |
| AI | Canary assistant plus AI-supported analysis inside deterministic product workflows |
| Current maturity | private product in pre-deployment hardening; production deployment/UAT are not claimed |

The current source-of-truth status records **8 active modules, 25 frontend features and 100 backend handlers**. The application combines a versioned PostgreSQL application schema with DuckDB/Parquet analytics rather than treating model output as the regulatory data source.

## Product surface

![i-MSHA dashboard regression snapshot](../visuals/msha/dashboard-regression.png)

*Authentic browser-regression snapshot from the project repository. It is shown as product/UI evidence, not as a production-deployment claim.*

## AI and validation focus

The private project record includes a **Canary AI assistant** with context-first routing, adversarial/golden-path tests and deterministic feature-handler access to live product data, alongside conventional product validation and typed ingestion. The 20 May 2026 status records **385 Canary unit tests and 839 full backend tests passing**. The engineering emphasis is on combining AI assistance with traceable public data rather than allowing the model to become the source of regulatory truth.

## My role

Product/programme direction, systems architecture, AI/data workflow definition, technical review, feature prioritisation and validation framing across the full-stack build.

## Boundary

The product remains under active development and its own status record still lists deployment work as pending. This case does not claim completed UAT, production hosting, customer deployment or regulatory certification.

[Back to portfolio](../README.md) · [Project inventory](README.md)
