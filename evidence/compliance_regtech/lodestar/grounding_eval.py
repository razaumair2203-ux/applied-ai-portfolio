"""Representative Lodestar retrieval-grounding evaluation.

For each hand-checked query/expected-source pair, test whether hybrid retrieval
surfaces an accepted source in the top-k. This evaluates retrieval grounding;
it does not evaluate downstream LLM answer correctness.

This sanitized script documents the full-system evaluation logic. Running it
requires the private Lodestar eb_core package and corpus/database. For a public
zero-dependency check of the published pure retrieval-control logic, run
`python -m evidence.compliance_regtech.lodestar.public_smoke_test` from the repository root.
"""

from __future__ import annotations

import json
import pathlib

from eb_core.db import connection
from eb_core.embeddings import get_embedding_provider
from eb_core.retrieval import hybrid_search

HERE = pathlib.Path(__file__).parent


def evaluate(pairs_path: pathlib.Path, *, gate: float = 0.10) -> dict:
    spec = json.loads(pairs_path.read_text(encoding="utf-8"))
    k = spec["k"]
    provider = get_embedding_provider()
    failures = []

    with connection() as conn:
        for pair in spec["pairs"]:
            results = hybrid_search(
                conn,
                provider,
                pair["q"],
                k=k,
                visa_class=[pair["visa"]],
            )
            hit = any(
                any(
                    marker in (result.citation_label or "")
                    or marker == (result.section_label or "")
                    or marker in (result.section_label or "")
                    for marker in pair["accepted"]
                )
                for result in results
            )
            if not hit:
                failures.append(
                    {
                        "query": pair["q"],
                        "accepted": pair["accepted"],
                        "retrieved": [
                            f"{r.citation_label} §{r.section_label}" for r in results
                        ],
                    }
                )

    total = len(spec["pairs"])
    error_rate = len(failures) / total
    return {
        "pairs": total,
        "top_k": k,
        "failures": failures,
        "error_rate": error_rate,
        "gate": gate,
        "gate_passed": error_rate < gate,
    }


if __name__ == "__main__":
    result = evaluate(HERE / "grounding_pairs.json")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["gate_passed"] else 1)
