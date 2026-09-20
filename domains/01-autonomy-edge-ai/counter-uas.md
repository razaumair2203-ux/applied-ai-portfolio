# Counter-UAS Phase I — physical AI-vision prototype and multisensor research foundation

**Private technical review available:** [Request review →](https://github.com/razaumair2203-ux/applied-ai-portfolio/issues/new?template=access-counter-uas.yml)

Phase I is a completed **physical drone-detection research prototype**, led by M. Umair Raza as **Principal Investigator**. The work progressed from dataset/model development into a constructed laser–camera sensing mount and preliminary indoor/outdoor trials, using approximately **14,000 training images**, a **1,500-image test set**, **200 training epochs** and 640×640 inputs. Later passive-RF, acoustic and multisensor work remains a separate research direction rather than being back-claimed as completed capability.

## Physical system evidence

<p align="center">
  <a href="https://github.com/razaumair2203-ux/applied-ai-portfolio/issues/new?template=access-counter-uas.yml"><img src="../../visuals/autonomy-edge-ai/counter-uas/phase1_original_mount.jpg" alt="Constructed Counter-UAS Phase-I laser-camera mount" width="49%"></a>
  <a href="https://github.com/razaumair2203-ux/applied-ai-portfolio/issues/new?template=access-counter-uas.yml"><img src="../../visuals/autonomy-edge-ai/counter-uas/phase1_video_mount.jpg" alt="Counter-UAS Phase-I mount shown in the original trial video" width="49%"></a>
</p>

*Authentic Phase-I hardware. Left: the constructed laser–camera mount extracted byte-identically from the original project presentation before publication resizing. Right: the same mount shown in the original project video at 00:34.*

The public images are presentation derivatives only: EXIF orientation correction, proportional resize, JPEG compression and conservative contrast/sharpness adjustment. **No hardware, people, background or scene content was added, removed or regenerated.** The source and output SHA-256 records are published in [hardware provenance](../../evidence/autonomy_edge_ai/counter_uas/hardware_provenance.json).

## Demonstrated detection work

<p align="center">
  <a href="https://github.com/razaumair2203-ux/applied-ai-portfolio/issues/new?template=access-counter-uas.yml"><img src="../../visuals/autonomy-edge-ai/counter-uas/outdoor_detection.png" alt="Outdoor Counter-UAS Phase I detection trial" width="49%"></a>
  <a href="https://github.com/razaumair2203-ux/applied-ai-portfolio/issues/new?template=access-counter-uas.yml"><img src="../../visuals/autonomy-edge-ai/counter-uas/indoor_detection.png" alt="Indoor Counter-UAS Phase I detection trial" width="49%"></a>
</p>

The archived project evidence includes:

- computer-vision drone detection in a physical sensing setup;
- indoor and outdoor experimental trials;
- camera / hardware integration records;
- preserved model-training results and trial imagery;
- original source material catalogued with provenance and hashes.

[![Counter-UAS Phase I training curves](../../visuals/autonomy-edge-ai/counter-uas/training_curves.png)](https://github.com/razaumair2203-ux/applied-ai-portfolio/issues/new?template=access-counter-uas.yml)

## Engineering scope

The engineering value is the **prototype-to-experiment transition**: model development, physical sensing hardware, camera/mount integration, tracking control and real indoor/outdoor trial conditions were brought together under one Phase-I programme. The retained project record shows **manual human-in-loop tracking, centroid-driven automatic single-target tracking, multi-target tracking using a swarm centroid, pan-tilt actuation, and Kalman-filter reduction of centroid jitter**. Experimental-results material records successful single- and multi-target tracking. It is not represented as an operational counter-drone weapon or fielded C-UAS product.

## AI contribution, decisions and limits

The learned component is the YOLO visual detector. Centroid tracking and Kalman filtering are downstream geometric/control processing; the portfolio does not relabel them as additional learned models. This separation makes detector behaviour, tracking stability and physical integration independently reviewable.

| Engineering choice | Evidence and limitation |
|---|---|
| Camera-based Phase I | Retained indoor/outdoor imagery and physical mount demonstrate an experimental setup; no operational detection-range or weather envelope is established. |
| Separate single-target and swarm-centroid modes | Historical experimental material describes both modes. A group centroid is not evidence of maintaining every target identity. |
| Training curves plus trial images | Useful development evidence, but insufficient for an independently reproducible benchmark without the frozen split, checkpoint and per-condition test records. |
| Phase I versus later sensor fusion | Visual prototype work is completed at research-demonstrator level. Passive RF/acoustic integration remains a separate research direction. |

**Evaluation gap:** public evidence does not contain audited false-alarm rates, per-class precision/recall, tracking error, latency distributions or trial denominators. Those quantities are not inferred from selected screenshots or model confidence. This case supports PI and systems-integration experience in experimental AI hardware; it does not establish operational counter-drone effectiveness.

## Contribution boundary

- **Direct responsibility:** Principal Investigator / research direction, experiment framing and systems-integration oversight.
- **Team-developed work:** model development, prototype construction and trial execution are represented as programme outputs rather than sole-authorship claims.
- **Tracking/control boundary:** the completed Phase-I record supports visual tracking/control integration; it does not establish operational engagement capability, and later RF/acoustic/multisensor or edge/fog/cloud concepts remain separate.
- **Scope boundary:** Phase-I visual detection evidence is separated from later passive-RF, acoustic and multisensor research directions.

## Evidence provenance and programme evolution

The private source archive retains the full-resolution original mount photograph, the original Phase-I trial video and the historical presentation/poster material. The public portfolio now carries publication-sized derivatives of the hardware photograph and video frame alongside the original-size-derived detection outputs and training curves.

[![Counter-UAS programme evolution](../../visuals/autonomy-edge-ai/counter-uas/framework_evolution.svg)](https://github.com/razaumair2203-ux/applied-ai-portfolio/issues/new?template=access-counter-uas.yml)

*Phase I / AI vision is completed evidence. Later RF/acoustic/multisensor stages are research directions, not represented as completed capability.*

## Research evolution

Follow-on work investigates how independently recorded optical, passive-RF and acoustic modalities could be compared and eventually fused while retaining provenance. Those directions are not represented as completed Phase-I capability.

The detailed historical source repository remains private because it contains programme material and original project records.

[Back to domain index](README.md)
