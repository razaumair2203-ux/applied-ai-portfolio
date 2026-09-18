# TIR-FOD public reproducibility slice

This folder turns the portfolio's TIR-FOD evidence from a narrative/result snapshot into an independently inspectable numerical and training contract.

## What can be reproduced without a GPU

From the portfolio root:

```bash
python evidence/tir-fod/reproducibility/recompute_results.py
```

The script reads **29 sanitized seed-level scalar run records** and recomputes means, sample standard deviations and seed-paired differences used by the current revision. It asserts the headline values rather than merely printing them.

The public records reproduce, among other checks:

- YOLOv8n three-seed mAP@[.50:.95] **0.8603 ± 0.0017**;
- size-matched contamination effect **+0.0852 ± 0.0019**;
- frame-level 12-class mAP@[.50:.95] **0.8223 ± 0.0070**;
- acquisition-block-disjoint mAP@[.50:.95] **0.7410 ± 0.0423**;
- paired frame-level minus block-disjoint difference **+0.0813 ± 0.0418**.

## Inspect the exact training contract without installing ML packages

```bash
python evidence/tir-fod/reproducibility/train_public.py \
  --config baseline_n --data /path/to/frozen/data.yaml --seed 42 --dry-run
```

The dry run exposes the exact recorded hyperparameter contract. A full run imports Ultralytics only after the contract is printed/validated.

## Full training rerun boundary

A full model-training rerun requires the public TIR-FOD dataset, its frozen split files, compatible pretrained weights and a CUDA/PyTorch/Ultralytics environment. The dataset is linked from the portfolio case study and research record.

Use the **distributed frozen split lists directly**. The current revision uses 2,450 train / 529 validation / 520 test source frames; the training partition contains **18,221 images** after excluding stored four-image mosaics identified as unsafe for the source-lineage split. Regenerating a split from seed 42 is not treated as equivalent to the frozen lists.

The portfolio does not claim that CI retrains 29 GPU models. CI verifies the published protocol, compiles the real training harness, and independently recomputes all public scalar summaries.

## Files

- `raw_seed_metrics.json` — sanitized 29-run scalar results from the authoritative revision QA.
- `recompute_results.py` — zero-dependency summary and paired-difference recomputation.
- `training_protocol.json` — split, hyperparameter, config and evaluation contract.
- `current_v2_split_manifest.json` — exact current frozen membership for the 12-class frame-level vs acquisition-block study.
- `environment.json` — recorded relevant software/hardware environment and YOLOv8 initializer hashes.
- `train_public.py` — sanitized training/evaluation harness matching the recorded protocol.
- `requirements.txt` — direct Python package requirement for the recorded Ultralytics environment.

## Provenance

The source records live in the private research workspace because the full workspace contains programme and manuscript material. These public files were derived from the authoritative current revision artifacts, with local paths and unrelated private material omitted. The raw scalar values are not synthesized or reverse-engineered from rounded table text.
