# Public portfolio restructuring — baseline and measured after-state

**Audit:** 25 October 2026. **Scope:** the public repository `razaumair2203-ux/applied-ai-portfolio`, compared before and after the homepage restructuring. This is a *structure and provenance* audit, not a claim of improved hiring outcomes.

## Reproducible structural KPIs

| Metric | Before | After | Calculation |
|---|---:|---:|---|
| Landing-page words | 1,933 | 810 | Unicode whitespace-token count; **58.1% fewer** |
| Landing-page characters | 19,985 | 8,517 | UTF-8 source characters; **57.4% shorter** |
| Headings (H1–H3) | 21 | 7 | Direct Markdown headings; fewer nesting decisions |
| Selected project case links directly present | 8/12 | 12/12 | Exact evidence-case filename references in the README; **+4 cases / +33.3 percentage points coverage** |
| First flagship-case link position | Character 1,796 | Character 864 | 1-based reader-position proxy; **51.9% earlier** |
| New photo-authentic editorial media linked | 0 | 4 | Count `visuals/editorial/*.svg` references |
| Outdated configuration/recovery phrases on landing | 5 | 0 | Literal `Mecanum`, `developing physical recovery`, `final physical-retention closure remains open` and `IEEE Access revision in progress` |
| Broken local README links and embedded photo refs | Not separately counted before | 0 | All relative Markdown and HTML image references checked against current repository Git tree |
| New editorial cards with exact source-pixel fidelity | — | 4/4 | Embedded base64 image bytes matched the indicated existing Git blob file's base64 verbatim; **five** source images total |

The selected 12 entry points are Clear Run, Super Mushshak, Counter-UAS, IN-ARCP, multi-UAV SAR, i-MSHA, Lodestar, JobLooper, BuildSignal AI, Adversarial Review Lite, ATLAS and CloakBench. This is **curated homepage coverage**, not an assertion that every private or archived repository should be public or featured.

## Source-only media control

| New card | Actual image source | Data-integrity check |
|---|---|---|
| [Clear Run](../visuals/editorial/clear-run-autonomy-2026.svg) | `visuals/autonomy-edge-ai/tir-fod/airborne_platform.png` | Embedded source base64 identical, actual Phase-I UAV |
| [Super Mushshak](../visuals/editorial/super-mushshak-systems-2026.svg) | `visuals/assurance-digital-engineering/super-mushshak/dynon-skyview-installed-prototype.jpg` | Embedded source base64 identical, real cockpit |
| [Counter-UAS](../visuals/editorial/counter-uas-physical-ai-2026.svg) | `visuals/autonomy-edge-ai/counter-uas/phase1_original_mount.jpg` plus `outdoor_detection.png` | Both embedded sources identical, real mount/trial |
| [i-MSHA](../visuals/editorial/i-msha-product-engineering-2026.svg) | `visuals/compliance-regtech/i-msha/dashboard-regression.png` | Embedded source base64 identical, real regression capture |

Photos/trial screenshots were inspected as original images. **Layout and typography were reviewed structurally as SVG source, but no independently rasterized SVG screenshot was available in this run.** Final marketing approval should follow a human visual inspection of each exported card at its intended display size.

**Architecture check:** the Clear Run media and current engineering case order sensing → target event/geolocation → supervised GCS handling → ground collection → evidence/retention. There is no claim that one pictured UAV proves the current tracked rover, nor that archived Mecanum software evidence is the installed hardware baseline. Mission/pickup aggregates are labeled team-reported and not conjoined into a false success rate.

**What these KPIs do *not* measure:** LinkedIn reach, technical-leader engagement, recruiter response, interview rate, peer review, deployment reliability, media accessibility across every browser, or university/public-release clearance. Establish these separately before any marketing ROI claim.

## Traceability and next verification

The previous homepage is archived at [the frozen 25 October baseline](../archive/README_2026-10-25_before_repositioning.md). The current Clear Run case is [October engineering case](../domains/01-autonomy-edge-ai/CLEAR_RUN_ENGINEERING_CASE_2026_10.md). Other repository documentation may still need synchronization; an up-to-date homepage does not make every historical page current.
