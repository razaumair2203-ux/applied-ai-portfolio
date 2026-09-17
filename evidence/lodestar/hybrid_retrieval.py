"""Sanitized representative source from Lodestar.

Hybrid lexical + vector retrieval with RRF fusion and authority-aware candidate lanes.
"""

from __future__ import annotations

from dataclasses import dataclass

_RRF_K = 60


@dataclass
class RetrievalResult:
    chunk_id: str
    document_id: str
    citation_label: str
    title: str
    source_type: str
    binding_weight: int
    section_label: str | None
    chunk_text: str
    is_non_precedent: bool
    score: float
    url: str | None = None


def _rrf(*ranked_lists: list[str]) -> dict[str, float]:
    scores: dict[str, float] = {}
    for ranked in ranked_lists:
        for rank, chunk_id in enumerate(ranked):
            scores[chunk_id] = scores.get(chunk_id, 0.0) + 1.0 / (_RRF_K + rank + 1)
    return scores


def hybrid_search(conn, provider, query: str, *, k: int = 10, pool: int = 30, reranker=None):
    if reranker is None:
        from .rerank import authority_rerank
        reranker = authority_rerank

    query_vec = provider.embed_query(query)
    lexical_ids = _lexical(conn, query, pool)
    vector_ids = _vector(conn, query_vec, pool)

    # Separate high-authority lanes keep controlling sources in the candidate pool.
    lexical_authority = _lexical(conn, query, pool, max_weight=3)
    vector_authority = _vector(conn, query_vec, pool, max_weight=3)

    fused = _rrf(lexical_ids, vector_ids, lexical_authority, vector_authority)
    if not fused:
        return []

    candidate_ids = sorted(fused, key=lambda cid: fused[cid], reverse=True)[: max(k * 3, 20)]
    candidates = _hydrate(conn, candidate_ids, fused)
    return reranker(candidates)[:k]


def _lexical(conn, query, k, max_weight=None):
    weight_clause = ""
    params = {"q": query, "k": k}
    if max_weight is not None:
        weight_clause = " AND c.document_id IN (SELECT id FROM documents WHERE binding_weight <= %(mw)s)"
        params["mw"] = max_weight
    rows = conn.execute(
        f"""
        SELECT c.id::text
        FROM chunks c
        WHERE c.tsv @@ websearch_to_tsquery('english', %(q)s){weight_clause}
        ORDER BY ts_rank(c.tsv, websearch_to_tsquery('english', %(q)s)) DESC
        LIMIT %(k)s
        """,
        params,
    ).fetchall()
    return [row[0] for row in rows]


def _vector(conn, query_vec, k, max_weight=None):
    weight_clause = ""
    params = {"vec": query_vec, "k": k}
    if max_weight is not None:
        weight_clause = " AND c.document_id IN (SELECT id FROM documents WHERE binding_weight <= %(mw)s)"
        params["mw"] = max_weight
    rows = conn.execute(
        f"""
        SELECT c.id::text
        FROM chunks c
        WHERE c.embedding IS NOT NULL{weight_clause}
        ORDER BY c.embedding <=> %(vec)s::vector
        LIMIT %(k)s
        """,
        params,
    ).fetchall()
    return [row[0] for row in rows]


def _hydrate(conn, ids: list[str], fused: dict[str, float]):
    if not ids:
        return []
    rows = conn.execute(
        """
        SELECT c.id::text, c.document_id::text, d.citation_label, d.title,
               d.source_type, d.binding_weight, c.section_label, c.chunk_text, d.url
        FROM chunks c JOIN documents d ON d.id = c.document_id
        WHERE c.id = ANY(%(ids)s::uuid[])
        """,
        {"ids": ids},
    ).fetchall()
    by_id = {row[0]: row for row in rows}
    out = []
    for cid in ids:
        row = by_id.get(cid)
        if row:
            out.append(RetrievalResult(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[4] == "aao_nonprecedent", fused[cid], row[8]))
    return out
