#!/usr/bin/env python3
import json
from pathlib import Path

data = json.loads(Path(__file__).with_name("evaluation_summary.json").read_text(encoding="utf-8"))
assert data["schema"] == "ai-evaluation.aggregate-v1"
assert data["pilot"]["total_pairs"] == 50
assert data["pilot"]["split"] == {"train": 20, "validation": 15, "held_out": 15}
assert data["pilot"]["coverage_counts"] == {"personas": 9, "industries": 40, "regions": 8, "jd_styles": 5}
assert data["pilot"]["sensitivity"]["fabrication_detection"] == 1.0
assert data["pilot"]["sensitivity"]["metric_detection"] == 0.92
assert data["pilot"]["sensitivity"]["date_detection"] == 1.0
assert data["baseline_comparison"]["evaluated_pairs"] == 20
assert data["jd_parser_rescore"]["pairs_scored"] == 38
assert data["safeguard_example"]["decision"] == "BLOCKED"
assert data["safeguard_example"]["requires_human_review"] is True
assert any("not live product metrics" in x for x in data["limitations"])
print("AI evaluation aggregate evidence: OK")
