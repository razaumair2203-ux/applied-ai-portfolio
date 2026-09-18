"""Validate the repository metadata contract stored in the repository.

This verifies the desired metadata is well-formed. It does not pretend to mutate or
verify GitHub server-side About settings when an administration-capable API is absent.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TOPIC=re.compile(r"^[a-z0-9][a-z0-9-]{0,49}$")

def main() -> None:
    spec=json.loads((ROOT/"docs"/"REPOSITORY_METADATA_CONTRACT.json").read_text(encoding="utf-8"))
    desc=spec["desired_description"]
    topics=spec["desired_topics"]
    assert 1 <= len(desc) <= 350
    assert 1 <= len(topics) <= 20
    assert len(topics) == len(set(topics))
    assert all(TOPIC.fullmatch(topic) for topic in topics)
    license_text=(ROOT/"LICENSE").read_text(encoding="utf-8")
    assert "All rights reserved" in license_text
    assert "Public projects linked from this portfolio retain the licenses" in license_text
    print("PASS repository metadata contract: description/topics/license policy are well-formed.")

if __name__=="__main__":
    main()
