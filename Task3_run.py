#!/usr/bin/env python3
"""SCB ModelGuard — Task 3 Option C analysis pipeline."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from src.config_loader import load_jurisdiction_config
from src.engine.evaluator import evaluate_jurisdiction
from src.engine.narrative import render_report
from src.load_data import apply_jurisdiction_data_policy, load_period_data
from src.metrics.drift import compute_drift_metrics
from src.metrics.fairness import compute_fairness_metrics
from src.metrics.performance import compute_performance_metrics
from src.sensitivity.distribution_shift import run_sensitivity

OUTPUT = ROOT / "Task3_outputs"
FIGURES = OUTPUT / "figures"


def _save_figures(train: pd.DataFrame, live: pd.DataFrame, perf: dict) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=(8, 4))
    for label, df in [("Training (2022-23)", train), ("Live (2025-26)", live)]:
        ax.hist(df["model_score"], bins=30, alpha=0.55, label=label, density=True)
    ax.set_xlabel("model_score")
    ax.set_title("SCB-CS-001 Score Distribution Shift")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURES / "Task3_score_distribution.png", dpi=150)
    plt.close(fig)

    cal = pd.DataFrame(perf["calibration_live_by_decile"])
    if not cal.empty:
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(range(len(cal)), cal["actual_default_rate"], color="steelblue")
        ax.set_xticks(range(len(cal)))
        ax.set_xticklabels([f"D{i+1}" for i in range(len(cal))], rotation=0)
        ax.set_ylabel("Actual default rate")
        ax.set_title("Live portfolio calibration by score decile")
        fig.tight_layout()
        fig.savefig(FIGURES / "Task3_calibration_live.png", dpi=150)
        plt.close(fig)


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    config = load_jurisdiction_config()
    train, live = load_period_data()

    performance = compute_performance_metrics(train, live)
    drift = compute_drift_metrics(train, live)
    fairness = compute_fairness_metrics(train, live)

    metrics_bundle = {"performance": performance, "drift": drift, "fairness": fairness}
    with open(OUTPUT / "Task3_metrics_baseline.json", "w", encoding="utf-8") as f:
        json.dump(metrics_bundle, f, indent=2)

    evaluations = {}
    for jkey in ("US_OCC", "SG_MAS"):
        train_j = apply_jurisdiction_data_policy(train, jkey, config)
        if jkey == "US_OCC":
            fair_j = {
                "enabled": False,
                "message": "Ethnicity stripped — fairness-under-unawareness (see BISG exploratory stub).",
            }
        else:
            fair_j = compute_fairness_metrics(train_j, live, reference_group="Chinese")
        ev = evaluate_jurisdiction(jkey, config, performance, drift, fair_j)
        evaluations[jkey] = ev
        report = render_report(ev, performance, drift, fair_j)
        out_path = OUTPUT / f"Task3_report_{jkey}.md"
        out_path.write_text(report, encoding="utf-8")
        print(f"Wrote {out_path} — {ev['overall_status']}")

    with open(OUTPUT / "Task3_evaluations.json", "w", encoding="utf-8") as f:
        json.dump(evaluations, f, indent=2, default=str)

    sens = run_sensitivity(train, live, config)
    sens.to_csv(OUTPUT / "Task3_sensitivity.csv", index=False)
    sens.pivot(index="scenario", columns="jurisdiction", values="overall_status").to_csv(
        OUTPUT / "Task3_sensitivity_pivot.csv"
    )

    fig, ax = plt.subplots(figsize=(9, 4))
    status_map = {"PASS": 0, "WARN": 1, "FAIL": 2}
    plot_df = sens.copy()
    plot_df["status_num"] = plot_df["overall_status"].map(status_map)
    sns.barplot(data=plot_df, x="scenario", y="status_num", hue="jurisdiction", ax=ax)
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(["PASS", "WARN", "FAIL"])
    ax.set_title("Jurisdiction status under distribution-shift scenarios")
    ax.set_ylabel("Compliance status")
    fig.tight_layout()
    fig.savefig(FIGURES / "Task3_sensitivity_status.png", dpi=150)
    plt.close(fig)

    _save_figures(train, live, performance)

    print("\n=== Jurisdiction comparison (baseline) ===")
    for jkey in ("US_OCC", "SG_MAS"):
        e = evaluations[jkey]
        print(
            f"{jkey}: {e['overall_status']} | drift={e['checks']['drift']['status']} "
            f"| perf={e['checks']['performance']['status']} "
            f"| fairness={e['checks']['fairness']['status']}"
        )
    print(f"\nMetrics: AUC drop={performance['auc_drop']:.4f}, PSI={drift['psi_model_score']:.4f}")
    print(f"Outputs written to {OUTPUT}")


if __name__ == "__main__":
    main()
