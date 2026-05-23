from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_jurisdiction_config(path: Path | None = None) -> dict:
    if path is None:
        for candidate in (
            ROOT / "Task3_jurisdictions.yaml",
            ROOT / "config" / "jurisdictions.yaml",
        ):
            if candidate.exists():
                path = candidate
                break
        else:
            path = ROOT / "Task3_jurisdictions.yaml"
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)
