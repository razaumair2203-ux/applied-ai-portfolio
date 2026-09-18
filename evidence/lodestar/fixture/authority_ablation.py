"""Characterize Lodestar's two-stage authority weighting on the public DB fixture.

This is a mechanistic ablation, not a quality benchmark. It compares:
1) ordinary lexical + vector RRF,
2) four-lane RRF with high-authority lexical/vector lanes,
3) four-lane RRF plus the authority multiplier.

Run with the same pgvector fixture service used by CI:
    python -m evidence.lodestar.fixture.authority_ablation
"""
from __future__ import annotations

import json
import os

import psycopg

from evidence.lodestar.fixture.postgres_fixture_test import DSN, FixtureProvider, setup
from evidence.lodestar.hybrid_retrieval import _hydrate, _lexical, _rrf, _vector
from evidence.lodestar.rerank import authority_rerank


QUERY = "substantial merit and national importance of the endeavor"


def score_by_label(conn, fused: dict[str, float]) -> dict[str, float]:
    ids = sorted(fused, key=fused.get, reverse=True)
    rows = _hydrate(conn, ids, fused)
    return {r.citation_label: r.score for r in rows}


def final_score(result) -> float:
    return result.score * (1.0 + (6 - result.binding_weight) * 0.05)


def main() -> None:
    provider = FixtureProvider()
    with psycopg.connect(os.environ.get("LODESTAR_FIXTURE_DSN", DSN)) as conn:
        setup(conn)
        qvec = provider.embed_query(QUERY)

        lex = _lexical(conn, QUERY, 30, ["eb2_niw"], None)
        vec = _vector(conn, qvec, 30, ["eb2_niw"], None)
        lex_auth = _lexical(conn, QUERY, 30, ["eb2_niw"], None, max_weight=3)
        vec_auth = _vector(conn, qvec, 30, ["eb2_niw"], None, max_weight=3)

        two_lane = _rrf(lex, vec)
        four_lane = _rrf(lex, vec, lex_auth, vec_auth)

        labels_two = score_by_label(conn, two_lane)
        labels_four = score_by_label(conn, four_lane)

        dhan_label = next(k for k in labels_four if "Dhanasar" in k)
        nonprec_label = next(k for k in labels_four if "Non-Precedent" in k)

        two_ratio = labels_two[dhan_label] / labels_two[nonprec_label]
        four_ratio = labels_four[dhan_label] / labels_four[nonprec_label]

        four_ids = sorted(four_lane, key=four_lane.get, reverse=True)
        reranked = authority_rerank(_hydrate(conn, four_ids, four_lane))
        final = {r.citation_label: final_score(r) for r in reranked}
        reranked_ratio = final[dhan_label] / final[nonprec_label]

        # Mechanistic invariants: the high-authority lanes amplify the controlling source,
        # and the final multiplier adds a second authority preference.
        assert four_ratio > two_ratio
        assert reranked_ratio > four_ratio

        report = {
            "query": QUERY,
            "interpretation": "mechanistic fixture ablation; not a retrieval-quality benchmark",
            "two_lane_rrf": {
                "dhanasar_score": labels_two[dhan_label],
                "nonprecedent_score": labels_two[nonprec_label],
                "authority_to_nonprecedent_ratio": two_ratio,
            },
            "four_lane_rrf": {
                "dhanasar_score": labels_four[dhan_label],
                "nonprecedent_score": labels_four[nonprec_label],
                "authority_to_nonprecedent_ratio": four_ratio,
            },
            "four_lane_plus_rerank": {
                "dhanasar_final_score": final[dhan_label],
                "nonprecedent_final_score": final[nonprec_label],
                "authority_to_nonprecedent_ratio": reranked_ratio,
            },
            "conclusion": (
                "The authority policy is materially stronger than a small final rerank nudge: "
                "high-authority candidate lanes already increase the controlling source's RRF "
                "advantage, and the final multiplier increases it again."
            ),
        }
        print(json.dumps(report, indent=2))
        print("PASS Lodestar authority ablation: two-stage authority influence characterized.")


if __name__ == "__main__":
    main()
