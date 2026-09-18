"""Sanitized TIR-FOD training/evaluation harness matching the recorded revision protocol.

Inspect without dependencies:
    python train_public.py --config baseline_n --data /path/to/data.yaml --seed 42 --dry-run

Run training (requires a compatible Ultralytics/PyTorch/CUDA environment):
    python train_public.py --config baseline_n --data /path/to/data.yaml --seed 42
"""
from __future__ import annotations
import argparse
import json
import time
from pathlib import Path

MODELS = {
    "baseline_n": "yolov8n.pt",
    "baseline_s": "yolov8s.pt",
    "baseline_m": "yolov8m.pt",
    "baseline_11s": "yolo11s.pt",
    "baseline_11m": "yolo11m.pt",
    "baseline_12s": "yolo12s.pt",
    "originals_fixedopt_s": "yolov8s.pt",
    "contam_matched_s": "yolov8s.pt",
    "framelevel_12c_s": "yolov8s.pt",
    "xsession_12c_s": "yolov8s.pt",
}

BASE = dict(
    epochs=60, imgsz=640, batch=32, workers=8, patience=15,
    deterministic=True, optimizer="auto", close_mosaic=10,
    hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, degrees=0.0,
    translate=0.1, scale=0.5, shear=0.0, perspective=0.0,
    flipud=0.0, fliplr=0.5, mosaic=1.0, mixup=0.0,
    copy_paste=0.0, val=True, plots=False, verbose=False,
)
FIXED_OPT = {"optimizer": "MuSGD", "lr0": 0.01, "momentum": 0.9}


def build_contract(config: str, data: str, seed: int, device: str, project: str) -> dict:
    if config not in MODELS:
        raise ValueError(f"unknown config: {config}")
    train_kwargs = dict(BASE)
    if config in {"originals_fixedopt_s", "contam_matched_s"}:
        train_kwargs.update(FIXED_OPT)
    train_kwargs.update(seed=seed, device=device)
    return {
        "config": config,
        "model": MODELS[config],
        "data": data,
        "seed": seed,
        "project": project,
        "train_kwargs": train_kwargs,
        "evaluation": {"split": "test", "imgsz": 640, "batch": 32, "workers": 8, "device": device},
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True, choices=sorted(MODELS))
    ap.add_argument("--data", required=True, help="Frozen dataset data.yaml for this configuration")
    ap.add_argument("--seed", required=True, type=int)
    ap.add_argument("--device", default="0")
    ap.add_argument("--project", default="runs_public")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    contract = build_contract(args.config, args.data, args.seed, args.device, args.project)
    if args.dry_run:
        print(json.dumps(contract, indent=2))
        return

    from ultralytics import YOLO

    t0 = time.time()
    model = YOLO(contract["model"])
    model.train(
        data=contract["data"],
        project=contract["project"],
        name=f"{args.config}_seed_{args.seed}",
        exist_ok=True,
        **contract["train_kwargs"],
    )
    train_seconds = time.time() - t0

    run_dir = Path(contract["project"]) / f"{args.config}_seed_{args.seed}"
    best = YOLO(str(run_dir / "weights" / "best.pt"))
    val = best.val(data=contract["data"], **contract["evaluation"])
    box = val.box
    result = {
        "config": args.config,
        "seed": args.seed,
        "model": contract["model"],
        "test_mAP50": float(box.map50),
        "test_mAP50_95": float(box.map),
        "test_mAP75": float(box.map75),
        "precision": float(box.mp),
        "recall": float(box.mr),
        "train_seconds": train_seconds,
        "completed_epochs": int(getattr(model.trainer, "epoch", -1) + 1),
    }
    out = run_dir / "public_result.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
