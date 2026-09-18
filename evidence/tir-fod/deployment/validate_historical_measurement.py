"""Validate the public historical Jetson evidence boundary.

This does NOT fabricate missing per-run logs or recompute an unavailable historical mean.
It ensures the retained summary is internally bounded and that the public record explicitly
marks what cannot be independently reproduced.
"""
from __future__ import annotations
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent

def main() -> None:
    rec=json.loads((HERE/"historical_measurement_status.json").read_text(encoding="utf-8"))
    assert rec["run_count"] == 10
    hist=rec["historical_summary"]
    assert hist["tensorrt_stage_fps"]["mean"] == 25.0
    assert hist["end_to_end_fps"] == {"min":15.07,"mean":15.6,"max":16.0}
    assert hist["end_to_end_fps"]["min"] <= hist["end_to_end_fps"]["mean"] <= hist["end_to_end_fps"]["max"]
    prov=rec["provenance"]
    assert prov["raw_per_run_logs_retained"] is False
    assert prov["deployed_tensorrt_engine_retained"] is False
    assert prov["historical_checkpoint_identifiable"] is False
    assert prov["deterministic_recomputation_possible"] is False
    power=rec["power_thermal"]
    assert power["jetson_module_w_range"] == [11,12]
    assert power["two_cameras_total_w"] == 4
    assert power["broader_non_propulsion_system_total_w"]["range"] == [16,18]
    print("PASS historical Jetson evidence boundary: exact summaries retained without claiming missing raw-log reproducibility.")

if __name__=="__main__":
    main()
