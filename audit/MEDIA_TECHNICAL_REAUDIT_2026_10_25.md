# Media technical re-audit — 25 October 2026

**Scope:** public portfolio images, 6 withdrawn editorial cards and 12 unapproved review sheets. Based on source-linked GitHub objects and inspection of embedded original bitmaps / project records. This is a provenance, technical-claim and composition-content check, **not** a complete browser rendering or a formal release-clearance decision.

## Release decision

**HOLD external promotion of the 12 review sheets.** The original six image-bearing cards use unaltered source bitmaps, but honest bitmap provenance does not itself validate their accompanying system claims. Six further SVGs are workflow *schematics*, not real photos, product screenshots or observed outputs.

| Severity | Finding | Required correction |
|---|---|---|
| HIGH | **Clear Run photographed vs described rover baseline.** In the private project manuscript, `.../internal/analysis/final/tikz/photos/rover.jpg` visibly shows a **wheeled** collector with acrylic ramp/enclosure. The current portfolio says the latest platform is **tracked/skid-steer**, based on project-lead/team reporting. These may be different hardware revisions, but no build ID, dates, release-approved tracked image or as-tested configuration mapping is attached. | Do **not** caption the wheeled photo as a tracked rover or show it as proof of latest as-tested configuration. Freeze release-safe side-by-side revision record first. |
| HIGH | **GCS UI mistaken for mission evidence.** The public `visuals/autonomy-edge-ai/clear-run/gcs_integration.png` displays a real GCS **bench/disconnected state** (drone, camera and ground agent disconnected; zero detected objects). It demonstrates the interface exists, **not** live integrated tasking or pickup. The screenshot also includes recognizable aerial-map content requiring public-release assessment. | Label as bench/interface UI, never a successful active mission or operator evidence; do not reuse map crop without release review. |
| HIGH | **Different experimental denominators.** 28/30, 27/30, 38/42 collection tasks and 15 daytime + 15 after-dark missions refer to unjoined campaign records. | No common end-to-end reliability KPI until one signed trial ledger maps campaign, hardware revision, task/mission outcome and intervention. |
| MEDIUM | `mission_verification_matrix.json` is stamped September 18, and its physical-capture stage says “development”; October source reports a built collector and integrated mission demonstration. | Preserve September record, label **historical**, and use the October status page for current claims. Do not silently rewrite the older evidence. |
| MEDIUM | The i-MSHA authentic Chromium screenshot is **archived development UI**, with a visible red **“1 Issue”** development badge. | Preserve pixels and disclose development state; avoid “tested successfully” or production-dashboard inference. |
| MEDIUM | Six no-photo workflow sheets are generic evidence schematics, not product media. | Keep as technical appendices; prioritize authentic screen/test records over decorative stage boxes. |
| MEDIUM | Older Clear Run architecture drawings and the historical Mecanum code reflect an earlier configuration and do not establish later tracked-platform wiring or ROS deployment. | Version-label drawings and avoid reusing them to imply the installed latest hardware configuration. |

## Asset-level review (12 review sheets)

| Card | Authentic evidence | Result | Release gate |
|---|---|---|---|
| [TIR-FOD](../visuals/review-2026/tir-fod.svg) | Real airborne UAV; public 3,499-source-frame, 5,593-annotation and 29-training-run records | **CONDITIONAL:** photo/source genuine; no field accuracy KPI implied | State model/Jetson configuration for any latency claim |
| [Super Mushshak](../visuals/review-2026/super-mushshak.svg) | Real installed Dynon cockpit and actual flight cockpit photographs | **CONDITIONAL:** two photographs are from one historical configuration, not two independent avionics configurations | Keep Dynon/Garmin evaluation paths distinct; period/photo permissions |
| [Counter-UAS](../visuals/review-2026/counter-uas.svg) | Constructed camera mount and actual outdoor detector capture | **CONDITIONAL:** Phase-I visual tracking only | Training-scale numbers archive-reported; no operational range or false-alarm proof |
| [IN-ARCP](../visuals/review-2026/inarcp.svg) | Actual R22 plotted `P_d` versus SCR and post-onset guard study | **CONDITIONAL:** simulation/research curves, not radar deployment | Preserve R22 configuration/experiment and avoid certification language |
| [Multi-UAV SAR](../visuals/review-2026/multi-uav-sar.svg) | Actual command-loss simulation plot (24 synthetic cases and 12 terrain maps) | **CONDITIONAL:** original plot; 640 simulated SITL flights are a separate study count | Do not suggest the plotted curves summarize all 640 flights |
| [i-MSHA](../visuals/review-2026/i-msha.svg) | Archived Chromium UI regression capture | **REVISE:** real screenshot with visible developer issue badge | Disclose dated preproduction state; no clean-test claim |
| [Lodestar](../visuals/review-2026/lodestar.svg) | No screenshot; staged retrieval-assessment workflow | **SCHEMATIC:** private historical corpus/test counts | Label 209/2,945/34 as dated source reports, not fresh public reruns |
| [JobLooper](../visuals/review-2026/joblooper.svg) | No screenshot; designed approval pipeline | **SCHEMATIC:** source architecture only | Replace with actual output diff/CLI capture when releasable |
| [Adversarial Review](../visuals/review-2026/adversarial-review.svg) | No screenshot; independent reviewer workflow | **SCHEMATIC:** not an actual completed review | Replace with redacted real audit/test excerpt |
| [BuildSignal AI](../visuals/review-2026/buildsignal.svg) | No screenshot; editorial process diagram | **SCHEMATIC:** not a hosted service UI | Use actual private-app screen, subject to public release |
| [Clear Run MBSE](../visuals/review-2026/mbse.svg) | Flow schematic; bounded telemetry replay is genuine test evidence | **SCHEMATIC:** not a current as-built ground platform diagram | Feature failure/rejection fixture and exact message behavior instead |
| [ATLAS HPC](../visuals/review-2026/atlas.svg) | No screenshot; research job workflow | **SCHEMATIC:** 22-node count leadership-reported | Add sanitized SLURM/job output before marketing as active-system media |

## Claims blocked from hero visuals

- Poster-only `80,840` total images, undefined `88.8% RGB`/`86% IR accuracy`, `44 ms` end-to-end inference, `<=50 ms` comms and `0.31 m` target-position accuracy.
- `28/30 = 93.3%` pickup success, `38/42 = 90.5%` storage/retention and `30` missions must remain separate author-reported observations pending campaign linkage. **38/42 = 90.48%, not end-to-end mission reliability.**
- Neither formal TRL 4, full-runway 30-minute coverage nor operational airport deployment is independently demonstrated.

## Revised media specification

For LinkedIn: **one engineering statement + one authentic asset + one experiment-bound number + one limitation + link to evidence**. Prefer a clean 16:9 layout; do not bury evidence in 3-column small text. Each photo/image caption must include subsystem, configuration/date (when known), and whether it shows *hardware*, *UI*, *simulation*, *trial capture* or *architecture*. Architecture arrows are **functional/interface intent** until tested; no invented hardware/integration arrows. Keep high-res source pixels untouched; cropping/resizing is allowed if it does not hide outcome/diagnostic information.

## Quantified audit state (not recruiting outcome)

- **12/12** existing review SVGs checked for caption/content against their underlying GitHub evidence class; **6/12** contain real bitmap assets, **6/12** are pure workflow diagrams.
- **0/12** approved as publish-ready by this audit; authenticity, claim validity and external release are separate gates.
- **3/3** publicly featured homepage photographs are genuine project hardware, though the first UAV predates the latest ground prototype.
- **2** high-impact configuration/display ambiguities confirmed by direct source-image inspection (wheeled vs reported tracked; disconnected UI); neither is automatically a claim that a later prototype does not exist.
- **No** fresh image generation, field measurements, automated end-to-end mission trials, recruiter KPIs, mobile browser screenshot tests or release authorization performed.

**Source references:** [current Clear Run case](../domains/01-autonomy-edge-ai/CLEAR_RUN_ENGINEERING_CASE_2026_10.md), [archived Sep verification matrix](../evidence/autonomy_edge_ai/clear_run/mission_verification_matrix.json), [poster audit](CLEAR_RUN_POSTER_CLAIM_AUDIT_2026_10_25.md), [provenance map](../visuals/provenance.json), [review index](../visuals/review-2026/README.md). Private photo references are source locators for authorized review, not public file links.
