from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT

PROTECTED_DEFAULT = ["ethnicity", "gender"]


def load_period_data(
    train_path: Path | None = None,
    live_path: Path | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    train_path = train_path or DATA_DIR / "Task3_TrainingData.csv"
    live_path = live_path or DATA_DIR / "Task3_LiveData.csv"
    train = pd.read_csv(train_path)
    live = pd.read_csv(live_path)
    return train, live


def apply_jurisdiction_data_policy(
    df: pd.DataFrame,
    jurisdiction_key: str,
    config: dict,
) -> pd.DataFrame:
    """US mode strips ethnicity/gender per ECOA / fairness-under-unawareness."""
    j = config["jurisdictions"][jurisdiction_key]
    strip = j.get("data_handling", {}).get("strip_fields", [])
    out = df.copy()
    for col in strip:
        if col in out.columns:
            out = out.drop(columns=[col])
    return out
