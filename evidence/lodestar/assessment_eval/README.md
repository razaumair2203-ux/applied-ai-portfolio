# Lodestar structured-assessment output evaluation

Lodestar's downstream product surface is not a generic free-form RAG chatbot. It produces a **structured per-criterion evidence assessment** with one of five states, evidence references, citable authority and a rationale.

This public evaluation therefore tests the actual generation boundary instead of pretending a generic QA benchmark represents the product.

## Run

```bash
python -m evidence.lodestar.assessment_eval.run_eval
```

The frozen adversarial cases test:

- valid citations survive;
- invented citations are dropped;
- a model that cites only invented authority is forced onto the refusal path;
- a uniquely identifiable truncated chunk ID can be recovered;
- an ambiguous prefix is rejected;
- no retrieved authority means no asserted conclusion;
- `not_applicable` can survive the post-generation grounding gate where appropriate;
- invented evidence IDs are removed;
- unknown numeric authority fields such as `approval_probability` or `score` cannot survive canonicalization;
- statuses outside the five-state taxonomy are rejected.

## What the metric means

CI requires:

- **100% post-gate citation validity**;
- **100% post-gate evidence-ID validity**;
- **100% refusal-contract correctness** on the frozen adversarial cases;
- all expected state transitions to match the hand-checked fixture specification.

This is an **output-contract / grounding-safety evaluation**, not a claim of legal correctness, universal answer quality, or immigration-outcome prediction. Semantic correctness of a real provider's rationale still needs human/domain evaluation and is deliberately not converted into a fake automated score.

## Provenance

The guardrail behavior is a sanitized pure extraction of the private Lodestar assessment engine's invariants: allowed-citation enforcement, unambiguous prefix recovery, refusal when citations disappear, five-state output and valid evidence IDs. The cases are public software fixtures and contain no candidate data.
