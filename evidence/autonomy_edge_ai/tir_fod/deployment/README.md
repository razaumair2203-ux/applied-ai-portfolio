# TIR-FOD / Jetson deployment provenance

This directory records what is retained from the historical Jetson/TensorRT flight measurements and defines the capture protocol for future named-checkpoint runs.

## Historical record

The retained summary records:

- ten-run mean **25.0 FPS TensorRT-stage throughput**;
- ten-run **15.6 FPS end-to-end** with reported range **15.07–16.0 FPS**;
- a retained single runtime display of **25.12 FPS TensorRT / 15.07 FPS end-to-end**;
- reported power and thermal observations from the flight configuration.

## Provenance limits

The following historical artefacts were not retained:

- raw per-run timing logs;
- the exact deployed TensorRT engine;
- a uniquely identifiable historical model checkpoint.

For that reason the historical figures are preserved as system measurements but are not represented as a fully reproducible named-checkpoint benchmark.

The machine-readable record is [historical_measurement_status.json](historical_measurement_status.json).

## Future measurement protocol

[named_checkpoint_protocol.json](named_checkpoint_protocol.json) defines the stronger capture path for subsequent runs, including model/engine hashes, per-frame timing, separated inference and end-to-end measurements, device telemetry and retained run-level data.

```bash
python evidence/autonomy_edge_ai/tir_fod/deployment/validate_historical_measurement.py
```

The validation script checks internal consistency of the retained record; it does not attempt to recreate missing historical data.

[Back to TIR-FOD / Clear Run](../../../../domains/01-autonomy-edge-ai/clear-run-tir-fod.md)
