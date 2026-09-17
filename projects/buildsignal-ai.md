# BuildSignal AI — validated AI/editorial product workflow

**Source repository:** private product repository; public-safe architecture only.

BuildSignal AI is a **Next.js / TypeScript / MDX** publishing and research platform for AI, SaaS and technical content. The point of including it here is not that a blog is an AI project; it is that the product uses explicit validation and workflow controls around AI-assisted research/editorial work.

## Implemented product surface

- Next.js 16 / React 19 / TypeScript 6;
- MDX content pipeline;
- local admin workspaces for Articles, Media, Video, Audio, YouTube, Social, Research, Comments, QA, Tools and Publish;
- article approval boundary before publishing;
- environment-secret separation;
- platform, editorial, media-pipeline and operations validators;
- style checking, lint, strict type checking and production build validation;
- layout inspection tooling;
- an AI-judge-loop simulation path for evaluating AI-assisted review behavior.

## Validation commands in the working repo

```text
npm run validate:platforms
npm run validate:editorial
npm run validate:pipeline
npm run validate:ops
npm run check:style -- --article=<slug>
npm run lint
npm run typecheck
npm run build
```

## Why it is relevant

It demonstrates product engineering around AI-assisted work: content/data pipelines, validation, QA, human approval and maintainable web tooling. I do not present it as an ML-model training project; its value is the controlled application layer around AI-enabled research/editorial workflows.

[Back to portfolio](../README.md)
