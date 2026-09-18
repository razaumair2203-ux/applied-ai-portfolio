"""Zero-dependency checks for the public Lodestar evidence bundle.

Run from repository root:
    python -m evidence.lodestar.public_smoke_test

These checks validate the published pure retrieval-control logic. They do NOT
reproduce the private 209-document corpus or the recorded 2.9% full-corpus
retrieval-grounding result.
"""

from __future__ import annotations

import json
from pathlib import Path

from .hybrid_retrieval import RetrievalResult, _filter_clause, _rrf
from .legal_chunking import chunk_cfr
from .rerank import authority_rerank


def _result(chunk_id: str, binding_weight: int, score: float) -> RetrievalResult:
    return RetrievalResult(
        chunk_id=chunk_id,
        document_id="doc",
        citation_label=f"cite-{chunk_id}",
        title="fixture",
        source_type="cfr",
        binding_weight=binding_weight,
        section_label=None,
        chunk_text="fixture",
        is_non_precedent=False,
        score=score,
    )


def check_rrf() -> None:
    scores = _rrf(["a", "b", "c"], ["b", "a", "d"])
    assert scores["a"] > scores["c"]
    assert scores["b"] > scores["d"]


def check_authority_rerank() -> None:
    statute = _result("statute", 1, 0.50)
    example = _result("example", 4, 0.50)
    assert authority_rerank([example, statute])[0].chunk_id == "statute"

    weak_statute = _result("weak-statute", 1, 0.10)
    strong_example = _result("strong-example", 4, 0.90)
    assert authority_rerank([weak_statute, strong_example])[0].chunk_id == "strong-example"


def check_filters() -> None:
    clause, params = _filter_clause(["eb1a"], ["membership"])
    assert "visa_class" in clause and "criterion_tags" in clause
    assert params == {
        "visa_class": ["eb1a"],
        "criterion_tags": ["membership"],
    }


def check_structure_aware_chunking() -> None:
    text = """Preamble with enough text to be retained as a meaningful legal chunk.

(i) First criterion text with enough content to represent a section.
(ii) Second criterion text with enough content to represent another section.
"""
    chunks = chunk_cfr(text)
    labels = [chunk.section_label for chunk in chunks]
    assert "(i)" in labels and "(ii)" in labels


def check_frozen_eval_spec() -> None:
    path = Path(__file__).with_name("grounding_pairs.json")
    spec = json.loads(path.read_text(encoding="utf-8"))
    assert spec["k"] == 5
    assert len(spec["pairs"]) == 34
    assert all(pair["accepted"] for pair in spec["pairs"])


def main() -> None:
    checks = [
        check_rrf,
        check_authority_rerank,
        check_filters,
        check_structure_aware_chunking,
        check_frozen_eval_spec,
    ]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")
    print(f"PASS {len(checks)} public Lodestar smoke checks")


if __name__ == "__main__":
    main()
