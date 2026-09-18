# TIR-FOD / Jetson deployment evidence boundary

The earlier portfolio wording made the historical 25.0 FPS TensorRT / 15.6 FPS end-to-end figures sound more reproducible than the retained evidence allows.

## What is actually retained

The historical flight-test record supports:

- an **author-confirmed 10-run summary** of 25.0 FPS TensorRT-stage throughput;
- an **author-confirmed 10-run summary** of 15.6 FPS end-to-end, range 15.07–16.0 FPS;
- a retained runtime display showing 25.12 FPS TensorRT and 15.07 FPS end-to-end;
- author-confirmed Jetson Orin Nano operation in 15 W nvpmodel mode;
- reported Jetson module draw of 11–12 W, two cameras at about 4 W total, and a broader non-propulsion system total around 17 W (16–18 W range);
- reported 55–70 °C device temperature range.

The raw per-run logs and historical TensorRT engine were **not retained**. The historical checkpoint cannot be identified defensibly after the fact.

Therefore this portfolio does **not** publish a reconstructed 10-row CSV, does not describe the historical values as publicly recomputable, and does not infer a checkpoint name from FPS or engine size.

## Machine-readable status

[`historical_measurement_status.json`](historical_measurement_status.json) records exactly which facts are retained and which evidence is missing.

Run:

```bash
python evidence/tir-fod/deployment/validate_historical_measurement.py
```

The check enforces the evidence boundary; it deliberately cannot recreate data that does not exist.

## How future/named-checkpoint measurement is made reproducible

[`named_checkpoint_protocol.json`](named_checkpoint_protocol.json) publishes the measurement contract developed for a named Jetson checkpoint:

- fixed 520-frame held-out input set;
- 30 warm-up frames;
- at least five repeated runs, ten preferred;
- CUDA-synchronized inference timing;
- telemetry in a separate `tegrastats` process;
- engine/checkpoint hashes;
- refusal to mix engines or silently accept incomplete runs;
- across-run statistics computed over run means;
- inference-only benchmarking kept separate from live capture/decode/inference timing.

When named-checkpoint result logs are returned and verified, they can be published as a separate evidence class. They must not be presented as reconstruction of the historical flight engine.
