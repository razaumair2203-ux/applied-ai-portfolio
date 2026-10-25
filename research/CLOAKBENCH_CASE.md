# CloakBench — adversarial perception evaluation (research in progress)

**Domain:** AI assurance · adversarial computer vision · measurable failure modes.

**Research question.** When a wearable adversarial patch appears to defeat person detection, is the model actually suppressing the person or merely displacing the bounding box so it misses the annotation?

**Approach.** CloakBench separates **suppression** from **detection displacement**, evaluates attack files against calibrated detector operating points, uses matched-occlusion controls and records per-person scores for scripted downstream analyses.

**Evidence availability:** the working repository is private and the research remains unfinished. A publication-safe experiment package has not yet been released; no private audit is linked as public evidence.

**Status, 25 October 2026:** **Unfinished research snapshot.** The 14 October session audit notes unresolved reproduction steps, unscored trained reference cases and manuscript build issues. No reliable headline effectiveness metric or accepted paper is claimed.

**Role relevance:** failure-mode taxonomy, adversarial robustness, test protocol design and transparent evaluation of perception systems.
