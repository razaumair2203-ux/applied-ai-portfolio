"""Public portfolio integrity checks.

Zero-dependency checks for recruiter-facing evidence consistency.
Run from repository root:
    python tools/portfolio_integrity_check.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def check_internal_markdown_links() -> None:
    failures: list[str] = []
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            href = raw.strip().split("#", 1)[0]
            if not href or href.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = (path.parent / href).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                failures.append(f"{path.relative_to(ROOT)} -> {raw} escapes repository")
                continue
            if not target.exists():
                failures.append(f"{path.relative_to(ROOT)} -> {raw} missing")
    assert not failures, "\n".join(failures)


def check_json_evidence() -> None:
    for path in ROOT.rglob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))


def check_lodestar_eval_contract() -> None:
    spec_path = ROOT / "evidence" / "lodestar" / "grounding_pairs.json"
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    assert spec["k"] == 5
    assert len(spec["pairs"]) == 34
    assert all(pair.get("q") and pair.get("accepted") for pair in spec["pairs"])

    log = (ROOT / "evidence" / "lodestar" / "grounding-eval.md").read_text(encoding="utf-8")
    assert "1 / 34 misses (2.9%)" in log



def check_tir_fod_reproducibility() -> None:
    base = ROOT / "evidence" / "tir-fod" / "reproducibility"
    raw = json.loads((base / "raw_seed_metrics.json").read_text(encoding="utf-8"))
    protocol = json.loads((base / "training_protocol.json").read_text(encoding="utf-8"))
    split = json.loads((base / "current_v2_split_manifest.json").read_text(encoding="utf-8"))
    assert len(raw["runs"]) == 29
    assert protocol["full_benchmark_split"]["images"]["train"] == 18221
    assert protocol["full_benchmark_split"]["source_frames"] == {
        "train": 2450, "validation": 529, "test": 520
    }
    assert split["xsession_block_overlap"] == []
    assert set(split["classes"]) == {
        "HeadSet", "MetalShard", "Screw", "Nut", "PaperCup", "SafetyGoggle",
        "Scissor", "ScrewDriver", "SprayCan", "Tape", "SodaCan", "Wire"
    }


def check_lodestar_db_fixture_contract() -> None:
    base = ROOT / "evidence" / "lodestar" / "fixture"
    assert (base / "schema.sql").exists()
    assert (base / "postgres_fixture_test.py").exists()
    schema = (base / "schema.sql").read_text(encoding="utf-8")
    test = (base / "postgres_fixture_test.py").read_text(encoding="utf-8")
    assert "vector(1024)" in schema
    assert "websearch_to_tsquery" not in schema  # query logic stays in published retrieval module
    assert "from evidence.lodestar.hybrid_retrieval import hybrid_search" in test
    assert "criterion_tags" in test and "visa_class" in test


def check_jetson_historical_boundary() -> None:
    path = ROOT / "evidence" / "tir-fod" / "deployment" / "historical_measurement_status.json"
    rec = json.loads(path.read_text(encoding="utf-8"))
    assert rec["provenance"]["raw_per_run_logs_retained"] is False
    assert rec["provenance"]["deployed_tensorrt_engine_retained"] is False
    assert rec["provenance"]["historical_checkpoint_identifiable"] is False
    root = (ROOT / "README.md").read_text(encoding="utf-8")
    case = (ROOT / "projects" / "tir-fod-clear-run.md").read_text(encoding="utf-8")
    matrix = (ROOT / "docs" / "HEADLINE_EVIDENCE_MATRIX.md").read_text(encoding="utf-8")
    assert "raw per-run logs not retained" in root
    assert "author-confirmed ten-run" in case
    assert "Raw per-run logs and historical engine were not retained" in matrix
    assert "compute-and-camera subsystem power" not in case


def check_lodestar_assessment_eval_contract() -> None:
    base = ROOT / "evidence" / "lodestar" / "assessment_eval"
    spec = json.loads((base / "evaluation_cases.json").read_text(encoding="utf-8"))
    assert len(spec["cases"]) == 10
    readme = (base / "README.md").read_text(encoding="utf-8")
    assert "100% post-gate citation validity" in readme
    assert "not a claim of legal correctness" in readme
    guard = (base / "assessment_guardrail.py").read_text(encoding="utf-8")
    assert "FIVE_STATES" in guard
    assert "approval_probability" not in guard


def check_repository_metadata_contract() -> None:
    spec = json.loads((ROOT / "docs" / "REPOSITORY_METADATA_CONTRACT.json").read_text(encoding="utf-8"))
    assert spec["desired_description"].startswith("Applied AI portfolio:")
    assert len(spec["desired_topics"]) == 12
    assert "computer-vision" in spec["desired_topics"]
    assert "rag" in spec["desired_topics"]
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    assert "All rights reserved" in license_text


def check_audit_closure_state() -> None:
    first = (ROOT / "docs" / "AI_PORTFOLIO_INSPECTION_CONTRACT.md").read_text(encoding="utf-8")
    reaudit = (ROOT / "docs" / "AI_PORTFOLIO_REAUDIT_2026-09-18.md").read_text(encoding="utf-8")
    closure = (ROOT / "docs" / "AUDIT_CLOSURE_MATRIX.md").read_text(encoding="utf-8")
    assert "**Status:** open" not in first
    assert "**Status:** open" not in reaudit
    assert "RESOLVED / CHARACTERIZED" in reaudit
    assert "Content closed; live About fields external-admin pending" in closure
    assert "No code/content remediation remains open" in closure
    assert (ROOT / "evidence" / "lodestar" / "fixture" / "authority_ablation.py").exists()

def check_claim_boundaries() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "Evidence boundary." in readme
    assert "team-developed Clear Run" in readme
    assert "1/34 top-5 expected-source misses (2.9%)" in readme

    clear_run = (ROOT / "projects" / "tir-fod-clear-run.md").read_text(encoding="utf-8")
    assert "does not yet establish closed-loop physical goal delivery" in clear_run


def check_final_release_authenticity() -> None:
    root = (ROOT / "README.md").read_text(encoding="utf-8")
    impact = (ROOT / "docs" / "IMPACT_MODEL.md").read_text(encoding="utf-8")
    final_audit = (ROOT / "docs" / "FINAL_RELEASE_AUDIT_2026-09-18.md").read_text(encoding="utf-8")
    tir = (ROOT / "projects" / "tir-fod-clear-run.md").read_text(encoding="utf-8")
    lodestar = (ROOT / "projects" / "lodestar.md").read_text(encoding="utf-8")

    assert "What “impact” means in this portfolio" in root
    assert "What is deliberately not claimed" in root
    assert "measured improvement in runway safety or mission effectiveness" in root
    assert "completed autonomous physical FOD recovery" in root
    assert "self-awarded recruiter score" in final_audit
    assert "Release decision: PASS" in final_audit
    assert "Technical risk retired" in impact
    assert "What does not count by itself" in impact
    assert "Engineering impact and decision value" in tir
    assert "What is not claimed" in tir
    assert "Engineering impact and decision value" in lodestar
    assert "What is not claimed" in lodestar

    forbidden_root = (
        "safety-critical AI system",
        "fully autonomous FOD recovery",
        "production-proven Lodestar",
        "measurably improved runway safety",
    )
    assert not any(term in root for term in forbidden_root)


def main() -> None:
    checks = [
        check_internal_markdown_links,
        check_json_evidence,
        check_lodestar_eval_contract,
        check_tir_fod_reproducibility,
        check_lodestar_db_fixture_contract,
        check_jetson_historical_boundary,
        check_lodestar_assessment_eval_contract,
        check_repository_metadata_contract,
        check_audit_closure_state,
        check_claim_boundaries,
        check_final_release_authenticity,
    ]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")
    print(f"PASS {len(checks)} portfolio integrity checks")


if __name__ == "__main__":
    main()
