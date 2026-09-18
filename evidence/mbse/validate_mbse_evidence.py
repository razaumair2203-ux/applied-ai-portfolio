#!/usr/bin/env python3
import json
from pathlib import Path

p = Path(__file__).with_name("telemetry_replay_cases.json")
data = json.loads(p.read_text(encoding="utf-8"))

assert data["schema"] == "mbse.telemetry-replay.v1"
assert data["observed_flight_incident"] is False
assert data["formatter_contract"]["max_return_characters"] == 49
assert len(data["cases"]) == 3
assert {c["classification"] for c in data["cases"]} == {"control", "unsafe_accept", "unsafe_substitution"}
assert {r["id"] for r in data["derived_requirements"]} == {"R-COORD", "R-ORIGIN"}
assert "does not establish" in data["claim_boundary"]
print("MBSE telemetry evidence: OK")
