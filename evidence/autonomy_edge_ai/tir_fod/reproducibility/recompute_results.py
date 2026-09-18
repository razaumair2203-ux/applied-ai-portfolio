"""Recompute TIR-FOD public multi-seed summaries from sanitized scalar run records.

Zero third-party dependencies:
    python evidence/tir-fod/reproducibility/recompute_results.py
"""
from __future__ import annotations
import json
import statistics as st
from pathlib import Path

HERE = Path(__file__).resolve().parent
METRICS = ("test_mAP50", "test_mAP50_95", "test_mAP75", "precision", "recall")


def stats(values):
    return {"n": len(values), "mean": st.mean(values), "sample_std": st.stdev(values), "values": values}


def close(actual, expected, tol=1e-12):
    assert abs(actual - expected) <= tol, (actual, expected)


def main():
    payload = json.loads((HERE / "raw_seed_metrics.json").read_text(encoding="utf-8"))
    records = {}
    for run in payload["runs"]:
        records.setdefault(run["config"], {})[run["seed"]] = run
    assert sum(len(v) for v in records.values()) == 29

    summary = {
        cfg: {metric: stats([by_seed[s][metric] for s in sorted(by_seed)]) for metric in METRICS}
        for cfg, by_seed in records.items()
    }

    def paired(positive, negative):
        assert set(records[positive]) == set(records[negative]) == {42, 43, 44}
        seeds = sorted(records[positive])
        return {
            metric: stats([records[positive][s][metric] - records[negative][s][metric] for s in seeds])
            for metric in METRICS
        }

    pairs = {
        "contaminated_minus_clean": paired("contam_matched_s", "baseline_s"),
        "clean_minus_originals": paired("baseline_s", "originals_fixedopt_s"),
        "framelevel_minus_block": paired("framelevel_12c_s", "xsession_12c_s"),
    }

    # Public headline and manuscript-table invariants.
    close(summary["baseline_n"]["test_mAP50_95"]["mean"], 0.8603393111852491)
    close(summary["baseline_n"]["test_mAP50_95"]["sample_std"], 0.0016614579609774808)
    close(pairs["contaminated_minus_clean"]["test_mAP50_95"]["mean"], 0.08515008188999729)
    close(pairs["contaminated_minus_clean"]["test_mAP50_95"]["sample_std"], 0.0019233780114959458)
    close(summary["framelevel_12c_s"]["test_mAP50_95"]["mean"], 0.8222947814586841)
    close(summary["xsession_12c_s"]["test_mAP50_95"]["mean"], 0.7410327567690895)
    close(pairs["framelevel_minus_block"]["test_mAP50_95"]["mean"], 0.08126202468959454)
    close(pairs["framelevel_minus_block"]["test_mAP50_95"]["sample_std"], 0.04182231286178369)

    out = {"runs": 29, "configs": summary, "paired_differences": pairs}
    print(json.dumps(out, indent=2))
    print("PASS TIR-FOD: 29 public scalar run records reproduce current revision summaries.")


if __name__ == "__main__":
    main()
