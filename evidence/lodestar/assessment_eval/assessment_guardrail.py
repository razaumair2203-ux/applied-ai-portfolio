"""Sanitized pure guardrail logic from Lodestar's structured assessment path.

This module evaluates the output contract around generation; it does not decide legal
correctness. The private product uses the same invariants before assessment output is
displayed or persisted.
"""
from __future__ import annotations

FIVE_STATES = {
    "documented", "arguable_but_weak", "unsupported", "contradicted", "not_applicable"
}
CANONICAL_FIELDS = {
    "status", "whats_weak", "whats_missing", "citation_chunk_ids",
    "used_evidence_ids", "rationale"
}


def refusal(criterion_label: str, *, status: str = "unsupported") -> dict:
    return {
        "status": status,
        "whats_weak": [],
        "whats_missing": [f"Retrievable legal authority for: {criterion_label}"],
        "citation_chunk_ids": [],
        "used_evidence_ids": [],
        "rationale": (
            "Insufficient basis in retrieved sources — no authority was retrieved "
            "for this criterion, so no legal conclusion is asserted."
        ),
    }


def canonicalize(response: dict) -> dict:
    out = {k: response[k] for k in CANONICAL_FIELDS if k in response}
    out.setdefault("whats_weak", [])
    out.setdefault("whats_missing", [])
    out.setdefault("citation_chunk_ids", [])
    out.setdefault("used_evidence_ids", [])
    out.setdefault("rationale", "")
    if out.get("status") not in FIVE_STATES:
        raise ValueError(f"invalid assessment status: {out.get('status')!r}")
    return out


def apply_guardrail(
    response: dict,
    *,
    allowed_chunk_ids: list[str],
    valid_evidence_ids: list[str],
    criterion_label: str,
) -> tuple[dict, list[str], list[str]]:
    """Return (safe_response, dropped_citations, recovered_prefixes).

    Mirrors the private engine's key behavior:
    - no retrieved authority -> refusal before generation can establish a conclusion;
    - exact citations survive;
    - a >=8-character prefix is recovered only when it matches exactly one allowed id;
    - unknown/ambiguous citations are dropped;
    - if every citation disappears, take the refusal path (preserving not_applicable);
    - used evidence ids are filtered to known evidence.
    """
    if not allowed_chunk_ids:
        return refusal(criterion_label), [], []

    resp = canonicalize(response)
    allowed = set(allowed_chunk_ids)
    recovered_ids: list[str] = []
    recovered_prefixes: list[str] = []
    for cid in resp["citation_chunk_ids"]:
        if cid in allowed:
            recovered_ids.append(cid)
            continue
        matches = [a for a in allowed if a.startswith(cid)] if len(cid) >= 8 else []
        if len(matches) == 1:
            recovered_ids.append(matches[0])
            recovered_prefixes.append(cid)
        else:
            recovered_ids.append(cid)

    dropped = [cid for cid in recovered_ids if cid not in allowed]
    surviving = [cid for cid in recovered_ids if cid in allowed]
    if not surviving:
        status = "not_applicable" if resp["status"] == "not_applicable" else "unsupported"
        return refusal(criterion_label, status=status), dropped, recovered_prefixes

    resp["citation_chunk_ids"] = surviving
    valid_evidence = set(valid_evidence_ids)
    resp["used_evidence_ids"] = [
        eid for eid in resp["used_evidence_ids"] if eid in valid_evidence
    ]
    return resp, dropped, recovered_prefixes
