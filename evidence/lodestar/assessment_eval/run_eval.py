"""Run the public Lodestar structured-assessment adversarial evaluation."""
from __future__ import annotations
import json
from pathlib import Path

from .assessment_guardrail import apply_guardrail, FIVE_STATES

HERE=Path(__file__).resolve().parent
FORBIDDEN_AUTHORITY_KEYS=("score","probability","percent","likelihood","approval_chance")


def has_forbidden_key(obj) -> bool:
    if isinstance(obj, dict):
        return any(any(token in k.lower() for token in FORBIDDEN_AUTHORITY_KEYS) for k in obj) or any(has_forbidden_key(v) for v in obj.values())
    if isinstance(obj, list):
        return any(has_forbidden_key(v) for v in obj)
    return False


def main() -> None:
    spec=json.loads((HERE/"evaluation_cases.json").read_text(encoding="utf-8"))
    total=len(spec["cases"])
    passed=0
    schema_rejected=0
    dropped_total=0
    recovered_total=0
    refusals_expected=0
    refusals_correct=0

    for case in spec["cases"]:
        exp=case["expected"]
        try:
            safe,dropped,recovered=apply_guardrail(
                case["model_response"],
                allowed_chunk_ids=case["allowed_chunk_ids"],
                valid_evidence_ids=case["valid_evidence_ids"],
                criterion_label=case["criterion_label"],
            )
        except ValueError:
            assert exp.get("schema_rejected") is True, case["id"]
            schema_rejected += 1
            passed += 1
            print(f"PASS {case['id']} schema rejection")
            continue

        assert not exp.get("schema_rejected"), case["id"]
        assert safe["status"] in FIVE_STATES
        assert safe["status"] == exp["status"], (case["id"],safe)
        assert safe["citation_chunk_ids"] == exp["citations"], (case["id"],safe)
        assert safe["used_evidence_ids"] == exp["used_evidence_ids"], (case["id"],safe)
        assert len(dropped) == exp.get("dropped",0), (case["id"],dropped)
        assert len(recovered) == exp.get("recovered",0), (case["id"],recovered)
        assert not has_forbidden_key(safe), (case["id"],safe)
        assert all(cid in case["allowed_chunk_ids"] for cid in safe["citation_chunk_ids"])
        assert all(eid in case["valid_evidence_ids"] for eid in safe["used_evidence_ids"])

        expected_refusal=exp.get("refusal",False)
        if expected_refusal:
            refusals_expected += 1
            is_refusal="insufficient basis" in safe["rationale"].lower() and not safe["citation_chunk_ids"]
            refusals_correct += int(is_refusal)
            assert is_refusal, (case["id"],safe)

        dropped_total += len(dropped)
        recovered_total += len(recovered)
        passed += 1
        print(f"PASS {case['id']}")

    assert passed == total
    assert refusals_correct == refusals_expected
    metrics={
        "cases":total,
        "case_pass_rate":passed/total,
        "post_gate_citation_validity":1.0,
        "post_gate_evidence_id_validity":1.0,
        "refusal_contract_accuracy":1.0,
        "hallucinated_or_ambiguous_citations_dropped":dropped_total,
        "unique_prefixes_recovered":recovered_total,
        "schema_rejections":schema_rejected,
        "semantic_legal_correctness_measured":False,
    }
    print(json.dumps(metrics,indent=2))
    print("PASS Lodestar structured-assessment output contract evaluation.")


if __name__=="__main__":
    main()
