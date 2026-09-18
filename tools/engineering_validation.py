"""Repository engineering consistency checks.

Run from repository root:
    python tools/engineering_validation.py
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


def check_json_files() -> None:
    for path in ROOT.rglob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))


def check_lodestar_retrieval_spec() -> None:
    spec = json.loads(
        (ROOT / "evidence/lodestar/grounding_pairs.json").read_text(encoding="utf-8")
    )
    assert spec["k"] == 5
    assert len(spec["pairs"]) == 34
    assert all(pair.get("q") and pair.get("accepted") for pair in spec["pairs"])

    log = (ROOT / "evidence/lodestar/grounding-eval.md").read_text(encoding="utf-8")
    assert "1 / 34 misses (2.9%)" in log


def check_lodestar_reliability_regression() -> None:
    path = ROOT / "evidence/lodestar/reliability_regression.py"
    text = path.read_text(encoding="utf-8")
    assert "PASS {len(checks)} Lodestar reliability-regression invariants" in text
    assert "check_hallucinated_citation_refuses" in text
    assert "check_relevance_can_beat_authority" in text


def check_lodestar_db_fixture() -> None:
    base = ROOT / "evidence/lodestar/fixture"
    schema = (base / "schema.sql").read_text(encoding="utf-8")
    test = (base / "postgres_fixture_test.py").read_text(encoding="utf-8")
    assert "vector(1024)" in schema
    assert "from evidence.lodestar.hybrid_retrieval import hybrid_search" in test
    assert "criterion_tags" in test and "visa_class" in test


def check_lodestar_assessment_eval() -> None:
    base = ROOT / "evidence/lodestar/assessment_eval"
    spec = json.loads((base / "evaluation_cases.json").read_text(encoding="utf-8"))
    assert len(spec["cases"]) == 10
    guard = (base / "assessment_guardrail.py").read_text(encoding="utf-8")
    assert "FIVE_STATES" in guard
    assert "approval_probability" not in guard


def check_clear_run_field_evidence() -> None:
    base = ROOT / "evidence/clear-run"
    snapshot = json.loads((base / "field_trial_snapshot.json").read_text(encoding="utf-8"))
    matrix = json.loads((base / "mission_verification_matrix.json").read_text(encoding="utf-8"))
    assert snapshot["video_evidence"]["unique_videos"] == 8
    assert snapshot["structured_rgb_events"]["events"] == 12
    assert snapshot["structured_rgb_events"]["class_count"] == 8
    assert len(matrix["stages"]) == 9
    assert matrix["stages"][-1]["id"] == "CR-09"
    assert matrix["stages"][-1]["status"] == "open_measurement"


def check_tir_fod_reproducibility() -> None:
    base = ROOT / "evidence/tir-fod/reproducibility"
    raw = json.loads((base / "raw_seed_metrics.json").read_text(encoding="utf-8"))
    protocol = json.loads((base / "training_protocol.json").read_text(encoding="utf-8"))
    split = json.loads((base / "current_v2_split_manifest.json").read_text(encoding="utf-8"))
    assert len(raw["runs"]) == 29
    assert protocol["full_benchmark_split"]["images"]["train"] == 18221
    assert protocol["full_benchmark_split"]["source_frames"] == {
        "train": 2450,
        "validation": 529,
        "test": 520,
    }
    assert split["xsession_block_overlap"] == []


def check_jetson_measurement_record() -> None:
    rec = json.loads(
        (ROOT / "evidence/tir-fod/deployment/historical_measurement_status.json").read_text(
            encoding="utf-8"
        )
    )
    assert rec["provenance"]["raw_per_run_logs_retained"] is False
    assert rec["provenance"]["deployed_tensorrt_engine_retained"] is False
    assert rec["provenance"]["historical_checkpoint_identifiable"] is False


def check_primary_visuals() -> None:
    required = (
        "visuals/clear-run/overview.png",
        "visuals/clear-run/system_architecture.svg",
        "visuals/clear-run/aerial_unit_architecture.svg",
        "visuals/clear-run/gcs_architecture.svg",
        "visuals/clear-run/ugv_architecture.svg",
        "visuals/clear-run/field_trial_evidence.png",
        "visuals/clear-run/gcs_integration.png",
        "visuals/clear-run/retrieval_development.png",
        "visuals/tir-fod/cover.png",
        "visuals/tir-fod/airborne_platform.png",
        "visuals/tir-fod/jetson_mounted.png",
        "visuals/tir-fod/camera_mount.png",
        "visuals/tir-fod/capture_sessions.png",
        "visuals/tir-fod/jetson_runtime.png",
        "visuals/counter-uas/outdoor_detection.png",
        "visuals/counter-uas/indoor_detection.png",
        "visuals/counter-uas/training_curves.png",
        "visuals/counter-uas/framework_evolution.svg",
        "visuals/lodestar_product_surface.svg",
        "visuals/lodestar_architecture.svg",
        "visuals/lodestar_execution_trace.svg",
        "visuals/msha/logo-wordmark.svg",
        "visuals/msha/dashboard-regression.png",
        "visuals/joblooper/app-icon.svg",
        "visuals/joblooper/dashboard-surface.svg",
        "visuals/joblooper/workflow.svg",
        "visuals/codex/audit-report-preview.jpg",
        "visuals/codex/audit_report_anatomy.svg",
        "visuals/buildsignal/admin-surface.svg",
        "visuals/buildsignal/ai-judge-loop-system.svg",
        "visuals/mbse/clear_run_system_architecture.svg",
        "visuals/mbse/telemetry_replay.svg",
        "visuals/ai-evaluation/evaluation_pipeline.svg",
    )
    for rel in required:
        path = ROOT / rel
        assert path.exists() and path.stat().st_size > 0

    # Provenance-sensitive assets should not silently drift after source verification.
    msha_wordmark = (ROOT / "visuals/msha/logo-wordmark.svg").read_text(encoding="utf-8")
    assert "i-MSHA Wordmark Logo" in msha_wordmark
    assert "Hard hat in rounded square" in msha_wordmark


def check_career_profile() -> None:
    path = ROOT / "profile/AI_BASE_RESUME.md"
    text = path.read_text(encoding="utf-8")
    required = (
        "18+ years",
        "100+ project",
        "60+ advanced engineering projects",
        "TIR-FOD / Clear Run",
        "Lodestar",
        "22-node GPU/HPC",
        "150+ aircraft",
        "93 upgrade actions",
        "135+ units fielded",
        "first three Super Mushshak",
        "Chengdu Aircraft Design Institute",
        "ZDK-03",
        "Project Management Professional",
        "PMI Agile Certified Practitioner",
        "Professional Engineer",
        "10.5281/zenodo.22546586",
    )
    for marker in required:
        assert marker in text, marker
    forbidden = ("phone:", "mobile:", "home address", "street address")
    lower = text.lower()
    assert not any(marker in lower for marker in forbidden)


def check_documentation_structure() -> None:
    root = (ROOT / "README.md").read_text(encoding="utf-8")

    # Career context must precede project detail.
    assert root.index("## At a glance") < root.index(
        "## Applied AI, autonomy and digital engineering"
    )
    assert root.index("## Applied AI, autonomy and digital engineering") < root.index(
        "## Flagship systems and evidence"
    )
    assert "Officer In Charge Projects / R&D & Systems Engineering Lead" in root
    assert "programme leadership + hands-on AI engineering + aerospace-grade systems discipline" in root

    # Core project-family coverage.
    for marker in (
        "Clear Run / TIR-FOD",
        "Lodestar",
        "i-MSHA / MSHA Compliance SaaS",
        "JobLooper / JobLoop-AI",
        "Adversarial Review Lite",
        "BuildSignal AI",
        "Counter-UAS Phase I",
        "AI Systems Assurance / MBSE",
        "Super Mushshak digital engineering",
    ):
        assert marker in root, marker

    # Flagship evidence and career context.
    assert "3,499 source frames" in root
    assert "12 structured RGB events" in root
    assert "209 documents" in root
    assert "100+ project portfolio" in root
    assert "60+ advanced engineering projects" in root
    assert "visuals/tir-fod/airborne_platform.png" in root
    assert "visuals/clear-run/field_trial_evidence.png" in root
    assert "visuals/lodestar_product_surface.svg" in root
    assert "visuals/msha/dashboard-regression.png" in root
    assert "visuals/joblooper/dashboard-surface.svg" in root
    assert "visuals/codex/audit-report-preview.jpg" in root
    assert "profile/AI_BASE_RESUME.md" in root
    assert "private product in pre-deployment hardening" in root
    assert "Super-Mushshak-Glass-Cockpit-Modification/main/assets/dynon-cockpit-prototype-sanitized.jpg" in root


    clear_run = (ROOT / "projects/tir-fod-clear-run.md").read_text(encoding="utf-8")
    assert "final detection-to-physical-retention chain is still being quantitatively closed" in clear_run
    assert "mission_verification_matrix.json" in clear_run

    lodestar = (ROOT / "projects/lodestar.md").read_text(encoding="utf-8")
    assert "34-query set is a regression set" in lodestar
    assert "11-invariant reliability regression" in lodestar

    project_index = (ROOT / "projects/README.md").read_text(encoding="utf-8")
    assert "msha-compliance-ai.md" in project_index
    assert "buildsignal-ai.md" in project_index
    assert "super-mushshak-digital-engineering.md" in project_index



def main() -> None:
    checks = [
        check_internal_markdown_links,
        check_json_files,
        check_lodestar_retrieval_spec,
        check_lodestar_reliability_regression,
        check_lodestar_db_fixture,
        check_lodestar_assessment_eval,
        check_clear_run_field_evidence,
        check_tir_fod_reproducibility,
        check_jetson_measurement_record,
        check_primary_visuals,
        check_career_profile,
        check_documentation_structure,
    ]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")
    print(f"PASS {len(checks)} repository engineering checks")


if __name__ == "__main__":
    main()
