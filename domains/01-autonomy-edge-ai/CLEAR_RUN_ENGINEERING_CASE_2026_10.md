# Clear Run — integrated airfield robotics and systems engineering
**As of 25 October 2026 · prototype demonstration and active field-research programme**

> **Engineering perspective:** The project is not a standalone FOD detector. It tests the interfaces that convert detection into supervised physical recovery. A fabricated collector and integrated mission demonstration are reported by the project lead; the later tracked/skid-steer drive configuration has not been mapped to the wheeled collector photograph retained in the manuscript. Repeated, independently auditable detection-to-retention performance is not yet established.

[Photo-authentic media card](../../visuals/editorial/clear-run-autonomy-2026.svg) · [Programme maturity summary](CLEAR_RUN_2026-10_STATUS.md) · [Public field-evidence extract](../../evidence/autonomy_edge_ai/clear_run/README.md) · [Released TIR-FOD dataset](https://doi.org/10.5281/zenodo.22546586)

## The actual system boundary

```text
Day/night airborne RGB and passive-LWIR sensing
       |
Onboard detection / FP16 TensorRT / target-event formation
       |
Estimated target geolocation, airframe telemetry, message transmission
       |
Ground control station: target review, operator authorization, task dispatch
       |
Ground collector: local sensing / approach / terminal positioning
       |
Fabricated ramp-and-lift mechanism: physical pickup and retention
       |
Outcome verification, timestamped evidence, failures and operator interventions
```

Each arrow represents an **engineering interface** and therefore a failure or verification boundary. Detection confidence does not establish coordinate accuracy. Coordinate output does not establish task acknowledgement. Reaching the vicinity of an object does not establish correct pickup, and pickup does not establish retained recovery after motion.

### Demonstrated work versus research still open

| Element | Current defensible statement | Next verification obligation |
|---|---|---|
| Thermal perception | Public 23-category LWIR dataset, source lineage, repeated model evaluation, Jetson Orin Nano / TensorRT field work | Generalization under changed acquisition and operating conditions |
| RGB / passive-IR event pipeline | Recorded field frames and event/coordinate outputs; September public event/log batch | Link every event to calibrated truth and full trial denominators |
| Ground control | Purpose-built GCS and tasking/interface evidence | Exact target identity through acknowledge, retry, abort and dispatch |
| Ground hardware | **Fabricated ramp-and-lift collector**, with tracked/skid-steer revision author-reported; current manuscript photo shows a wheeled collection platform. Revision-specific tests and images are not yet linked | Freeze installed hardware/firmware/sensor revisions |
| Mission demonstration | Complete prototype mission **confirmed by project lead** | Preserve synchronized as-tested configuration, event/time chain and independent witness/records |
| Day/night missions | **15 daytime + 15 after-dark** missions in latest author-reported campaign | Session-linked conditions, failures, success denominators and independent audit |
| Physical retention | Earlier October author-reported **38 retained collection outcomes / 42 tasks (90.5%)** | Retained per-task ledger, object conditions, post-capture motion and failure taxonomy |
| Geolocation | Estimates generated; historical approximate 1 m RMSE reported as a scalar | Paired surveyed reference/output locations and error distribution |
| Whole-runway fleets | Multi-UAV/multi-rover fleet development is **proposed Phase III** | Procurement/design freeze, scaling/coverage tests, no fielded fleet claim |

**Avoid collapsing denominators:** 30 day/night missions are not equivalent to the separately reported 42 collection tasks. Neither aggregate is yet a blinded, independently repeatable system-success rate. The manuscript's team-reported results are not a replacement for archived per-trial telemetry.

### Ground-platform configuration caution

Earlier public engineering snapshots describe a **Mecanum chassis and hybrid ROS1/ROS2/Nav2/SLAM development configuration**. The **later reported build** is a **tracked/skid-steer rover** with a fabricated ramp-and-lift collector, based on the team presentation and October programme account. However, the retained journal-development image `internal/analysis/final/tikz/photos/rover.jpg` shows a **wheeled collector**; the two photograph/build baselines have not been conclusively linked. Those are different baselines and **must not be depicted as the same installed configuration**.

Until an as-tested build inventory exists, the portfolio does not assert that every earlier Nav2, SLAM, motor or GCS interface was part of the exact later field configuration. **Do not call the photographed wheeled platform a tracked rover.** The [media re-audit](../../audit/MEDIA_TECHNICAL_REAUDIT_2026_10_25.md) documents the unresolved identification.

## What I led

My contribution is **systems engineering, technical direction, programme integration and experiment/V&V leadership**: decompose the mission, identify interfaces and risks, direct experiment design and engineering acceptance, review perception/deployment results, coordinate multidisciplinary contributions and make unresolved validation work explicit.

**Team-developed contributions:** airframe and payload integration, controller code, GCS/ROS implementation, rover construction, field activity and physical mechanism work. I do not claim sole mechanical or software authorship.

## Supporting real photographs and trial captures

| Authentic record | What it does and does not show |
|---|---|
| ![Actual airborne programme UAV](../../visuals/autonomy-edge-ai/tir-fod/airborne_platform.png) | Real **earlier TIR-FOD sensing UAV**, not the latest rover or proof of entire mission |
| ![Recorded field detection outputs](../../visuals/autonomy-edge-ai/clear-run/field_trial_evidence.png) | Actual trial-frame derivatives and event counts from an earlier September snapshot; not pickup outcomes or measured geolocation errors |

The earlier [Clear Run public case](clear-run-tir-fod.md) contains original source and integration imagery from the September configuration. Its GCS screen is captured with UAV/sensors/ground agent disconnected; it is interface evidence rather than a live end-to-end mission record. It is retained for provenance but should not be used to infer the latest installed ground hardware.

## Publications and maturity

- **TIR-FOD:** resubmitted to IEEE Access **6 October 2026**, decision pending; public dataset available on Zenodo.
- **Integrated Clear Run paper:** submitted / under consideration as reported by the author in October 2026; no acceptance claimed.
- **Future Phase III:** coordinated, multi-vehicle whole-runway inspection and recovery is a research/funding proposal, **not** executed fleet capability.
- No commercial deployment, airport certification, approved unattended runway operation, official TRL rating or secured external adopter is asserted.

*This public case omits precise airfield locations, private communications details, unpublished assets and sensitive programme records.*
