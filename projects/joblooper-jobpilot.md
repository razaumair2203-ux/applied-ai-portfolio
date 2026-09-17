# JobLooper — deterministic assurance around AI-assisted document generation

**Public implementation:** [Pub-JobLooper](https://github.com/razaumair2203-ux/Pub-JobLooper)

JobLooper is useful evidence here because it demonstrates a design principle for applied AI: the model may help with interpretation or drafting, but **truth, provenance, workflow state and release gates remain deterministic software responsibilities**.

## What the public implementation actually is

The public application is a local-first **Python 3.10+** system built primarily on the standard library. It can operate without an AI provider and adds optional assistant integration rather than making the model a hard runtime dependency.

Its implemented workflow includes:

- exact job-description capture;
- preflight / requirement checks;
- structured evidence and career-anchor handling;
- deterministic generation and release gates;
- provenance and content hashes;
- stateful application records;
- local dashboard and CLI paths;
- document build / export controls;
- submission-state tracking;
- optional Codex/OpenAI App Server assistance.

## Why the architecture is relevant to AI systems

A common failure mode in AI-assisted generation is allowing fluent output to overwrite factual or workflow state. JobLooper instead keeps the model inside a bounded layer:

```text
source evidence + captured requirement
              ↓
deterministic application state
              ↓
optional AI assistance
              ↓
deterministic validation / release gates
              ↓
document build + hashes + submission record
```

The public repository therefore demonstrates **AI containment and assurance**, not a claim that every stage is AI-powered.

## What is deliberately not claimed

- no prediction of ATS ranking or hiring outcome;
- no claim that an LLM is authoritative for dates, metrics or ownership;
- no claim of a TypeScript/Node runtime for the public implementation;
- no claim of cross-provider review unless a particular private experimental branch is being discussed separately;
- no claim that optional AI integration replaces deterministic validation.

A related private experimental system, JobPilot Local, explores additional career-document workflows, but private features are not used here as proof of public implementation capability.

[Back to portfolio](../README.md)
