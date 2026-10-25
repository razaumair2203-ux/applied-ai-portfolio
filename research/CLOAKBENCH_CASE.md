# CloakBench: do adversarial T-shirts hide people or just move the box?

A measurement protocol for wearable adversarial patches against person detectors.

## Why it matters

Security teams rely on published "evasion" rates for adversarial clothing. If those rates count a shifted box as a missed person, the threat is overstated.

## What I did

- **Supervised** the student research, following our 2025 TK-Patch paper (IEEE ICoDT2).
- **Framed** the core question: suppression (person vanishes) versus displacement (box moves off the label).
- **Guided** the test protocol: calibrated detector thresholds and matched-occlusion controls.
- **Guided** a review of evaluation protocols across **32** published papers.

## Results (pilot)

- **35.7%** of targets were scored as evaded, yet **99.0%** of those still had a person box.
- Real printed patches correspond to a patch scale of **k = 0.183**; the common k = 0.3 protocol uses **2.7×** the area of any real print.

## Status

Research in progress; manuscript in preparation.

## Links

- [TK-Patch, IEEE ICoDT2 2025](https://doi.org/10.1109/ICoDT269104.2025.11360694)

[Back to research](README.md) · [Back to portfolio](../README.md)
