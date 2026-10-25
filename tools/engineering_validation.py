"""Repository engineering consistency checks.

Run from repository root:
    python tools/engineering_validation.py
"""

from __future__ import annotations

import json
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HTML_REF_RE = re.compile(r'(?:href|src)="([^"]+)"')


def check_documented_python_modules() -> None:
    """Every documented local python -m entry point must exist."""
    for path in ROOT.rglob("*.md"):
        for module in re.findall(r"python -m (evidence\.[\w.]+)", path.read_text()):
            target = ROOT.joinpath(*module.split("."))
            assert target.with_suffix(".py").exists() or (target / "__main__.py").exists(), (path, module)


def check_hardware_publication_hashes() -> None:
    records = json.loads((ROOT / "evidence/autonomy_edge_ai/counter_uas/hardware_provenance.json").read_text())
    for record in records:
        path = ROOT / record.get("portfolio_path", record.get("output"))
        assert path.is_file(), record.get("portfolio_path", record.get("output"))
        assert hashlib.sha256(path.read_bytes()).hexdigest() == record.get("sha256", record.get("output_sha256")), record.get("portfolio_path", record.get("output"))


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


def check_internal_html_refs() -> None:
    failures: list[str] = []
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for raw in HTML_REF_RE.findall(text):
            href = raw.strip().split("#", 1)[0]
            if not href or raw.startswith(("#", "http://", "https://", "mailto:")):
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
        "visuals/assurance-digital-engineering/super-mushshak/dynon-skyview-installed-prototype.jpg",
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
        "Autonomous / Embedded / Edge AI",
        "Compliance / Regulatory Intelligence",
        "Practical Agentic AI Products",
        "AI Assurance / Evaluation / Digital Engineering",
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
        "msha v2",
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
    assert len(words) <= 2200, f"README too long for first-pass scan: {len(words)} words"

    image_positions = [pos for pos in (root.find("!["), root.find("<img")) if pos >= 0]
    assert image_positions, "README must contain authentic visual evidence"
    first_image = min(image_positions)
    words_before_first_image = re.findall(r"\b[\w+.-]+\b", root[:first_image])
    assert len(words_before_first_image) <= 700, (
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
    """Validate the current source-authentic, recruiter-readable portfolio."""
    root = (ROOT / "README.md").read_text(encoding="utf-8")
    gallery = (ROOT / "media/showcase/README.md").read_text(encoding="utf-8")

    selected_cases = (
        ("### 01 · Clear Run", "media/showcase/clear-run-real-collector-sequence.png"),
        ("### 02 · Super Mushshak", "media/showcase/super-mushshak-original-flight-evidence.png"),
        ("### 03 · TIR-FOD", "media/showcase/tir-fod-23-class-evidence-atlas.png"),
        ("### 04 · Counter-UAS Phase I", "media/showcase/counter-uas-real-physical-evidence.png"),
    )
    last = -1
    for heading, media in selected_cases:
        assert heading in root, heading
        pos = root.index(heading)
        assert pos > last, heading
        last = pos
        assert media in root, media
        assert (ROOT / media).is_file(), media
        assert media.split("/")[-1] in gallery, media

    for marker in (
        "Aerospace Systems Integration",
        "JF-17", "ZDK-03 AEW&C",
        "23 FOD categories", "3,499", "5,593",
        "team-reported integrated prototype demonstration",
        "not an operational counter-drone system",
        "Lodestar", "i-MSHA", "JobLooper",
        "Adversarial Review Lite", "BuildSignal AI", "ATLAS",
    ):
        assert marker.lower() in root.lower(), marker

    import struct
    dimensions = {
        "media/showcase/clear-run-real-collector-sequence.png": (1600, 900),
        "media/showcase/super-mushshak-original-flight-evidence.png": (1600, 900),
        "media/showcase/tir-fod-23-class-evidence-atlas.png": (1600, 1260),
        "media/showcase/counter-uas-real-physical-evidence.png": (1600, 900),
    }
    for rel, expected in dimensions.items():
        raw = (ROOT / rel).read_bytes()
        assert raw[:8] == b"\x89PNG\r\n\x1a\n", rel
        assert struct.unpack(">II", raw[16:24]) == expected, rel
        assert len(raw) > 50000, rel
        svg = ROOT / rel.replace(".png", ".svg")
        assert svg.is_file(), svg
        data = svg.read_text(encoding="utf-8")
        assert "data:image/" in data and "<script" not in data.lower(), svg

    atlas = (ROOT / "media/showcase/tir-fod-23-class-evidence-atlas.svg").read_text(encoding="utf-8")
    taxonomy = (
        "Bottle", "Label", "Cutter", "AllenKey", "Glove", "Hammer",
        "HeadSet", "MetalShard", "Screw", "Nut", "Wrench", "PaperCup",
        "Plier", "SafetyGoggle", "Scissor", "ScrewDriver", "SprayCan",
        "Stick", "Rock", "Tape", "SodaCan", "Wire", "Pen",
    )
    assert len(taxonomy) == 23
    for name in taxonomy:
        assert f">{name}</text>" in atlas, name

    import hashlib
    origin_hashes = {
        "tir-fod-23-class-source-grid.png": "fa9b03a15d71efea097ddd5c822b3ad33c8a477b",
        "clear-run-collector-before.jpg": "7e003c31437168db62f0fe15c6421c2889e486d8",
        "clear-run-collector-approach.jpg": "2ea107c8015cc7f9db4f5b077c157d9849036ba9",
        "clear-run-collector-source-outcome-overlay.jpg": "9e76eacb0eb6f408fd53b566e804193b1f40b0b0",
        "clear-run-uav-inflight.jpg": "6f1edff8d617b09da621ef1d349e5c29b1b5a96f",
    }
    for name, expected_sha in origin_hashes.items():
        raw = (ROOT / "media/real" / name).read_bytes()
        calculated = hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()
        assert calculated == expected_sha, name


def check_portfolio_guardrails() -> None:
    """Keep team attribution, distinct hardware configurations and actual-media truth."""
    root = (ROOT / "README.md").read_text(encoding="utf-8")
    gallery = (ROOT / "media/showcase/README.md").read_text(encoding="utf-8")
    for needle in (
        "team-reported", "not an operational counter-drone system",
        "23 independently validated per-class detections",
        "Original source", "2.5×",
    ):
        assert needle.lower() in (root + gallery).lower(), needle

    assert "JF-17" in root and "ZDK-03 AEW&C" in root
    assert "Super Mushshak" in root and "Counter-UAS Phase I" in root
    assert "TIR-FOD" in root and "Clear Run" in root
    assert "CloakBench" in root and "IN-ARCP" in root

    clear_run = (ROOT / "domains/01-autonomy-edge-ai/CLEAR_RUN_ENGINEERING_CASE_2026_10.md").read_text(encoding="utf-8")
    assert "small-wheel" in clear_run
    assert "2.5×" in clear_run
    assert "repeated, independently auditable" in clear_run.lower()
    assert "tracked/skid-steer" in clear_run

    thermal = (ROOT / "domains/01-autonomy-edge-ai/clear-run-tir-fod.md").read_text(encoding="utf-8")
    assert "tir-fod-23-class-evidence-atlas.png" in thermal
    assert "source-aware" in thermal
    assert "ROS2" in thermal and "Nav2" in thermal

    counter = (ROOT / "domains/01-autonomy-edge-ai/counter-uas.md").read_text(encoding="utf-8")
    for marker in ("phase1_original_mount.jpg", "outdoor_detection.png", "indoor_detection.png", "## Contribution boundary"):
        assert marker in counter, marker

    aircraft = (ROOT / "domains/04-assurance-digital-engineering/super-mushshak-digital-engineering.md").read_text(encoding="utf-8")
    assert "super-mushshak-original-flight-evidence.png" in aircraft
    assert "Dynon" in aircraft and "Garmin" in aircraft
    assert "lead systems engineer" in aircraft.lower()

    for name in ("clear-run-real-collector-sequence.png",
                 "tir-fod-23-class-evidence-atlas.png",
                 "counter-uas-real-physical-evidence.png",
                 "super-mushshak-original-flight-evidence.png"):
        assert name in gallery
    assert "not independently verified" in gallery.lower()
    assert "same edited" in gallery.lower() or "one edited" in gallery.lower()
    assert "fictional product screenshot is never substituted" in gallery.lower()

def check_visual_manifest_and_svg() -> None:
    """Validate actual publication bytes and SVG syntax, not just file presence."""
    import hashlib
    import xml.etree.ElementTree as ET
    manifest = json.loads((ROOT / "visuals/provenance.json").read_text())
    for item in manifest["assets"]:
        path = ROOT / item["path"]
        assert path.is_file(), item["path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], item["path"]
    for path in (ROOT / "visuals").rglob("*.svg"):
        ET.parse(path)
    for path in ROOT.rglob("*.md"):
        assert "python -m evidence.lodestar." not in path.read_text(), str(path)


def main() -> None:
    checks = [
        check_visual_manifest_and_svg,
        check_documented_python_modules,
        check_hardware_publication_hashes,
        check_internal_markdown_links,
        check_internal_html_refs,
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
        check_portfolio_guardrails,
    ]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")
    print(f"PASS {len(checks)} repository engineering checks")


if __name__ == "__main__":
    main()
