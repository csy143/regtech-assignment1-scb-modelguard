from __future__ import annotations

import pandas as pd


def compute_fairness_metrics(
    train: pd.DataFrame,
    live: pd.DataFrame,
    reference_group: str = "Chinese",
) -> dict:
    """Approval Rate Ratio (ARR) and default-rate ratios vs reference ethnicity."""
    if "ethnicity" not in live.columns:
        return {
            "enabled": False,
            "message": "Ethnicity unavailable — US fairness-under-unawareness path.",
        }

    return {
        "enabled": True,
        "reference_group": reference_group,
        "train": _group_outcomes(train, reference_group),
        "live": _group_outcomes(live, reference_group),
        "arr_live_min": _min_arr(live, reference_group, "approval_rate"),
        "arr_train_min": _min_arr(train, reference_group, "approval_rate"),
        "gender_live": _gender_arr(live),
    }


def _group_outcomes(df: pd.DataFrame, ref: str) -> list[dict]:
    ref_appr = df.loc[df["ethnicity"] == ref, "approved"].mean()
    ref_def = df.loc[df["ethnicity"] == ref, "actual_default"].mean()
    rows = []
    for eth in sorted(df["ethnicity"].unique()):
        sub = df[df["ethnicity"] == eth]
        appr = float(sub["approved"].mean())
        default = float(sub["actual_default"].mean())
        rows.append(
            {
                "ethnicity": eth,
                "n": int(len(sub)),
                "approval_rate": appr,
                "default_rate": default,
                "arr_vs_reference": float(appr / ref_appr) if ref_appr else None,
                "default_ratio_vs_reference": float(default / ref_def) if ref_def else None,
            }
        )
    return rows


def _min_arr(df: pd.DataFrame, ref: str, field: str) -> float | None:
    ref_rate = df.loc[df["ethnicity"] == ref, "approved"].mean()
    if not ref_rate:
        return None
    ratios = []
    for eth in df["ethnicity"].unique():
        if eth == ref:
            continue
        r = df.loc[df["ethnicity"] == eth, "approved"].mean() / ref_rate
        ratios.append(r)
    return float(min(ratios)) if ratios else None


def _gender_arr(df: pd.DataFrame) -> dict:
    if "gender" not in df.columns:
        return {}
    ref = df[df["gender"] == "M"]["approved"].mean()
    f = df[df["gender"] == "F"]["approved"].mean()
    return {
        "reference": "M",
        "arr_female_vs_male": float(f / ref) if ref else None,
    }
