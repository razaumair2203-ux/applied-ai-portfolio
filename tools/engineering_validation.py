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
        (ROOT / "evidence/compliance_regtech/lodestar/grounding_pairs.json").read_text(encoding="utf-8")
    )
    assert spec["k"] == 5
    assert len(spec["pairs"]) == 34
    assert all(pair.get("q") and pair.get("accepted") for pair in spec["pairs"])

    log = (ROOT / "evidence/compliance_regtech/lodestar/grounding-eval.md").read_text(encoding="utf-8")
    assert "1 / 34 misses (2.9%)" in log


def check_lodestar_reliability_regression() -> None:
    path = ROOT / "evidence/compliance_regtech/lodestar/reliability_regression.py"
    text = path.read_text(encoding="utf-8")
    assert "PASS {len(checks)} Lodestar reliability-regression invariants" in text
    assert "check_hallucinated_citation_refuses" in text
    assert "check_relevance_can_beat_authority" in text


def check_lodestar_db_fixture() -> None:
    base = ROOT / "evidence/compliance_regtech/lodestar/fixture"
    schema = (base / "schema.sql").read_text(encoding="utf-8")
    test = (base / "postgres_fixture_test.py").read_text(encoding="utf-8")
    assert "vector(1024)" in schema
    assert "from evidence.compliance_regtech.lodestar.hybrid_retrieval import hybrid_search" in test
    assert "criterion_tags" in test and "visa_class" in test


def check_lodestar_assessment_eval() -> None:
    base = ROOT / "evidence/compliance_regtech/lodestar/assessment_eval"
    spec = json.loads((base / "evaluation_cases.json").read_text(encoding="utf-8"))
    assert len(spec["cases"]) == 10
    guard = (base / "assessment_guardrail.py").read_text(encoding="utf-8")
    assert "FIVE_STATES" in guard
    assert "approval_probability" not in guard


def check_clear_run_field_evidence() -> None:
    base = ROOT / "evidence/autonomy_edge_ai/clear_run"
    snapshot = json.loads((base / "field_trial_snapshot.json").read_text(encoding="utf-8"))
    matrix = json.loads((base / "mission_verification_matrix.json").read_text(encoding="utf-8"))
    assert snapshot["video_evidence"]["unique_videos"] == 8
    assert snapshot["structured_rgb_events"]["events"] == 12
    assert snapshot["structured_rgb_events"]["class_count"] == 8
    assert len(matrix["stages"]) == 9
    assert matrix["stages"][-1]["id"] == "CR-09"
    assert matrix["stages"][-1]["status"] == "open_measurement"


def check_tir_fod_reproducibility() -> None:
    base = ROOT / "evidence/autonomy_edge_ai/tir_fod/reproducibility"
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
        (ROOT / "evidence/autonomy_edge_ai/tir_fod/deployment/historical_measurement_status.json").read_text(
            encoding="utf-8"
        )
    )
    assert rec["provenance"]["raw_per_run_logs_retained"] is False
    assert rec["provenance"]["deployed_tensorrt_engine_retained"] is False
    assert rec["provenance"]["historical_checkpoint_identifiable"] is False


def check_primary_visuals() -> None:
    required = (
        "visuals/autonomy-edge-ai/clear-run/overview.png",
        "visuals/autonomy-edge-ai/clear-run/system_architecture.svg",
        "visuals/autonomy-edge-ai/clear-run/aerial_unit_architecture.svg",
        "visuals/autonomy-edge-ai/clear-run/gcs_architecture.svg",
        "visuals/autonomy-edge-ai/clear-run/ugv_architecture.svg",
        "visuals/autonomy-edge-ai/clear-run/field_trial_evidence.png",
        "visuals/autonomy-edge-ai/clear-run/gcs_integration.png",
        "visuals/autonomy-edge-ai/clear-run/retrieval_development.png",
        "visuals/autonomy-edge-ai/tir-fod/cover.png",
        "visuals/autonomy-edge-ai/tir-fod/airborne_platform.png",
        "visuals/autonomy-edge-ai/tir-fod/jetson_mounted.png",
        "visuals/autonomy-edge-ai/tir-fod/camera_mount.png",
        "visuals/autonomy-edge-ai/tir-fod/capture_sessions.png",
        "visuals/autonomy-edge-ai/tir-fod/jetson_runtime.png",
        "visuals/autonomy-edge-ai/counter-uas/phase1_original_mount.jpg",
        "visuals/autonomy-edge-ai/counter-uas/phase1_video_mount.jpg",
        "visuals/autonomy-edge-ai/counter-uas/outdoor_detection.png",
        "visuals/autonomy-edge-ai/counter-uas/indoor_detection.png",
        "visuals/autonomy-edge-ai/counter-uas/training_curves.png",
        "visuals/autonomy-edge-ai/counter-uas/framework_evolution.svg",
        "visuals/compliance-regtech/lodestar/product-surface.svg",
        "visuals/compliance-regtech/lodestar/architecture.svg",
        "visuals/compliance-regtech/lodestar/execution-trace.svg",
        "visuals/compliance-regtech/i-msha/logo-wordmark.svg",
        "visuals/compliance-regtech/i-msha/dashboard-regression.png",
        "visuals/practical-ai-products/joblooper/app-icon.svg",
        "visuals/practical-ai-products/joblooper/dashboard-surface.svg",
        "visuals/practical-ai-products/joblooper/workflow.svg",
        "visuals/assurance-digital-engineering/adversarial-review/audit-report-preview.jpg",
        "visuals/assurance-digital-engineering/adversarial-review/audit_report_anatomy.svg",
        "visuals/practical-ai-products/buildsignal/admin-surface.svg",
        "visuals/practical-ai-products/buildsignal/ai-judge-loop-system.svg",
        "visuals/autonomy-edge-ai/mbse/clear_run_system_architecture.svg",
        "visuals/autonomy-edge-ai/mbse/telemetry_replay.svg",
        "visuals/assurance-digital-engineering/ai-evaluation/evaluation_pipeline.svg",
    )
    for rel in required:
        path = ROOT / rel
        assert path.exists() and path.stat().st_size > 0

    # Provenance-sensitive assets should not silently drift after source verification.
    msha_wordmark = (ROOT / "visuals/compliance-regtech/i-msha/logo-wordmark.svg").read_text(encoding="utf-8")
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


def check_presentation_integrity() -> None:
    public_paths = [
        ROOT / "README.md",
        ROOT / "domains",
        ROOT / "profile",
        ROOT / "research",
        ROOT / "evidence",
        ROOT / "visuals",
    ]
    forbidden = (
        "under the user's",
        "the user's pi leadership",
        "side-project bucket",
        "portfolio-only demo",
        "portfolio-only demonstrations",
        "why this belongs in an ai portfolio",
        "why it matters to the ai/autonomy portfolio",
        "aggressively building",
        "recruiter-facing",
    )
    failures: list[str] = []
    for base in public_paths:
        paths = [base] if base.is_file() else list(base.rglob("*.md"))
        for path in paths:
            text = path.read_text(encoding="utf-8").lower()
            for marker in forbidden:
                if marker in text:
                    failures.append(f"{path.relative_to(ROOT)} contains forbidden phrase: {marker}")
    assert not failures, "\n".join(failures)


def check_root_readme_scanability() -> None:
    root = (ROOT / "README.md").read_text(encoding="utf-8")
    words = re.findall(r"\b[\w+.-]+\b", root)
    assert len(words) <= 2400, f"README too long for first-pass scan: {len(words)} words"

    image_positions = [pos for pos in (root.find("!["), root.find("<img")) if pos >= 0]
    assert image_positions, "README must contain authentic visual evidence"
    first_image = min(image_positions)
    words_before_first_image = re.findall(r"\b[\w+.-]+\b", root[:first_image])
    assert len(words_before_first_image) <= 550, (
        f"First visual appears too late: {len(words_before_first_image)} words"
    )

    assert root.count("<img ") + root.count("![") <= 12, "README visual density is too high"


def check_private_review_contract() -> None:
    access = (ROOT / "PRIVATE_REPOSITORY_ACCESS.md").read_text(encoding="utf-8")
    assert "smallest useful review surface" in access
    assert "curated release-safe technical package or review branch" in access
    assert "complete repository access only when the repository itself is suitable" in access
    assert "LinkedIn" in access

    templates = (
        "access-clear-run.yml",
        "access-counter-uas.yml",
        "access-i-msha.yml",
        "access-lodestar.yml",
        "access-joblooper-private.yml",
        "access-buildsignal.yml",
    )
    for name in templates:
        text = (ROOT / ".github" / "ISSUE_TEMPLATE" / name).read_text(encoding="utf-8")
        assert "does not automatically grant raw repository access" in text
        assert "curated release-safe package or branch" in text


def check_atlas_case() -> None:
    path = ROOT / "domains/04-assurance-digital-engineering/atlas-hpc.md"
    text = path.read_text(encoding="utf-8")
    for marker in (
        "22-node",
        "Linux / Ubuntu",
        "SLURM",
        "CUDA",
        "Docker",
        "accountable technical leadership",
        "Public-release boundary",
    ):
        assert marker in text, marker


def check_research_contribution_boundaries() -> None:
    text = (ROOT / "research/README.md").read_text(encoding="utf-8")
    assert text.count("**Contribution boundary:** co-author") >= 3
    assert "**Programme contribution:**" in text
    assert "individual contribution is not inferred from author order" in text


def check_documentation_structure() -> None:
    root = (ROOT / "README.md").read_text(encoding="utf-8")

    # Career context and proof must precede the deeper project dossier.
    assert root.index("## At a glance") < root.index("## Portfolio map")
    assert root.index("## Portfolio map") < root.index("## Flagship systems")
    assert "Applied AI & Autonomous Systems Engineering Leader" in root
    assert "Officer In Charge Projects / R&D & Systems Engineering Lead" in root

    # Core project-family coverage.
    for marker in (
        "Clear Run / TIR-FOD",
        "Lodestar",
        "i-MSHA",
        "JobLooper",
        "Adversarial Review Lite",
        "BuildSignal AI",
        "Counter-UAS Phase I",
        "AI Systems Assurance / MBSE",
        "Super Mushshak",
        "ATLAS GPU/HPC",
    ):
        assert marker in root, marker

    # Flagship evidence and career context.
    for marker in (
        "3,499 source frames",
        "12 structured RGB events",
        "209 documents",
        "100+ project portfolio",
        "60+ advanced engineering projects",
        "visuals/autonomy-edge-ai/tir-fod/airborne_platform.png",
        "visuals/autonomy-edge-ai/clear-run/clear_run_detection_to_removal_architecture.webp",
        "visuals/compliance-regtech/i-msha/dashboard-regression.png",
        "visuals/compliance-regtech/lodestar/product-surface.svg",
        "visuals/practical-ai-products/joblooper/dashboard-surface.svg",
        "visuals/autonomy-edge-ai/counter-uas/phase1_original_mount.jpg",
        "profile/AI_BASE_RESUME.md",
        "curated, release-safe technical package or review branch",
    ):
        assert marker in root, marker

    mbse_case = (ROOT / "domains/01-autonomy-edge-ai/ai-systems-assurance-mbse.md").read_text(encoding="utf-8")
    assert "../../visuals/autonomy-edge-ai/clear-run/system_architecture.svg" in mbse_case
    assert "../../visuals/autonomy-edge-ai/clear-run/aerial_unit_architecture.svg" in mbse_case
    assert "../../visuals/autonomy-edge-ai/clear-run/gcs_architecture.svg" in mbse_case
    assert "../../visuals/autonomy-edge-ai/clear-run/ugv_architecture.svg" in mbse_case
    assert "## AI system assurance contribution" in mbse_case

    clear_run = (ROOT / "domains/01-autonomy-edge-ai/clear-run-tir-fod.md").read_text(encoding="utf-8")
    assert "final detection-to-physical-retention chain is still being quantitatively closed" in clear_run
    assert "mission_verification_matrix.json" in clear_run
    assert "## Contribution boundary" in clear_run
    assert "Team-developed work" in clear_run

    lodestar = (ROOT / "domains/02-compliance-regtech/lodestar.md").read_text(encoding="utf-8")
    assert "34-query set is a regression set" in lodestar
    assert "11-invariant reliability regression" in lodestar
    assert "Agent-assisted implementation" in lodestar

    counter_uas = (ROOT / "domains/01-autonomy-edge-ai/counter-uas.md").read_text(encoding="utf-8")
    assert "../../visuals/autonomy-edge-ai/counter-uas/phase1_original_mount.jpg" in counter_uas
    assert "../../visuals/autonomy-edge-ai/counter-uas/phase1_video_mount.jpg" in counter_uas
    assert "../../evidence/autonomy_edge_ai/counter_uas/hardware_provenance.json" in counter_uas
    assert "## Contribution boundary" in counter_uas
    counter_hw = json.loads(
        (ROOT / "evidence/autonomy_edge_ai/counter_uas/hardware_provenance.json").read_text(encoding="utf-8")
    )
    assert len(counter_hw) == 2
    assert counter_hw[0]["description"] == "Constructed Phase I laser-camera mount"
    assert "no semantic alteration" in counter_hw[0]["transformation"]

    project_index = (ROOT / "domains/README.md").read_text(encoding="utf-8")
    assert "02-compliance-regtech/i-msha.md" in project_index
    assert "03-practical-ai-products/buildsignal-ai.md" in project_index
    assert "04-assurance-digital-engineering/super-mushshak-digital-engineering.md" in project_index
    assert "04-assurance-digital-engineering/atlas-hpc.md" in project_index
    assert "JobLooper / JobPilot" not in project_index

    # Domain hierarchy is the repository structure, not only a landing-page label.
    for rel in (
        "domains/01-autonomy-edge-ai/README.md",
        "domains/02-compliance-regtech/README.md",
        "domains/03-practical-ai-products/README.md",
        "domains/04-assurance-digital-engineering/README.md",
    ):
        assert (ROOT / rel).exists(), rel
    assert not (ROOT / "projects").exists()
    for rel in (
        "evidence/lodestar", "evidence/clear-run", "evidence/tir-fod",
        "visuals/clear-run", "visuals/tir-fod", "visuals/msha", "visuals/joblooper",
    ):
        assert not (ROOT / rel).exists(), rel


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
        check_presentation_integrity,
        check_root_readme_scanability,
        check_private_review_contract,
        check_atlas_case,
        check_research_contribution_boundaries,
        check_documentation_structure,
    ]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")
    print(f"PASS {len(checks)} repository engineering checks")


if __name__ == "__main__":
    main()
