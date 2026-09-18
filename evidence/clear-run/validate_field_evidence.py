"""Validate the public Clear Run field-evidence snapshot and mission verification contract."""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    snapshot = json.loads((HERE / "field_trial_snapshot.json").read_text(encoding="utf-8"))
    matrix = json.loads((HERE / "mission_verification_matrix.json").read_text(encoding="utf-8"))

    events = snapshot["structured_rgb_events"]
    assert snapshot["video_evidence"]["unique_videos"] == 8
    assert snapshot["video_evidence"]["channels"] == {"RGB": 5, "IR": 3}
    assert events["events"] == 12
    assert events["class_count"] == 8
    assert len(events["reported_classes"]) == 8
    assert events["confidence"] == {
        "min": 0.5488,
        "mean": 0.7125,
        "max": 0.8887,
        "meaning": "model confidence; not calibrated probability or accuracy",
    }
    assert events["altitude_agl_m"] == {"min": 1.176, "mean": 2.069, "max": 2.334}
    assert "geolocation accuracy against surveyed target positions" in snapshot["not_established"]

    stages = {stage["id"]: stage for stage in matrix["stages"]}
    assert len(stages) == 9
    assert stages["CR-01"]["status"] == "demonstrated"
    assert stages["CR-02"]["status"] == "demonstrated"
    for stage_id in ("CR-03", "CR-05", "CR-06", "CR-08", "CR-09"):
        assert stages[stage_id]["status"] == "open_measurement"
    assert stages["CR-07"]["status"] == "development"

    forbidden_complete = {"validated", "complete", "closed", "operational"}
    for stage in stages.values():
        if stage["id"] not in {"CR-01", "CR-02"}:
            assert stage["status"] not in forbidden_complete

    print("PASS Clear Run field-evidence snapshot and mission verification contract.")


if __name__ == "__main__":
    main()
