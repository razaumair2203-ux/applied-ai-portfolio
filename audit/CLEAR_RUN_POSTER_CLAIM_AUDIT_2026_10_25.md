# Clear Run poster claim audit — 25 October 2026

**Input:** A1 portrait poster supplied by the project lead on 25 October 2026. The poster includes actual hardware/GCS/field imagery, but not a machine-readable trial ledger or independent geolocation reference data.

| Poster claim | Evidence and conflict | External-use decision |
|---|---|---|
| UAV/GCS/rover physical hardware | Photos and earlier project documentation support actual hardware and developed software; latest ground-drive configuration should be frozen explicitly. | **SHOW** authentic photos with source/date attribution. |
| 23 FOD classes | TIR-FOD public dataset documents 23 annotated LWIR object classes. | **SHOW** as dataset scope, not demonstrated field recall. |
| 80,840 images | Poster combines sources/augmentation; independently published base is 3,499 LWIR source frames and 5,593 annotations. | **WITHHOLD** until source/augmentation counts and training splits are reconciled. |
| 88.8% RGB and 86% IR accuracy | Poster does not define denominator or whether this is classification accuracy, object-detection accuracy, precision, recall or campaign-level yield. | **WITHHOLD** as public KPI until metric contract and raw evaluation are present. |
| 44 ms model inference, <=50 ms communications | Poster gives point results without full timing methodology, configuration identity, distributions or synchronized measurements. | **WITHHOLD** as engineering performance claims pending timing logs; may label a single recorded observation with conditions. |
| 0.31 m geolocation result; GPS 3 m comparison | The Oct 14 programme baseline states only an approximate 1 m RMSE scalar was retained and paired surveyed reference coordinates were unavailable. Poster values use a different unverified setup. | **WITHHOLD** public accuracy comparisons until reference pairs are preserved. |
| 'Rover removes it unaided' | Project lead confirms at least one integrated mission demonstration; scope of operator intervention, autonomy during final alignment and repeatability remains to distinguish. | **QUALIFY** as prototype demonstration with human supervision/unknown intervention count. |
| 28 of 30 / 93.3% success | Poster indicates 28/30 field trials; earlier September presentation had 27/30 pickups; Oct14 notes 38/42 retained pickup tasks (90.5%), while Oct22 notes 15 daylight + 15 after-dark missions. These refer to different or insufficiently linked populations. | **WITHHOLD** from headline until campaign identity and outcome ledger reconciled. |
| TRL 4 | No documented independent TRL gate/rationale. | **WITHHOLD** a formal TRL number. |
| ~PKR 1 million cost | The maintained October project cost statement is about US$5,700, which may use a different bill-of-materials/configuration/currency basis. | **WITHHOLD** headline cost until BOM, exchange assumptions and what is included are fixed. |
| Clears 25×400m sector or whole runway in 30 minutes | Appears as a requirement/aim; no matching verified sweep-completion/coverage and retrieval record. | **TARGET**, not performance result. |
| Day/night trials | Oct22 project lead confirms 15 daytime and 15 after-dark missions. | **SHOW** as author-reported campaign activity, not automatically 30 successful unattended recoveries. |
| Integrated-system journal acceptance/status | Oct22 private programme record says manuscript ready but not submitted; the author later reported both papers under consideration on Oct25. | **VERIFY SUBMISSION RECEIPT** before representing the integration paper as editorially under review. |

**Claim boundary:** Prototype integration and mission demonstration are meaningful achievements without conflating team-reported task aggregates, simulated timings, dataset evaluation and validated end-to-end retrieval performance.

**Image boundary:** Crops from the supplied poster are unaltered source-image pixels. The original camera files, their EXIF metadata, any retouching before poster composition and individual author permissions still require independent confirmation before unrestricted external publicity.

[Clear Run case](../domains/01-autonomy-edge-ai/CLEAR_RUN_ENGINEERING_CASE_2026_10.md) · [Public dataset](https://doi.org/10.5281/zenodo.22546586).
