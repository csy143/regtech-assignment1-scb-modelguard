# SCB ModelGuard — Compliance Report (United States — OCC Bulletin 2026-13 (traditional MRM))

**Overall status: WARN**

## Model scope
- In scope for traditional MRM: **True**
- Rationale: SCB-CS-001 is a Probability-of-Default style retail credit model using financial and employment features. It is NOT GenAI/agentic AI and therefore remains within OCC 2026-13 development, validation, and monitoring expectations.

## Data handling
- US path strips `['ethnicity', 'gender']` at ingest (ECOA / fairness-under-unawareness).
- BISG (surname + geography) may be used in production for **exploratory** US fair-lending audits only; this run does not invoke BISG.

## Key metrics

| Metric | Training | Live |
|--------|----------|------|
| AUC (1−score) | 0.6312 | 0.6162 |
| Default rate | 24.86% | 34.63% |
| PSI (model_score) | — | 0.4639 |
| Low-score share (<0.4) | 0.86% | 5.70% |

## Rule checks

### performance
- Status: **PASS**
- metric: auc_drop
- value: 0.01496340477462288
- warn_threshold: 0.05
- fail_threshold: 0.1
- note: SCB-CS-001 is a traditional PD-style score; OCC 2026-13 validation triggers apply. GenAI exclusion does not apply to this model.

### drift
- Status: **WARN**
- psi_model_score: 0.46389764122873256
- psi_status: warn
- low_score_share_increase: 0.0484
- low_score_status: warn

### portfolio_outcomes
- Status: **WARN**
- default_rate_increase: 0.09773333333333334

### fairness
- Status: **ADVISORY**
- enabled: False
- message: Ethnicity/gender disparity statistics are suppressed in US mode. Run optional BISG exploratory module separately; findings are litigation/ESG advisory only.


## Fairness (US advisory)
- Ethnicity/gender disparity statistics are suppressed in US mode. Run optional BISG exploratory module separately; findings are litigation/ESG advisory only.


## Escalation
Trigger independent model validation review under OCC 2026-13 (backtesting, benchmarking, trigger-based revalidation). Document for audit trail.

