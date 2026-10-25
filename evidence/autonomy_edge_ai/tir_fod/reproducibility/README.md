# TIR-FOD reproducibility

## What this code shows

The 29 seed-level training results behind the TIR-FOD paper, and the exact training recipe.

| Result | Value |
|---|---|
| YOLOv8n mAP@[.50:.95], 3 seeds | **0.8603 ± 0.0017** |
| Inflation from split leakage | **+8.52 ± 0.19 pp** |
| Frame-level split mAP | **0.8223 ± 0.0070** |
| Acquisition-block split mAP | **0.7410 ± 0.0423** |

Files: [per-run results](raw_seed_metrics.json) · [result checker](recompute_results.py) · [training recipe](training_protocol.json) · [split membership](current_v2_split_manifest.json) · [environment](environment.json) · [training harness](train_public.py) · [requirements](requirements.txt)

## How to run

Recompute all summary numbers (no GPU, no dependencies):

```bash
python evidence/autonomy_edge_ai/tir_fod/reproducibility/recompute_results.py
```

Print the training recipe without installing ML packages:

```bash
python evidence/autonomy_edge_ai/tir_fod/reproducibility/train_public.py \
  --config baseline_n --data /path/to/frozen/data.yaml --seed 42 --dry-run
```

Full retraining needs the [public dataset](https://doi.org/10.5281/zenodo.22546586), its frozen split lists, a CUDA GPU and `pip install -r requirements.txt`. Use the frozen lists (2,450 train / 529 validation / 520 test source frames) rather than regenerating splits.

[Back to TIR-FOD code](../README.md) · [Back to portfolio](../../../../README.md)
