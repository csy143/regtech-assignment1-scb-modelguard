# SCB ModelGuard — Integrated Technical & Regulatory Report  
**Assignment 1, Session 1 | Task 1 + Task 2 + Task 3 (Option C)**  
**Entity:** Standard Chartered Bank | **Model:** SCB-CS-001 | **Vendor:** Meridian Model Assurance (hypothetical RegTech)

---

## Executive abstract

SCB ModelGuard monitors one retail credit model across **two incompatible 2026 legal regimes**. On identical synthetic data (training 2022–2023, live 2025–2026), the tool reports **United States: WARN** and **Singapore: FAIL**. The divergence is not a software bug; it encodes how **political choices** in Washington and Singapore assign different meaning to the same PSI (~0.46), ΔAUC (~0.015), and portfolio stress. This report integrates entity selection (Task 1), values audit (Task 2), and quantitative methodology (Task 3) into one defensible narrative.

---

## Part I — Selection rationale: why Standard Chartered, why credit scoring + fairness

### 1.1 Named regulated entity

**Standard Chartered PLC** is a globally systemic bank with material **US** operations (OCC-supervised national bank subsidiaries) and **Singapore** as a regional headquarters and licensing hub (MAS). It is not a fictional convenience—it forces the RegTech design to confront **real cross-border deployment** of the same model inventory.

| Dimension | United States | Singapore |
|-----------|---------------|-----------|
| Primary supervisor (this project) | **OCC** — Bulletin **2026-13** (Apr 2026) | **MAS** — FEAT + AI/ML MRM (2024–2025) |
| Legal tradition for credit fairness | Civil-rights framing (ECOA, Regulation B, historical disparate impact) | Conduct + AI governance (FEAT outcomes, no HMDA-style race database) |
| 2026 direction (lecture) | **Deregulatory** on statistical fairness; **persistent** on traditional model risk | **Tightening** on AI robustness and fair outcomes |

**References:** OCC 2026-13 — https://www.occ.treas.gov/news-issuances/bulletins/2026/bulletin-2026-13.html ; MAS fairness principles in AI/ML — https://www.mas.gov.sg/publications/monographs-or-information-paper/2022/implementation-of-fairness-principles-in-financial-institutions-use-of-artificial-intelligence-and-machine-learning

### 1.2 Domain: retail credit scoring intersecting algorithmic fairness and MRM

We deliberately sit at the collision of two lecture threads:

1. **Model risk management** — Every significant lending decision runs through a score; regulators demand proof the model still works after macro shock (Basel lineage, SR 11-7 → OCC 2026-13).
2. **Algorithmic fairness / fair lending** — Historical discrimination migrated into “neutral” proxies (ZIP, employment type, credit history); US 2026 policy **retreats** from outcome-based enforcement while the EU/Singapore path **hardens** conduct-style monitoring.

**SCB-CS-001** is a **traditional Probability-of-Default-style retail score** (financial features, employment, DTI)—**not** GenAI. This distinction is legally load-bearing: OCC 2026-13 states *“GenAI and agentic AI fall outside this guidance's scope.”* **Traditional scores remain in scope** for development, validation, backtesting, and trigger-based revalidation.

### 1.3 RegTech as political artefacts

Lecture framing: *“RegTech tools are political artefacts.”* SCB ModelGuard is not neutral instrumentation—it **bakes in** whose law wins:

- **US mode** strips `ethnicity` and `gender` at ingest (ECOA / **fairness-under-unawareness**), computes **PSI and calibration drift** as hard MRM signals, and treats fairness as **advisory** (optional BISG exploratory path per CFPB proxy methodology lecture—**not** auto-fail).
- **Singapore mode** retains native ethnicity (Chinese / Malay / Indian / Other), applies **stricter PSI FAIL bands**, and can **FAIL** on portfolio outcome shifts under FEAT-style logic.

The **same PSI = 0.464** therefore produces **WARN** in the US (below FAIL threshold 0.55; principles-based “validate but don’t automatically halt”) and **FAIL** in Singapore (above FAIL threshold 0.25 → recommend pausing rollout expansion). That is the **dramatic political flip** the assignment demands: metrics are shared; **consequences** are jurisdiction-specific.

### 1.4 Divergent legislative choices (lecture evidence)

| Policy fork | United States (2025–2026) | Singapore |
|-------------|----------------------------|-----------|
| Disparate impact / outcome tests | Executive and Reg B trajectory toward **intent**; statistical disparity loses federal enforcement teeth | **FEAT** emphasises fair outcomes and accountability |
| Fair lending data infrastructure | HMDA-rich history; non-mortgage race data scarce → **BISG** proxies | Ethnicity often **lawfully available** in domestic operations data |
| AI credit governance | OCC 2026-13 **excludes GenAI only** | MAS AI MRM expects ongoing robustness under shift |
| What “compliance” means in 2026 | **Document validation** + avoid unsafe/unsound MRM | **Demonstrate** outcome and drift control to MAS-facing committees |

---

## Part II — Values audit: four philosophical questions

### 2.1 Our RegTech company: Meridian Model Assurance and product line SCB ModelGuard

**Mission:** *Make cross-border model risk visible before regulators and customers pay the price.*

| Attribute | Positioning |
|-----------|-------------|
| **Stage** | Growth-stage Series A (~35 FTE): 18 engineering, 10 quant/risk, 7 policy/legal translators |
| **Competency** | Jurisdiction rule engines, drift quantification, audit-grade committee packs |
| **Revenue aspiration** | USD 8–12M ARR within 24 months from 4–6 anchor global banks |
| **Geography** | HQ Singapore; commercial offices US/UK/UAE; **first rule packs: US_OCC + SG_MAS** |
| **Product** | **SCB ModelGuard** — instance for Standard Chartered’s **SCB-CS-001** retail score |

We sell to **multinational banks** whose CCOs cannot reconcile one Excel workbook with two regulators.

### 2.2 Whose perspective? Irreconcilable stakeholders in the 2026 macro winter

**Primary paying client:** Standard Chartered **CCO / Head of Model Risk** — wants **frictionless approvals** for business lines **and** defensible documentation for exams.

**Regulator perspectives:**

- **US (OCC):** Prudential — *“Is model risk managed to safe-and-sound standard?”* Fair lending enforcement capacity collapsed (CFPB staff lecture: 1,700 → ~200); **MRM remains**.
- **MAS:** Conduct + technology — *“Is AI robust under shift; are customer outcomes fair?”*

**Consumer (2025–2026 live cohort evidence):** Median income **SGD 47,832 → 42,454** (−11.2%); unemployment **2.8% → 6.7%**; portfolio default **24.9% → 34.6%**; approval **98.5% → 90.0%**. In a downturn, consumers need **credit liquidity** to smooth consumption; banks need **tighter gates** to protect capital—both are rational, mutually painful.

| Tension | Evidence in data / policy | Conflict |
|---------|---------------------------|----------|
| CCO vs US examiner | OCC footnote: guidance “non-binding” yet **unsafe/unsound** still enforceable | CCO wants green dashboards; examiner wants revalidation triggers |
| CCO vs MAS | PSI FAIL at 0.25 in SG vs 0.55 in US | Singapore unit must pause; US unit may continue with WARN |
| Bank vs consumer | Approval cut 8.5 pp while defaults rose 9.8 pp | More rejections **and** worse realised risk if model stale |
| Fairness vs growth | US: ethnicity stripped; SG: ARR monitored | Same bank brand, different moral visibility |

**Our choice:** Serve **model risk truth first**, CCO second—product sells **early warning**, not **compliance theatre**.

### 2.3 Genuine risk measurement vs compliance documentation

**Thesis:** RegTech must measure **substantive model economics**, not only produce binders.

**Feature kept for risk (not federally mandated as a checkbox):**

- **Live decile calibration tables** — Even when ΔAUC is only **0.015** (below US WARN 0.05), the lowest decile’s realised default rate on live data hits **55.7%** vs **11.4%** in the top decile. Rank-order can look stable while **absolute loss rates** explode under macro shift—classic post-COVID inflation / rate shock pattern.
- **PSI on `model_score`** — Income PSI is mild (0.049); **score PSI is 0.464** — the scoring population itself has reshaped (low-score share **0.86% → 5.70%**).

**Feature withheld to avoid documentation theatre:**

- **US auto “fair lending cleared” badge** from ethnicity ARR — After disparate-impact retreat, that would be **performative** and legally hazardous if ethnicity entered the US decision path. US pipeline **drops** protected fields; BISG remains an **exploratory stub** (`src/bisg_stub.py`).

### 2.4 Who pays when the tool is wrong?

| Error type | Mechanism | Who bears harm (2026 winter) |
|------------|-----------|------------------------------|
| **False negative** (miss drift) | PSI 0.46 ignored; defaults 34.6% vs model expectation | **Bank:** NPL ↑, RWA ↑, earnings miss. **Consumers:** approved borrowers over-levered into default |
| **False positive** (over-alert) | Unnecessary full retrain USD 2–5M | **Business line:** lost loan volume. **Consumers:** credit access denied—liquidity shock in recession |
| **Performance drift misread** | ΔAUC small but calibration broken | **Model risk officers:** career/regulatory exposure. **Communities:** if cut-offs tighten late, disproportionate knock-on to vulnerable borrowers |
| **Jurisdictional misconfiguration** | SG fairness rules applied to US feed | **Bank legal:** ECOA violation risk. **Consumers:** unlawful discrimination support |
| **US WARN ignored** | Continue rollout; state AG / private litigation | **Legal/ESG:** Reg B intent shift does not erase **state law** or reputational risk |
| **SG FAIL ignored** | Expand live book under MAS scrutiny | **ASEAN leadership:** licence/reputation. **Consumers:** unfair denial or predatory extension |

---

## Part III — Quantitative component (Option C)

### 3.1 Data and score convention

| Period | Rows | Median income (SGD) | Mean loan | Unemployment | Default rate | Approval |
|--------|------|---------------------|-----------|--------------|--------------|----------|
| Training 2022–23 | 5,000 | 47,832 | 77,580 | 2.8% | 24.9% | 98.5% |
| Live 2025–26 | 3,000 | 42,454 | 92,349 | 6.7% | 34.6% | 90.0% |

**Score direction:** Higher `model_score` = lower risk. For default discrimination we use **P(default) proxy = 1 − model_score** in AUC/Gini.

### 3.2 Metric definitions and computed values (baseline)

#### (1) ΔAUC — rank-order performance drift

\[
\Delta\text{AUC} = \text{AUC}_{\text{train}} - \text{AUC}_{\text{live}}
\]

| Period | AUC | Gini |
|--------|-----|------|
| Training | **0.6312** | 0.2624 |
| Live | **0.6162** | 0.2325 |
| **ΔAUC** | **0.0150** | — |

**Interpretation:** Modest rank decay—would **PASS** both jurisdictions’ performance FAIL gates (US 10%, SG 6%). **Risk story is not in ΔAUC alone.**

#### (2) PSI — population stability of `model_score`

PSI compares training score distribution to live using decile bins anchored on training:

\[
\text{PSI} = \sum_i (\text{Act}_i - \text{Exp}_i)\,\ln\frac{\text{Act}_i}{\text{Exp}_i}
\]

| Feature | PSI |
|---------|-----|
| **model_score** | **0.4639** |
| income_sgd | 0.0495 |
| debt_to_income | 0.0307 |

**Low-score mass (<0.4):** 0.86% → 5.70% (**+4.84 pp**).

#### (3) ARR — approval rate ratio (Singapore path only)

\[
\text{ARR}_{\text{group}} = \frac{\text{Approval rate}_{\text{group}}}{\text{Approval rate}_{\text{Chinese}}}
\]

| Ethnicity (live) | Approval | ARR vs Chinese |
|------------------|----------|----------------|
| Chinese (ref) | 90.0% | 1.000 |
| Indian | 91.1% | 1.012 |
| Malay | 90.0% | 1.001 |
| Other | 88.1% | **0.979** |

**ARR_min = 0.979** — **PASS** SG floor 0.80 at baseline. Stress scenario `fairness_stress_sg` drives Malay ARR to **0.751** → fairness **FAIL** (demonstration only).

#### (4) Portfolio default-rate shock

\[
\Delta_{\text{default}} = 34.63\% - 24.86\% = \textbf{9.77 pp}
\]

Triggers **WARN** in US (≥8 pp); **FAIL** in SG (≥10 pp fail band at 10 pp boundary—implemented as FAIL at ≥10%).

### 3.3 Jurisdiction rule engine and the WARN / FAIL flip

| Check | Value | US_OCC rule | US status | SG_MAS rule | SG status |
|-------|-------|-------------|-----------|-------------|-----------|
| ΔAUC | 0.015 | FAIL ≥0.10 | **PASS** | FAIL ≥0.06 | **PASS** |
| PSI | 0.464 | WARN ≥0.20, FAIL ≥0.55 | **WARN** | FAIL ≥0.25 | **FAIL** |
| Low-score Δ | +4.84 pp | FAIL ≥15 pp | WARN path | FAIL ≥4 pp | **FAIL** |
| Default Δ | +9.77 pp | WARN ≥8 pp | **WARN** | FAIL ≥10 pp | **WARN/FAIL edge** |
| Fairness ARR | 0.979 | Disabled (advisory) | **ADVISORY** | FAIL <0.80 | **PASS** |

**Aggregation logic (political core):**

- **US:** FAIL only if **performance AND drift** both hard-fail → with PSI 0.464, drift is WARN not FAIL → **overall WARN**. Fairness suppressed.
- **SG:** **Any** hard fail → PSI and low-score share trigger → **overall FAIL**.

**Escalation text:**

- **US WARN:** *Trigger independent validation under OCC 2026-13; document for audit trail.* Parallel **fairness advisory:** state-law litigation / ESG exposure if disparities exist but are no longer federal disparate-impact cases.
- **SG FAIL:** *Recommend pause on live rollout expansion; FEAT outcome review; committee pack.*

### 3.4 Sensitivity analysis (distribution shift scenarios)

Results in `Task3_outputs/Task3_sensitivity.csv` and `Task3_outputs/Task3_sensitivity_pivot.csv`:

| Scenario | US_OCC | SG_MAS |
|----------|--------|--------|
| baseline | WARN | FAIL |
| income_shock | WARN | FAIL |
| score_inflation | WARN | FAIL |
| default_shock | WARN | FAIL |
| fairness_stress_sg | WARN | FAIL |

**Conclusion:** Under every simulated shock, **Singapore remains FAIL while US remains WARN**—the regulatory aggregation is stable; the **flip is structural**, not noise.

### 3.5 US / Singapore data-path divergence (BISG lecture closure)

| Mode | Ethnicity handling | Rationale |
|------|-------------------|-----------|
| **US_OCC** | **Strip** `ethnicity`, `gender` at ingest | ECOA: non-mortgage credit often lacks lawful race collection; **fairness-under-unawareness** |
| **Exploratory US** | BISG stub (surname + geography) | CFPB BSIG lecture: proxy for **monitoring**, not for automated scoring |
| **SG_MAS** | **Use native ethnicity** | FEAT outcome audit feasible; no US-style BISG fiction required |

---

## Part IV — Human judgement cannot be outsourced

Automated outputs stop at **evidence packs**. The following require **Standard Chartered’s Model Risk Committee / CCO**:

| # | Decision | Why automation must not decide |
|---|----------|--------------------------------|
| 1 | **Physical cut-off adjustment** on `model_score` | Trade-off: immediate P&L vs future NPL; only humans hold risk appetite |
| 2 | **Whether to launch full model retrain** (USD millions, 6–12 months) | WARN ≠ mandatory retrain under US principles; business owns ROI |
| 3 | **Whether to file proactive MAS notification** | No API for “notify MAS”; judgement on licence/reputation |
| 4 | **US BISG exploratory run and board inclusion** | Litigation/ESG advisory—not algorithmic PASS/FAIL |
| 5 | **Halt Singapore rollout vs continue with enhanced monitoring** | SG FAIL is recommendation; only committee can stop product |
| 6 | **Override fairness-under-unawareness for US production** | Legal violation risk if ethnicity reintroduced to satisfy “global dashboard green” |

Lecture anchor: *“Judgement cannot be outsourced”* — SCB ModelGuard **informs** judgement; it does not **replace** accountability.

---

## Part V — Option C deliverable scope (not Option A)

This project follows **Option C** (design + quantitative analysis). The script `Task3_run.py` is a **measurement instrument** for ΔAUC, PSI, ARR, and sensitivity scenarios—not a standalone “Option A working prototype” submission. We do **not** ship a separate SHAP/LIME explainability module (listed only as future work in the management deck).

**Option C requires:** threshold methodology in `Task3_jurisdictions.yaml`, baseline metrics in `Task3_outputs/`, and jurisdiction-differentiated conclusions (US WARN vs SG FAIL).

## Part VI — Architecture & failure modes (concise)

```
CSV (train/live) → metrics engine → YAML jurisdiction evaluator → PASS/WARN/FAIL + narrative report
```

| Failure mode | Consequence | Mitigation |
|--------------|-------------|------------|
| Rule change mid-quarter | Wrong status | Versioned `Task3_jurisdictions.yaml` |
| Jurisdiction misconfiguration | US ethnicity leak | `strip_fields` guard in US_OCC |
| Model drift undetected | Credit losses | PSI + calibration deciles |
| Contradictory jurisdictions | Operational paralysis | Explicit dual reports, not blended score |

**Out of scope:** Legal opinions, auto-decline, BISG implementation, GenAI governance (wrong model class).

---

## Part VII — Team data collaboration (5%)

Synthetic dataset generation and RegTech scenario design collaborated with:

| Name | Matriculation | Email |
|------|---------------|-------|
| CHEN SHIYU | G2505198B | shiyu014@e.ntu.edu.sg |
| LIU YU | G2505967E | liuy0296@e.ntu.edu.sg |
| LIU YUAN | G2506419B | liuy0301@e.ntu.edu.sg |

---

## References (selected)

- OCC Bulletin 2026-13: https://www.occ.treas.gov/news-issuances/bulletins/2026/bulletin-2026-13.html  
- CFPB AI adverse action (2024): https://www.consumerfinance.gov/about-us/newsroom/cfpb-issues-guidance-on-credit-denials-by-lenders-using-artificial-intelligence/  
- Reg B rewrite commentary: https://www.consumerfinancialserviceslawmonitor.com/2026/04/cfpb-finalizes-regulation-b-subpart-a-rule-largely-as-proposed/  
- MAS fairness principles in AI/ML (FEAT thematic review, 2022): https://www.mas.gov.sg/publications/monographs-or-information-paper/2022/implementation-of-fairness-principles-in-financial-institutions-use-of-artificial-intelligence-and-machine-learning  
- Course lectures: *Lecture 1 Part 3.pdf*; *CFPB BSIG.pdf*

*Generated metrics: `Task3_outputs/Task3_metrics_baseline.json`. Run: `python Task3_run.py`.*
