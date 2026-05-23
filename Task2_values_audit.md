# Task 2 — Values Audit

> **Full integrated treatment: see `Task3_design.md` Part II.**


*Hypothetical company aligned with Task 3 tool (**SCB ModelGuard**). Domain: credit scoring + model risk for a global bank client.*

---

## 1. Company mission, stage, and aspirations

**Mission statement:**  
*“Make cross-border model risk visible before regulators and customers pay the price.”*

**Company profile — Meridian Model Assurance Pte Ltd (fictional)**

| Attribute | Choice |
|-----------|--------|
| **What we are good at** | Quantitative drift detection, jurisdiction rule engines, audit-grade documentation for model committees |
| **Stage** | Series A RegTech; ~35 staff (18 engineering, 10 quant/PM, 7 legal-policy) |
| **Revenue aspiration** | USD 8–12M ARR within 24 months from 4–6 anchor bank contracts |
| **Cost posture** | Lean cloud SaaS; heavy investment in policy-as-config, not bespoke consulting |
| **Geographic coverage** | Singapore HQ; sales in London, New York, Dubai; **US + ASEAN** as first compliance rule packs |

**Core values:** Intellectual honesty (report FAIL states), jurisdictional humility (no “global threshold”), client confidentiality, and **human accountability** for final credit decisions.

---

## 2. Whose perspective does the tool serve?

**Primary:** The paying client’s **Chief Compliance Officer (CCO) / Head of Model Risk**—they fund the licence and need defensible packs for **OCC validation** and **MAS governance forums**.

**Secondary:** **Regulators** (indirect)—outputs formatted as evidence, not advocacy.

**Tertiary:** **Consumers**—only through fairer outcomes if the bank *acts* on alerts; the tool does not contact applicants.

### Stakeholder tensions (evidence-based)

| Tension | Evidence | Our choice |
|---------|----------|------------|
| CCO wants **PASS** narratives; model risk wants **WARN/FAIL** | OCC 2026-13 footnote: guidance is non-binding yet **unsafe/unsound** actions still enforceable | Serve **model risk truth first**, CCO second—sell “early warning” not “green paint” |
| US fairness advocates vs bank | CFPB 2024 AI adverse-action guidance vs 2026 Reg B **intent** shift | US mode: **strip ethnicity**, MRM hard / fairness advisory |
| MAS outcomes vs business growth | FEAT expects monitoring when banks expand digital lending | SG mode: **stricter FAIL** on drift to protect licence renewal in ASEAN |
| Consumer vs shareholder | Higher decline rates reduce defaults but access complaints | Surface **portfolio default-rate rise** separately from approval ARR |

**Market sizing:** Global MRM RegTech spend is a fraction of USD 270B compliance spend (lecture figure); we target **>$30bn asset US branches + Singapore HQs**—roughly 40 institutions, 10–15 realistically addressable, ACV USD 400k–1.2M. Choice driven by **team competency** (ex-risk modellers) more than TAM fantasy.

---

## 3. Genuine risk measurement vs compliance documentation?

**Position:** The tool must **measure genuine risk** first; compliance labels are downstream.

### Design choice A — *Included for risk, not required for US compliance*

**Decile calibration table on live data** (`actual_default` by `model_score` bin).

- **Risk value:** Detects **calibration collapse** when macro default rates rise even if rank-order AUC is stable.
- **Not federally mandated** as a specific chart under OCC 2026-13, but is standard in model validation practice.

### Design choice B — *Excluded to avoid documentation theatre*

**Auto-generated “fair lending cleared” PDF for US** based on ethnicity ARR.

- Would be **documentation over substance** after disparate-impact retreat and **ECOA unawareness**.
- We **suppress** US ethnicity metrics and document **BISG exploratory** as optional, non-scoring.

---

## 4. Who bears the cost if the tool is wrong?

| Failure mode | Harm | Primary stakeholder hurt |
|--------------|------|---------------------------|
| **False negative** (drift not flagged) | Unexpected credit losses, capital surprise | **Bank shareholders / CRO**; secondary: borrowers in bad vintages |
| **False positive** (flag stable model) | Unnecessary validation spend, delayed product launch | **Business line / retail bank P&L**; tool vendor credibility if chronic |
| **Performance drift misread** | Wrong retrain timing | **Model risk team** (career/regulatory), **customers** if cut-offs tighten late |
| **Jurisdictional misconfiguration** (SG rules on US data) | **Unlawful use of ethnicity** in US decisioning support; exam finding | **Bank legal / CCO**; **consumers** if discriminatory denial patterns |
| **US fairness advisory ignored** | Litigation or state-law exposure while federal bar lowers | **Bank legal**; minority applicants if disparity real |
| **SG FAIL ignored** | MAS remediation, licence/reputational damage | **Bank ASEAN leadership**; **consumers** via reduced access or unfair denials |

**Vendor liability:** We lose renewal if **false negatives** dominate; we are replaced if **false positives** waste committee time. We disclose uncertainty in reports (WARN vs FAIL not legal verdicts).

---

## 5. Honest uncertainties

- Synthetic data—not demonstrated on real SCB portfolios.
- No live legal review of Reg B final text at submission time.
- BISG not implemented; US exploratory fairness is procedural stub only.
