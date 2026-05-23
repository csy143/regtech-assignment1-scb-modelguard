from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score


def _default_prob(score: pd.Series) -> pd.Series:
    """Higher model_score = lower risk; map to P(default) for AUC."""
    return 1.0 - score


def compute_performance_metrics(
    train: pd.DataFrame,
    live: pd.DataFrame,
) -> dict:
    auc_train = roc_auc_score(train["actual_default"], _default_prob(train["model_score"]))
    auc_live = roc_auc_score(live["actual_default"], _default_prob(live["model_score"]))
    auc_drop = auc_train - auc_live
    gini_train = 2 * auc_train - 1
    gini_live = 2 * auc_live - 1

    default_train = float(train["actual_default"].mean())
    default_live = float(live["actual_default"].mean())
    approval_train = float(train["approved"].mean())
    approval_live = float(live["approved"].mean())

    calibration = _calibration_table(live)

    return {
        "auc_train": float(auc_train),
        "auc_live": float(auc_live),
        "auc_drop": float(auc_drop),
        "gini_train": float(gini_train),
        "gini_live": float(gini_live),
        "default_rate_train": default_train,
        "default_rate_live": default_live,
        "default_rate_increase": default_live - default_train,
        "approval_rate_train": approval_train,
        "approval_rate_live": approval_live,
        "calibration_live_by_decile": calibration,
    }


def _calibration_table(df: pd.DataFrame, n_bins: int = 10) -> list[dict]:
    work = df[["model_score", "actual_default"]].copy()
    work["decile"] = pd.qcut(
        work["model_score"],
        q=n_bins,
        duplicates="drop",
    )
    rows = []
    for decile, grp in work.groupby("decile", observed=True):
        rows.append(
            {
                "decile": str(decile),
                "mean_score": float(grp["model_score"].mean()),
                "actual_default_rate": float(grp["actual_default"].mean()),
                "count": int(len(grp)),
            }
        )
    return rows
