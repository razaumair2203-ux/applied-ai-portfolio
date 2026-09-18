"""Real PostgreSQL + pgvector integration test for the public Lodestar retrieval code.

Requires:
    LODESTAR_FIXTURE_DSN=postgresql://eb:eb@localhost:5432/eb
    pip install -r evidence/lodestar/fixture/requirements.txt

This intentionally avoids a heavyweight embedding-model download. Fixture documents and
queries use deterministic 1024-dimensional vectors, while the retrieval path itself is
the real published PostgreSQL FTS + pgvector + RRF + hydration + reranking implementation.
"""
from __future__ import annotations

import os
from pathlib import Path

import psycopg

from evidence.compliance_regtech.lodestar.hybrid_retrieval import hybrid_search

HERE = Path(__file__).resolve().parent
DSN = os.environ.get("LODESTAR_FIXTURE_DSN", "postgresql://eb:eb@localhost:5432/eb")


def vec(a: float, b: float, c: float) -> str:
    values = [a, b, c] + [0.0] * 1021
    return "[" + ",".join(str(v) for v in values) + "]"


class FixtureProvider:
    def embed_query(self, query: str) -> str:
        q = query.lower()
        if "membership" in q or "association" in q:
            return vec(1.0, 0.0, 0.0)
        if "national importance" in q or "endeavor" in q:
            return vec(0.0, 1.0, 0.0)
        if "award" in q or "prize" in q:
            return vec(0.0, 0.0, 1.0)
        return vec(1.0, 1.0, 1.0)


def setup(conn: psycopg.Connection) -> None:
    conn.execute((HERE / "schema.sql").read_text(encoding="utf-8"))
    docs = [
        (
            "cfr", "8 CFR § 204.5(h)(3)(ii) [fixture]", "Membership criterion", 2,
            "(ii) Documentation of membership in associations requiring outstanding achievements judged by recognized experts.",
            "(h)(3)(ii)", ["membership"], ["eb1a"], vec(1.0, 0.0, 0.0),
        ),
        (
            "aao_precedent", "Matter of Dhanasar [fixture]", "National interest waiver precedent", 3,
            "The proposed endeavor must have substantial merit and national importance and the petitioner must be well positioned to advance it.",
            "Dhanasar", ["national_importance"], ["eb2_niw"], vec(0.0, 1.0, 0.0),
        ),
        (
            "aao_nonprecedent", "AAO Non-Precedent Example [fixture]", "Non-precedent NIW example", 5,
            "A non-precedent decision discusses substantial merit and national importance in a fact-specific record.",
            "AAO Non-Precedent", ["national_importance"], ["eb2_niw"], vec(0.0, 0.98, 0.02),
        ),
        (
            "cfr", "8 CFR § 204.5(h)(3)(i) [fixture]", "Awards criterion", 2,
            "(i) Documentation of lesser nationally or internationally recognized prizes or awards for excellence.",
            "(h)(3)(i)", ["awards"], ["eb1a"], vec(0.0, 0.0, 1.0),
        ),
    ]
    for source_type, citation, title, weight, text, section, tags, visas, embedding in docs:
        doc_id = conn.execute(
            """INSERT INTO documents(source_type,citation_label,title,binding_weight)
               VALUES (%s,%s,%s,%s) RETURNING id""",
            (source_type, citation, title, weight),
        ).fetchone()[0]
        conn.execute(
            """INSERT INTO chunks(document_id,chunk_text,chunk_index,section_label,
                                  embedding,criterion_tags,visa_class)
               VALUES (%s,%s,0,%s,%s::vector,%s,%s)""",
            (doc_id, text, section, embedding, tags, visas),
        )
    conn.commit()


def assert_contains(results, marker: str) -> None:
    labels = [f"{r.citation_label} {r.section_label or ''}" for r in results]
    assert any(marker in label for label in labels), (marker, labels)


def main() -> None:
    provider = FixtureProvider()
    with psycopg.connect(DSN) as conn:
        setup(conn)

        membership = hybrid_search(
            conn, provider,
            "membership requiring outstanding achievement in associations",
            k=3, visa_class=["eb1a"], criterion_tags=["membership"],
        )
        assert membership
        assert_contains(membership, "(h)(3)(ii)")
        assert all(r.source_type == "cfr" for r in membership)

        niw = hybrid_search(
            conn, provider,
            "substantial merit and national importance of the endeavor",
            k=3, visa_class=["eb2_niw"],
        )
        assert niw
        assert "Dhanasar" in niw[0].citation_label, [r.citation_label for r in niw]
        nonprecedent = next(r for r in niw if r.source_type == "aao_nonprecedent")
        assert nonprecedent.is_non_precedent is True

        awards = hybrid_search(
            conn, provider,
            "nationally recognized prizes or awards for excellence",
            k=3, visa_class=["eb1a"], criterion_tags=["awards"],
        )
        assert awards
        assert_contains(awards, "(h)(3)(i)")

        # Metadata filters must exclude the NIW corpus from an EB-1A-only query.
        filtered = hybrid_search(
            conn, provider, "national importance",
            k=5, visa_class=["eb1a"],
        )
        assert all("Dhanasar" not in r.citation_label for r in filtered)

    print("PASS Lodestar PostgreSQL/pgvector fixture: lexical, vector, filters, RRF, hydration and authority reranking executed.")


if __name__ == "__main__":
    main()
