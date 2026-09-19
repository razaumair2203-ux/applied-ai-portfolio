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
HTML_REF_RE = re.compile(r'(?:href|src)="([^"]+)"')


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
    root = (ROOT / "README.md").read_text(encoding="utf-8")

    # Identity, specialization anchors and programme scale must precede deeper evidence.
    assert root.index("## Four specialization areas") < root.index("## At a glance")
    assert root.index("## At a glance") < root.index("## 1. Autonomous, Embedded & Edge AI")
    assert "Applied AI & Autonomous Systems Engineering Leader" in root
    assert "Officer In Charge Projects / R&D & Systems Engineering Lead" in root

    # The four specialization anchors are an explicit navigation and information architecture contract.
    anchor_pairs = (
        ("autonomy-edge-ai", "## 1. Autonomous, Embedded & Edge AI"),
        ("compliance-regtech", "## 2. Compliance & Regulatory Intelligence"),
        ("practical-agentic-ai", "## 3. Practical Agentic AI Products"),
        ("assurance-digital-engineering", "## 4. AI Assurance, Evaluation & Digital Engineering"),
    )
    previous = -1
    for anchor, heading in anchor_pairs:
        assert f"](#{anchor})" in root, anchor
        assert f'<a name="{anchor}"></a>' in root, anchor
        assert heading in root, heading
        pos = root.index(heading)
        assert pos > previous, heading
        previous = pos

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
        "visuals/autonomy-edge-ai/clear-run/clear_run_detection_to_removal_architecture.webp",
        "visuals/compliance-regtech/i-msha/dashboard-regression.png",
        "visuals/compliance-regtech/lodestar/product-surface.svg",
        "visuals/practical-ai-products/joblooper/dashboard-surface.svg",
        "visuals/practical-ai-products/buildsignal/admin-surface.svg",
        "visuals/assurance-digital-engineering/adversarial-review/audit-report-preview.jpg",
        "visuals/assurance-digital-engineering/ai-evaluation/evaluation_pipeline.svg",
        "visuals/assurance-digital-engineering/super-mushshak/dynon-skyview-installed-prototype.jpg",
        "visuals/autonomy-edge-ai/counter-uas/phase1_original_mount.jpg",
        "profile/AI_BASE_RESUME.md",
        "curated, release-safe technical package or review branch",
    ):
        assert marker in root, marker

    # Prevent regression to the broken three-stream strip or stale external Super Mushshak asset.
    assert "three evidence streams" not in root.lower()
    assert "dynon-cockpit-prototype-sanitized.jpg" not in root
    assert "raw.githubusercontent.com/razaumair2203-ux/Super-Mushshak-Glass-Cockpit-Modification" not in root

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

    mushshak = (ROOT / "domains/04-assurance-digital-engineering/super-mushshak-digital-engineering.md").read_text(
        encoding="utf-8"
    )
    assert "../../visuals/assurance-digital-engineering/super-mushshak/dynon-skyview-installed-prototype.jpg" in mushshak
    assert "dynon-cockpit-prototype-sanitized.jpg" not in mushshak
    assert "raw.githubusercontent.com" not in mushshak

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



def check_portfolio_guardrails() -> None:
    root = (ROOT / "README.md").read_text(encoding="utf-8")

    # Four-area taxonomy is stable; Clear Run MBSE is a cross-cutting Area 4 capability,
    # not a third autonomy flagship.
    assert "**Flagships:** Clear Run / TIR-FOD · Counter-UAS" in root
    assert (
        "**Flagships:** AI Systems Assurance / MBSE · Evaluation-driven AI workflows · "
        "ATLAS GPU/HPC · Super Mushshak digital engineering"
    ) in root
    assert "### AI Systems Assurance / MBSE — Clear Run" in root

    autonomy_index = (ROOT / "domains/01-autonomy-edge-ai/README.md").read_text(encoding="utf-8")
    assurance_index = (ROOT / "domains/04-assurance-digital-engineering/README.md").read_text(encoding="utf-8")
    domain_map = (ROOT / "domains/README.md").read_text(encoding="utf-8")
    assert "primarily classified under [AI Assurance, Evaluation & Digital Engineering]" in autonomy_index
    assert "[AI Systems Assurance / MBSE — Clear Run]" in assurance_index
    area1 = domain_map.split("## 1. Autonomous, embedded and edge AI", 1)[1].split(
        "## 2. Compliance and regulatory intelligence", 1
    )[0]
    area4 = domain_map.split("## 4. AI assurance, evaluation and digital engineering", 1)[1]
    assert "AI Systems Assurance / MBSE" not in area1
    assert "AI Systems Assurance / MBSE — Clear Run" in area4

    # Domain ownership must stay consistent in the public visual/evidence indexes
    # even when the underlying asset paths remain near their originating projects.
    visual_index = (ROOT / "visuals/README.md").read_text(encoding="utf-8")
    visual_autonomy = visual_index.split("## Autonomous, embedded and edge AI", 1)[1].split(
        "## Compliance and regulatory intelligence", 1
    )[0]
    visual_practical = visual_index.split("## Practical AI products", 1)[1].split(
        "## AI assurance and digital engineering", 1
    )[0]
    visual_assurance = visual_index.split("## AI assurance and digital engineering", 1)[1]
    assert "### AI Systems Assurance / MBSE" not in visual_autonomy
    assert "### AI Systems Assurance / MBSE" in visual_assurance
    assert "### Adversarial Review Lite" in visual_practical
    assert "### Adversarial Review Lite" not in visual_assurance

    evidence_index = (ROOT / "evidence/README.md").read_text(encoding="utf-8")
    evidence_autonomy = evidence_index.split("## Autonomous, embedded and edge AI", 1)[1].split(
        "## Compliance and regulatory intelligence", 1
    )[0]
    evidence_practical = evidence_index.split("## Practical AI products", 1)[1].split(
        "## Public source repositories", 1
    )[0]
    evidence_assurance = evidence_index.split("## AI assurance and digital engineering", 1)[1].split(
        "## Practical AI products", 1
    )[0]
    assert "AI Systems Assurance / MBSE" not in evidence_autonomy
    assert "AI Systems Assurance / MBSE" in evidence_assurance
    assert "Adversarial Review Lite" in evidence_practical

    # Clear Run robotics depth must remain visible and must not regress to
    # the old ROS1-only simplification.
    clear_run_case = (ROOT / "domains/01-autonomy-edge-ai/clear-run-tir-fod.md").read_text(encoding="utf-8")
    clear_run_cv = (ROOT / "profile/AI_BASE_RESUME.md").read_text(encoding="utf-8")
    ugv_arch = (ROOT / "visuals/autonomy-edge-ai/clear-run/ugv_architecture.svg").read_text(encoding="utf-8")
    for marker in ("ROS2", "Nav2", "SLAM Toolbox"):
        assert marker in root, marker
        assert marker in clear_run_case, marker
        assert marker in clear_run_cv, marker
        assert marker in ugv_arch, marker
    assert "ROS 1 navigation" not in ugv_arch
    assert "hybrid ROS1/ROS2" in clear_run_case
    assert "national-scale field trials" in root
    assert "patent filing planned after field-trial maturation" in root
    assert "completed national deployment/adoption" in root
    assert "filed/pending/granted IP" in root

    # Counter-UAS and historical aircraft-integration depth must not regress
    # back to detector-only or display-only descriptions.
    counter_uas_case = (ROOT / "domains/01-autonomy-edge-ai/counter-uas.md").read_text(encoding="utf-8")
    public_cv = (ROOT / "profile/AI_BASE_RESUME.md").read_text(encoding="utf-8")
    for marker in ("centroid-driven", "multi-target", "Kalman-filter"):
        assert marker in counter_uas_case, marker
    assert "manual/automatic single/multi-target centroid tracking" in root
    assert "Kalman stabilization" in root
    assert "manual human-in-loop" in counter_uas_case
    assert "centroid-driven automatic single/multi-target tracking" in public_cv
    assert "complete modification wiring harness" in public_cv
    assert "NAV/COM/audio/data interfaces" in public_cv
    assert "aircraft-level retrofit" in root
    assert "customer evaluation" in root

    # Source-derived visuals must be visibly labelled on the landing page.
    assert "Lodestar is a source-derived rendering from the current frontend code" in root
    assert "JobLooper and BuildSignal AI surfaces are source-derived renderings" in root
    assert "These renderings are not presented as original product screenshots." in root

    # Active flagship pages expose dated public-evidence snapshots without rewriting
    # the date/provenance of underlying measurements.
    dated_pages = (
        "domains/01-autonomy-edge-ai/clear-run-tir-fod.md",
        "domains/02-compliance-regtech/i-msha.md",
        "domains/02-compliance-regtech/lodestar.md",
        "domains/03-practical-ai-products/joblooper-jobpilot.md",
        "domains/03-practical-ai-products/buildsignal-ai.md",
        "domains/03-practical-ai-products/adversarial-review-lite.md",
    )
    for rel in dated_pages:
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert "**Public evidence snapshot:** 19 September 2026." in text, rel

    # Landing page must expose an immediate path from claims to inspectable evidence.
    assert "## Inspect the engineering" in root
    for marker in (
        "TIR-FOD reproducibility",
        "Clear Run field/mission evidence",
        "Lodestar retrieval & evaluation",
        "JobLooper source",
        "engineering CI",
        "curated, release-safe technical package or review branch",
    ):
        assert marker in root, marker


def main() -> None:
    checks = [
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
