"""Representative DB-backed retrieval integration test from Lodestar.

A small known corpus is ingested, hybrid retrieval is run against it, and the test
asserts that the expected authority appears in the top five results. The working
private repository contains the complete suite and environment bootstrap.
"""

from __future__ import annotations

import pytest

FIXTURES = [
    (
        "cfr",
        "8 CFR § 204.5(h)(3)(ii) [test]",
        "Documentation of membership in associations in the field which require "
        "outstanding achievements of their members, as judged by recognized experts.",
        ["eb1a"],
    ),
    (
        "aao_precedent",
        "Matter of Dhanasar [test]",
        "The petitioner must demonstrate that the proposed endeavor has both "
        "substantial merit and national importance, and that he is well positioned "
        "to advance it.",
        ["eb2_niw"],
    ),
]

QUERY_SET = [
    ("membership requiring outstanding achievement in associations", ["(h)(3)(ii)", "(ii)"]),
    ("substantial merit and national importance of the endeavor", ["Dhanasar"]),
]


@pytest.mark.parametrize("query,accepted", QUERY_SET)
def test_known_query_retrieves_expected_document(seeded_database, query, accepted):
    from eb_core.db import connection
    from eb_core.retrieval import hybrid_search

    provider = seeded_database
    with connection() as conn:
        results = hybrid_search(conn, provider, query, k=5)

    assert results, f"no results for {query!r}"
    hit = any(
        any(
            marker in (result.citation_label or "")
            or marker == (result.section_label or "")
            for marker in accepted
        )
        for result in results
    )
    assert hit, f"none of {accepted!r} appeared in top-5"
