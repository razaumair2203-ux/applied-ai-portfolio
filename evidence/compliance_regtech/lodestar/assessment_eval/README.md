# Lodestar output checks

## What this code shows

Lodestar returns a structured per-criterion assessment: one of five states, evidence references and cited authority. These 10 adversarial cases check that:

- valid citations survive and invented ones are dropped;
- an answer citing only invented authority is forced to refuse;
- no retrieved authority means no conclusion;
- invented evidence IDs are removed;
- score or probability fields are stripped;
- states outside the five-state set are rejected.

Pass criteria: **100%** citation validity, evidence-ID validity and refusal correctness on all cases.

## How to run

```bash
python -m evidence.compliance_regtech.lodestar.assessment_eval.run_eval
```

[Back to Lodestar code](../README.md) · [Back to portfolio](../../../../README.md)
