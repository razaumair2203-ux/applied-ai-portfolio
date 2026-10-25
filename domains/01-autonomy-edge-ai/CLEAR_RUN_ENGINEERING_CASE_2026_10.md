# Clear Run — integrated airfield robotics and systems engineering
**As of 25 October 2026 · prototype demonstration and active field-research programme**

> **Engineering perspective:** The project is not a standalone FOD detector. It tests the interfaces that convert detection into supervised physical recovery. A fabricated collection system and an integrated mission demonstration are **reported by the project lead**. A release-cleared outdoor source sequence now shows the team-built collector on a small-wheel development platform; it does not establish the later reported tracked/skid-steer configuration. Repeated, independently auditable detection-to-retention performance is not yet established.

[Original field/hardware media](../../media/showcase/README.md#clear-run) · [Programme maturity summary](CLEAR_RUN_2026-10_STATUS.md) · [Public field-evidence extract](../../evidence/autonomy_edge_ai/clear_run/README.md) · [Released TIR-FOD dataset](https://doi.org/10.5281/zenodo.22546586)

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
| Ground hardware | **Fabricated ramp-and-lift collector**, with a later tracked/skid-steer drive revision reported by the team; latest hardware photo not publicly released | Freeze installed hardware/firmware/sensor revisions |
| Mission demonstration | Complete prototype mission **confirmed by project lead** | Preserve synchronized as-tested configuration, event/time chain and independent witness/records |
| Day/night missions | **15 daytime + 15 after-dark** missions in latest author-reported campaign | Session-linked conditions, failures, success denominators and independent audit |
| Physical retention | Earlier October author-reported **38 retained collection outcomes / 42 tasks (90.5%)** | Retained per-task ledger, object conditions, post-capture motion and failure taxonomy |
| Geolocation | Estimates generated; historical approximate 1 m RMSE reported as a scalar | Paired surveyed reference/output locations and error distribution |
| Whole-runway fleets | Multi-UAV/multi-rover fleet development is **proposed Phase III** | Procurement/design freeze, scaling/coverage tests, no fielded fleet claim |

**Avoid collapsing denominators:** 30 day/night missions are not equivalent to the separately reported 42 collection tasks. Neither aggregate is yet a blinded, independently repeatable system-success rate. The manuscript's team-reported results are not a replacement for archived per-trial telemetry.

### Ground-platform configuration caution

Earlier public engineering snapshots describe a **Mecanum chassis and hybrid ROS1/ROS2/Nav2/SLAM development configuration**. The team reports a later **tracked/skid-steer rover** and fabricated ramp-and-lift collector. Earlier project images and ROS/Mecanum development configurations are historical stages and must not be represented as that later as-tested configuration. Those are different baselines and **must not be depicted as the same installed configuration**.

Until an as-tested build inventory exists, the portfolio does not assert that every earlier Nav2, SLAM, motor or GCS interface was part of the exact later field configuration.

## What I led

My contribution is **systems engineering, technical direction, programme integration and experiment/V&V leadership**: decompose the mission, identify interfaces and risks, direct experiment design and engineering acceptance, review perception/deployment results, coordinate multidisciplinary contributions and make unresolved validation work explicit.

**Team-developed contributions:** airframe and payload integration, controller code, GCS/ROS implementation, rover construction, field activity and physical mechanism work. I do not claim sole mechanical or software authorship.

## Physical hardware and authentic recorded frames

[![Clear Run fabricated collector, three frames from one edited source](../../media/showcase/clear-run-real-collector-sequence.png)](../../media/showcase/README.md#clear-run--fabricated-debris-collection-prototype)

This media comes **from the Clear Run programme itself**, not from the earlier TIR-FOD photo set. The pickup-platform frames show a fabricated mechanism on the small-wheel configuration seen in source footage; original playback is labelled **2.5×**. The final frame's “collected” label is part of the original student's edited video, **not an independently audited capture/retention result**. These frames belong to one footage family, not three repeat trials.

[Unaltered original collector frame](../../media/real/clear-run-collector-before.jpg) · [Same source after movement](../../media/real/clear-run-collector-approach.jpg) · [Original outcome-overlay frame](../../media/real/clear-run-collector-source-outcome-overlay.jpg) · [Original Clear Run in-flight UAV](../../media/real/clear-run-uav-inflight.jpg)

The final collector configuration, GCS dispatch state, mission timing and whole-chain object identity must still be associated with the as-tested records before declaring measured end-to-end success.

## Publications and maturity

- **TIR-FOD:** resubmitted to IEEE Access **6 October 2026**, decision pending; public dataset available on Zenodo.
- **Integrated Clear Run paper:** submitted / under consideration as reported by the author in October 2026; no acceptance claimed.
- **Future Phase III:** coordinated, multi-vehicle whole-runway inspection and recovery is a research/funding proposal, **not** executed fleet capability.
- No commercial deployment, airport certification, approved unattended runway operation, official TRL rating or secured external adopter is asserted.

*This public case omits precise airfield locations, private communications details, unpublished assets and sensitive programme records.*
