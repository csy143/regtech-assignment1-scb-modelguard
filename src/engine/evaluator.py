from __future__ import annotations

from typing import Any


def _flag(value: float, warn: float, fail: float, higher_is_bad: bool = True) -> str:
    if higher_is_bad:
        if value >= fail:
            return "fail"
        if value >= warn:
            return "warn"
        return "pass"
    if value <= fail:
        return "fail"
    if value <= warn:
        return "warn"
    return "pass"


def evaluate_jurisdiction(
    jurisdiction_key: str,
    config: dict,
    performance: dict,
    drift: dict,
    fairness: dict,
) -> dict[str, Any]:
    j = config["jurisdictions"][jurisdiction_key]
    rules = j["rules"]
    checks: dict[str, dict] = {}

    # --- Performance (traditional MRM — in scope for OCC on SCB-CS-001) ---
    auc_drop = performance["auc_drop"]
    p_rules = rules["performance"]
    checks["performance"] = {
        "metric": "auc_drop",
        "value": auc_drop,
        "warn_threshold": p_rules["auc_drop_warn"],
        "fail_threshold": p_rules["auc_drop_fail"],
        "status": _flag(auc_drop, p_rules["auc_drop_warn"], p_rules["auc_drop_fail"]),
        "note": (
            "SCB-CS-001 is a traditional PD-style score; OCC 2026-13 validation triggers "
            "apply. GenAI exclusion does not apply to this model."
        ),
    }

    # --- Drift ---
    psi = drift["psi_model_score"]
    d_rules = rules["drift"]
    low_inc = drift["low_score_share_increase"]
    psi_status = _flag(psi, d_rules["psi_score_warn"], d_rules["psi_score_fail"])
    low_status = _flag(
        low_inc,
        d_rules["low_score_share_increase_warn"],
        d_rules["low_score_share_increase_fail"],
    )
    drift_status = "fail" if "fail" in (psi_status, low_status) else (
        "warn" if "warn" in (psi_status, low_status) else "pass"
    )
    checks["drift"] = {
        "psi_model_score": psi,
        "psi_status": psi_status,
        "low_score_share_increase": low_inc,
        "low_score_status": low_status,
        "status": drift_status,
    }

    # --- Portfolio outcomes ---
    d_inc = performance["default_rate_increase"]
    o_rules = rules["portfolio_outcomes"]
    checks["portfolio_outcomes"] = {
        "default_rate_increase": d_inc,
        "status": _flag(d_inc, o_rules["default_rate_increase_warn"], o_rules["default_rate_increase_fail"]),
    }

    # --- Fairness ---
    f_rules = rules["fairness"]
    if not f_rules.get("enabled", False):
        checks["fairness"] = {
            "status": "advisory",
            "enabled": False,
            "message": j.get("escalation", {}).get(
                "fairness_advisory",
                "Fairness metrics suppressed in US mode (fairness-under-unawareness).",
            ),
        }
        fairness_fail = False
        fairness_warn = False
    else:
        arr_min = fairness.get("arr_live_min")
        floor = f_rules.get("arr_ethnicity_floor")
        gender = fairness.get("gender_live", {})
        g_floor = f_rules.get("arr_gender_floor")
        arr_status = "pass"
        if arr_min is not None and floor is not None:
            arr_status = _flag(
                floor - arr_min,
                0.0,
                0.0,
                higher_is_bad=True,
            ) if arr_min < floor else "pass"
            if arr_min < floor:
                arr_status = "fail"

        g_arr = gender.get("arr_female_vs_male")
        g_status = "pass"
        if g_arr is not None and g_floor is not None and g_arr < g_floor:
            g_status = "fail"

        f_status = "fail" if "fail" in (arr_status, g_status) else (
            "warn" if "warn" in (arr_status, g_status) else "pass"
        )
        checks["fairness"] = {
            "status": f_status,
            "enabled": True,
            "arr_live_min": arr_min,
            "arr_ethnicity_floor": floor,
            "arr_status": arr_status,
            "gender_arr": g_arr,
            "gender_status": g_status,
        }
        fairness_fail = f_status == "fail"
        fairness_warn = f_status == "warn"

    perf_fail = checks["performance"]["status"] == "fail"
    perf_warn = checks["performance"]["status"] == "warn"
    drift_fail = checks["drift"]["status"] == "fail"
    drift_warn = checks["drift"]["status"] == "warn"
    port_fail = checks["portfolio_outcomes"]["status"] == "fail"
    port_warn = checks["portfolio_outcomes"]["status"] == "warn"

    agg = j.get("aggregation", {})
    if jurisdiction_key == "US_OCC":
        if perf_fail and drift_fail:
            overall = "FAIL"
        elif perf_fail or drift_fail or port_fail or perf_warn or drift_warn or port_warn:
            overall = "WARN"
        else:
            overall = "PASS"
    else:
        if perf_fail or drift_fail or port_fail or fairness_fail:
            overall = "FAIL"
        elif perf_warn or drift_warn or port_warn or fairness_warn:
            overall = "WARN"
        else:
            overall = "PASS"

    return {
        "jurisdiction": jurisdiction_key,
        "display_name": j["display_name"],
        "model_scope": j.get("model_scope", {}),
        "data_handling": j.get("data_handling", {}),
        "overall_status": overall,
        "checks": checks,
        "escalation": j.get("escalation", {}).get(overall.lower(), ""),
    }
