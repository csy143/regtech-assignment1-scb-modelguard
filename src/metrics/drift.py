from __future__ import annotations

import numpy as np
import pandas as pd


def population_stability_index(
    expected: np.ndarray | pd.Series,
    actual: np.ndarray | pd.Series,
    n_bins: int = 10,
) -> float:
    expected = np.asarray(expected, dtype=float)
    actual = np.asarray(actual, dtype=float)
    breakpoints = np.quantile(expected, np.linspace(0, 1, n_bins + 1))
    breakpoints = np.unique(breakpoints)
    if len(breakpoints) < 2:
        return 0.0

    exp_counts = np.histogram(expected, bins=breakpoints)[0].astype(float)
    act_counts = np.histogram(actual, bins=breakpoints)[0].astype(float)
    exp_pct = exp_counts / max(exp_counts.sum(), 1)
    act_pct = act_counts / max(act_counts.sum(), 1)
    exp_pct = np.clip(exp_pct, 1e-6, None)
    act_pct = np.clip(act_pct, 1e-6, None)
    exp_pct = exp_pct / exp_pct.sum()
    act_pct = act_pct / act_pct.sum()
    return float(np.sum((act_pct - exp_pct) * np.log(act_pct / exp_pct)))


def compute_drift_metrics(train: pd.DataFrame, live: pd.DataFrame) -> dict:
    psi_score = population_stability_index(train["model_score"], live["model_score"])
    psi_income = population_stability_index(train["income_sgd"], live["income_sgd"])
    psi_dti = population_stability_index(train["debt_to_income"], live["debt_to_income"])

    low_threshold = 0.4
    low_train = float((train["model_score"] < low_threshold).mean())
    low_live = float((live["model_score"] < low_threshold).mean())

    unemp_train = float((train["employment_status"] == "Unemployed").mean())
    unemp_live = float((live["employment_status"] == "Unemployed").mean())

    return {
        "psi_model_score": psi_score,
        "psi_income_sgd": psi_income,
        "psi_debt_to_income": psi_dti,
        "low_score_share_train": low_train,
        "low_score_share_live": low_live,
        "low_score_share_increase": low_live - low_train,
        "median_income_train": float(train["income_sgd"].median()),
        "median_income_live": float(live["income_sgd"].median()),
        "mean_loan_train": float(train["loan_amount_sgd"].mean()),
        "mean_loan_live": float(live["loan_amount_sgd"].mean()),
        "unemployment_rate_train": unemp_train,
        "unemployment_rate_live": unemp_live,
    }
