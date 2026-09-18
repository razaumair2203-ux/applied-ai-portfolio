"""Representative source from Lodestar.

Deterministic reranking of fused retrieval results. Authority is applied as a
small bounded multiplier on the fused retrieval score rather than replacing relevance.
"""

from __future__ import annotations

from typing import Callable, Sequence

from .hybrid_retrieval import RetrievalResult

Reranker = Callable[[Sequence[RetrievalResult]], list[RetrievalResult]]

_AUTHORITY_WEIGHT = 0.05


def authority_rerank(results: Sequence[RetrievalResult]) -> list[RetrievalResult]:
    """Apply a small authority-weighted multiplier to fused relevance scores."""

    def keyfn(result: RetrievalResult) -> float:
        authority_multiplier = 1.0 + (6 - result.binding_weight) * _AUTHORITY_WEIGHT
        return result.score * authority_multiplier

    return sorted(results, key=keyfn, reverse=True)


def identity_rerank(results: Sequence[RetrievalResult]) -> list[RetrievalResult]:
    """No-op reranker used for tests and ablation."""
    return list(results)
