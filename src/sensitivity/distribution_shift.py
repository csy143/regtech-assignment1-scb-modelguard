from __future__ import annotations

import copy

import pandas as pd

from src.engine.evaluator import evaluate_jurisdiction
from src.metrics.drift import compute_drift_metrics
from src.metrics.fairness import compute_fairness_metrics
from src.metrics.performance import compute_performance_metrics


def apply_scenario(live: pd.DataFrame, scenario: str, seed: int = 42) -> pd.DataFrame:
    rng = pd.Series(range(len(live))).sample(frac=1, random_state=seed)
    df = live.copy()

    if scenario == "baseline":
        return df
    if scenario == "income_shock":
        df["income_sgd"] = (df["income_sgd"] * 0.88).round(2)
        return df
    if scenario == "score_inflation":
        n = int(0.25 * len(df))
        idx = df.sample(n=n, random_state=seed).index
        df.loc[idx, "model_score"] = (df.loc[idx, "model_score"] - 0.15).clip(0, 1)
        return df
    if scenario == "default_shock":
        idx = df[df["model_score"] < 0.55].sample(frac=0.35, random_state=seed).index
        df.loc[idx, "actual_default"] = 1
        return df
    if scenario == "fairness_stress_sg":
        idx = df[df["ethnicity"] == "Malay"].index
        flip = idx[: max(1, int(0.25 * len(idx)))]
        df.loc[flip, "approved"] = 0
        return df
    raise ValueError(f"Unknown scenario: {scenario}")


def run_sensitivity(
    train: pd.DataFrame,
    live: pd.DataFrame,
    config: dict,
    scenarios: list[str] | None = None,
) -> pd.DataFrame:
    scenarios = scenarios or [
        "baseline",
        "income_shock",
        "score_inflation",
        "default_shock",
        "fairness_stress_sg",
    ]
    rows = []
    for scenario in scenarios:
        live_s = apply_scenario(live, scenario)
        perf = compute_performance_metrics(train, live_s)
        drift = compute_drift_metrics(train, live_s)
        fair = compute_fairness_metrics(train, live_s)

        for jkey in ("US_OCC", "SG_MAS"):
            ev = evaluate_jurisdiction(jkey, config, perf, drift, fair)
            rows.append(
                {
                    "scenario": scenario,
                    "jurisdiction": jkey,
                    "overall_status": ev["overall_status"],
                    "auc_drop": perf["auc_drop"],
                    "psi": drift["psi_model_score"],
                    "arr_live_min": fair.get("arr_live_min"),
                    "default_rate_live": perf["default_rate_live"],
                }
            )
    return pd.DataFrame(rows)
