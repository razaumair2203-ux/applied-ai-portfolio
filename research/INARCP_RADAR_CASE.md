# IN-ARCP: keeping radar false alarms in check in spiky clutter

Open-source detection maths and software that hold radar false-alarm rates at their design value in sea and ground clutter.

## Why it matters

Sea and ground clutter is spiky, so standard detectors raise far more false alarms than designed. Operators then lose trust, or thresholds are raised until real targets are missed.

## What I did

- **Led** the research as lead author, with four co-authors.
- **Wrote** all of the software, released as an MIT-licensed `pip` package.
- **Developed** innovation-normalized detection with conformal thresholds for compound-Gaussian clutter.
- **Analysed** how persistent targets mask themselves, and designed a slow-time guard against it.
- **Tested** on real IPIX sea-clutter data and real 77 GHz automotive radar interference.

## Results

- Conformal thresholds kept false alarms at **0.73–1.47× nominal** for 12 of 13 statistics, down to **10⁻⁴**.
- **10 of 11** model-based rules exceeded 2× nominal, some by up to **60×**.
- An 8-pulse guard raised mean detection from **0.24 to 0.82** at 10 dB signal-to-clutter ratio.
- With real 77 GHz interference, certified clipping cost **6.4 dB** of SCR.
- Negative results are reported openly, including self-masking at 48 looks.

## How it works

Each new sample is normalized by its prediction error from recent history. A conformal threshold, calibrated on clutter-only data, sets the false-alarm rate from data rather than from an assumed clutter model.

## Status

Manuscript prepared for IEEE Transactions on Radar Systems; software v0.3.0 public (Sep 2026).

## Links

- [IN-ARCP on GitHub](https://github.com/razaumair2203-ux/inarcp)

[Back to research](README.md) · [Back to portfolio](../README.md)
