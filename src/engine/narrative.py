from __future__ import annotations

from typing import Any


def render_report(
    evaluation: dict[str, Any],
    performance: dict,
    drift: dict,
    fairness: dict,
) -> str:
    j = evaluation["jurisdiction"]
    lines = [
        f"# SCB ModelGuard — Compliance Report ({evaluation['display_name']})",
        "",
        f"**Overall status: {evaluation['overall_status']}**",
        "",
        "## Model scope",
        f"- In scope for traditional MRM: **{evaluation['model_scope'].get('in_scope')}**",
        f"- Rationale: {evaluation['model_scope'].get('rationale', '').strip()}",
        "",
        "## Data handling",
    ]
    dh = evaluation.get("data_handling", {})
    if dh.get("strip_fields"):
        lines.append(
            f"- US path strips `{dh['strip_fields']}` at ingest (ECOA / fairness-under-unawareness)."
        )
        lines.append(
            "- BISG (surname + geography) may be used in production for **exploratory** US fair-lending "
            "audits only; this run does not invoke BISG."
        )
    else:
        lines.append(
            "- SG path retains native `ethnicity` for FEAT / outcome monitoring (Chinese/Malay/Indian/Other)."
        )

    lines.extend(["", "## Key metrics", ""])
    lines.append(f"| Metric | Training | Live |")
    lines.append(f"|--------|----------|------|")
    lines.append(
        f"| AUC (1−score) | {performance['auc_train']:.4f} | {performance['auc_live']:.4f} |"
    )
    lines.append(
        f"| Default rate | {performance['default_rate_train']:.2%} | {performance['default_rate_live']:.2%} |"
    )
    lines.append(
        f"| PSI (model_score) | — | {drift['psi_model_score']:.4f} |"
    )
    lines.append(
        f"| Low-score share (<0.4) | {drift['low_score_share_train']:.2%} | {drift['low_score_share_live']:.2%} |"
    )

    lines.extend(["", "## Rule checks", ""])
    for name, chk in evaluation["checks"].items():
        lines.append(f"### {name}")
        lines.append(f"- Status: **{chk.get('status', 'n/a').upper()}**")
        for k, v in chk.items():
            if k == "status":
                continue
            lines.append(f"- {k}: {v}")
        lines.append("")

    if evaluation["checks"].get("fairness", {}).get("enabled"):
        lines.append("## Fairness detail (live)")
        for row in fairness.get("live", []):
            lines.append(
                f"- {row['ethnicity']}: approval={row['approval_rate']:.3f}, "
                f"ARR vs {fairness.get('reference_group', 'Chinese')}={row['arr_vs_reference']:.3f}"
            )
    else:
        lines.append("## Fairness (US advisory)")
        lines.append(f"- {evaluation['checks']['fairness'].get('message', '')}")

    lines.extend(["", "## Escalation", evaluation.get("escalation", ""), ""])
    return "\n".join(lines)
