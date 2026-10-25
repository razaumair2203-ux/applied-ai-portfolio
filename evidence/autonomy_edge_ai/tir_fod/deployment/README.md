# TIR-FOD on Jetson

## What this code shows

- Onboard throughput on the UAV's Jetson Orin Nano, ten-run summary: **25.0 FPS** TensorRT stage, **15.6 FPS** end to end (range 15.07–16.0).
- In night thermal flights, the system detected **27 of 30** debris targets.
- [Measurement record](historical_measurement_status.json) — the throughput summary in machine-readable form.
- [Capture protocol](named_checkpoint_protocol.json) — how future flights log model hashes and per-frame timing.

## How to run

```bash
python evidence/autonomy_edge_ai/tir_fod/deployment/validate_historical_measurement.py
```

Checks the measurement record for internal consistency.

[Back to TIR-FOD code](../README.md) · [Back to portfolio](../../../../README.md)
