"""Zero-dependency Lodestar reliability regression.

These checks are distilled from invariants exercised in the working private system and
run only against the public sanitized implementation. They complement, rather than
replace, the PostgreSQL/pgvector fixture and the adversarial assessment evaluation.
"""
from __future__ import annotations

from evidence.compliance_regtech.lodestar.assessment_eval.assessment_guardrail import apply_guardrail, canonicalize
from evidence.compliance_regtech.lodestar.hybrid_retrieval import RetrievalResult, _filter_clause, _rrf
from evidence.compliance_regtech.lodestar.legal_chunking import chunk_cfr
from evidence.compliance_regtech.lodestar.rerank import authority_rerank, identity_rerank


def result(chunk_id: str, weight: int, score: float, source_type: str = "cfr") -> RetrievalResult:
    return RetrievalResult(
        chunk_id=chunk_id,
        document_id="doc",
        citation_label=f"cite-{chunk_id}",
        title="fixture",
        source_type=source_type,
        binding_weight=weight,
        section_label=None,
        chunk_text="fixture",
        is_non_precedent=(source_type == "aao_nonprecedent"),
        score=score,
    )


def check_rrf_overlap() -> None:
    scores = _rrf(["a", "b", "c"], ["b", "a", "d"])
    assert scores["a"] > scores["c"] and scores["b"] > scores["d"]


def check_rrf_top_of_both() -> None:
    scores = _rrf(["x", "y"], ["x", "z"])
    assert max(scores, key=scores.get) == "x"


def check_authority_near_tie() -> None:
    binding = result("binding", 1, 0.50, "statute")
    nonprecedent = result("nonprecedent", 4, 0.50, "aao_nonprecedent")
    assert authority_rerank([nonprecedent, binding])[0].chunk_id == "binding"


def check_relevance_can_beat_authority() -> None:
    binding = result("binding", 1, 0.10, "statute")
    nonprecedent = result("nonprecedent", 4, 0.90, "aao_nonprecedent")
    assert authority_rerank([binding, nonprecedent])[0].chunk_id == "nonprecedent"


def check_identity_rerank() -> None:
    items = [result("a", 2, 0.3), result("b", 1, 0.9)]
    assert [r.chunk_id for r in identity_rerank(items)] == ["a", "b"]


def check_metadata_filters() -> None:
    clause, params = _filter_clause(["eb1a"], ["awards"])
    assert "visa_class" in clause and "criterion_tags" in clause
    assert params == {"visa_class": ["eb1a"], "criterion_tags": ["awards"]}


def check_structure_aware_chunking() -> None:
    text = """Preamble with enough text to remain a meaningful chunk.

(i) First criterion text with enough content to represent a section.
(ii) Second criterion text with enough content to represent another section.
"""
    labels = [chunk.section_label for chunk in chunk_cfr(text)]
    assert "(i)" in labels and "(ii)" in labels


def check_hallucinated_citation_refuses() -> None:
    safe, dropped, _ = apply_guardrail(
        {
            "status": "documented",
            "citation_chunk_ids": ["invented-source"],
            "used_evidence_ids": ["ev-1"],
            "rationale": "fixture",
        },
        allowed_chunk_ids=["11111111-1111-1111-1111-111111111111"],
        valid_evidence_ids=["ev-1"],
        criterion_label="fixture",
    )
    assert dropped == ["invented-source"]
    assert safe["status"] == "unsupported"
    assert safe["citation_chunk_ids"] == []
    assert "insufficient basis" in safe["rationale"].lower()


def check_unknown_evidence_id_removed() -> None:
    cid = "22222222-2222-2222-2222-222222222222"
    safe, _, _ = apply_guardrail(
        {
            "status": "documented",
            "citation_chunk_ids": [cid],
            "used_evidence_ids": ["ev-valid", "ev-invented"],
            "rationale": "fixture",
        },
        allowed_chunk_ids=[cid],
        valid_evidence_ids=["ev-valid"],
        criterion_label="fixture",
    )
    assert safe["used_evidence_ids"] == ["ev-valid"]


def check_noncanonical_authority_fields_removed() -> None:
    response = canonicalize(
        {
            "status": "arguable_but_weak",
            "citation_chunk_ids": [],
            "used_evidence_ids": [],
            "rationale": "fixture",
            "approval_probability": 0.91,
            "score": 91,
        }
    )
    assert "approval_probability" not in response and "score" not in response


def check_invalid_state_rejected() -> None:
    try:
        canonicalize({"status": "strong_pass"})
    except ValueError:
        return
    raise AssertionError("invalid state was accepted")


def main() -> None:
    checks = [
        check_rrf_overlap,
        check_rrf_top_of_both,
        check_authority_near_tie,
        check_relevance_can_beat_authority,
        check_identity_rerank,
        check_metadata_filters,
        check_structure_aware_chunking,
        check_hallucinated_citation_refuses,
        check_unknown_evidence_id_removed,
        check_noncanonical_authority_fields_removed,
        check_invalid_state_rejected,
    ]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")
    print(f"PASS {len(checks)} Lodestar reliability-regression invariants")


if __name__ == "__main__":
    main()
