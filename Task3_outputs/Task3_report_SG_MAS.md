# SCB ModelGuard — Compliance Report (Singapore — MAS FEAT / AI MRM (2024–2025))

**Overall status: FAIL**

## Model scope
- In scope for traditional MRM: **True**
- Rationale: Same SCB-CS-001 model deployed in Singapore; native ethnicity permitted for conduct and FEAT outcome monitoring alongside prudential performance tests.

## Data handling
- SG path retains native `ethnicity` for FEAT / outcome monitoring (Chinese/Malay/Indian/Other).

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
- warn_threshold: 0.03
- fail_threshold: 0.06
- note: SCB-CS-001 is a traditional PD-style score; OCC 2026-13 validation triggers apply. GenAI exclusion does not apply to this model.

### drift
- Status: **FAIL**
- psi_model_score: 0.46389764122873256
- psi_status: fail
- low_score_share_increase: 0.0484
- low_score_status: fail

### portfolio_outcomes
- Status: **WARN**
- default_rate_increase: 0.09773333333333334

### fairness
- Status: **PASS**
- enabled: True
- arr_live_min: 0.9790288529204786
- arr_ethnicity_floor: 0.8
- arr_status: pass
- gender_arr: 0.9989571166360753
- gender_status: pass

## Fairness detail (live)
- Chinese: approval=0.900, ARR vs Chinese=1.000
- Indian: approval=0.911, ARR vs Chinese=1.012
- Malay: approval=0.900, ARR vs Chinese=1.001
- Other: approval=0.881, ARR vs Chinese=0.979

## Escalation
Recommend pause on live rollout expansion; root-cause on drift + FEAT outcome review; prepare committee pack for Singapore governance forum.

