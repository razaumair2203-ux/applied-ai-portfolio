# BuildSignal — product / publishing workflow engineering

**Status:** private working repository; included as secondary software/product evidence, **not as a core AI/ML project**.

BuildSignal is a Next.js, TypeScript and MDX editorial platform for technical content. Its relevance to this portfolio is conventional product engineering around structured workflows, validation and publishing—not model training or RAG.

## Implemented product surface

- Next.js / TypeScript / MDX application;
- local administrative workspaces for articles, media, video, audio, YouTube, social, research, comments, QA, tools and publishing;
- explicit approval before content publication;
- environment-secret separation through local configuration;
- platform, editorial and pipeline validation commands;
- linting, type checking and build validation.

Representative validation commands in the working repository include:

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

## Portfolio boundary

BuildSignal demonstrates web/product workflow engineering. It is deliberately separated from the portfolio's direct AI evidence—Lodestar, TIR-FOD, Codex Adversarial Review Lite and JobLooper—so ordinary software features are not inflated into AI credentials.

[Back to project inventory](README.md) · [Back to portfolio](../README.md)
