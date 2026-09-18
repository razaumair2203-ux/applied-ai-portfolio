# TIR-FOD technical evidence

This folder contains the public-safe numerical and reproducibility evidence for the TIR-FOD benchmark and deployment claims.

## Public paths

- [Reproducibility slice](reproducibility/README.md) — **29 seed-level scalar records**, exact training/evaluation contract, current split manifest, recorded environment, GPU training harness and zero-dependency result recomputation.
- [Legacy benchmark snapshot](benchmark_results.json) — selected single-run benchmark fields retained for historical traceability.

Run the current numerical verification from the repository root:

```bash
python evidence/autonomy_edge_ai/tir_fod/reproducibility/recompute_results.py
```

The current revision's aggregate claims should be verified from the reproducibility bundle, not inferred from the older single-run snapshot.

[Back to technical evidence index](../../README.md)
