# Task 1 — Selection and Research

> **Full integrated treatment (selection + values + quant): see `Task3_design.md` Part I.**


## 1. Regulated entity

**Standard Chartered PLC** (listed; prudential supervision in multiple jurisdictions)

| Jurisdiction | Supervisor(s) | Relevance to this project |
|--------------|---------------|---------------------------|
| **United States** | OCC (national bank subsidiaries), Federal Reserve, FDIC | Retail/credit models of US operations; OCC **Bulletin 2026-13** (Apr 2026) replaces SR 11-7 for large banks |
| **Singapore** | **MAS** (Monetary Authority of Singapore) | Regional hub; **FEAT Principles** and **AI/ML model risk management** papers (2024–2025) for digital and credit analytics |

**Why Standard Chartered:** It is a real, named global bank with material US and Singapore footprints—ideal for demonstrating one model (**SCB-CS-001**) judged under **divergent 2026 regulatory trajectories**.

**References / URLs**

- Standard Chartered Group: https://www.sc.com/en/
- OCC Bulletin 2026-13: https://www.occ.treas.gov/news-issuances/bulletins/2026/bulletin-2026-13.html
- MAS fairness principles in AI/ML (FEAT thematic review, 2022): https://www.mas.gov.sg/publications/monographs-or-information-paper/2022/implementation-of-fairness-principles-in-financial-institutions-use-of-artificial-intelligence-and-machine-learning
- MAS technology risk / AI guidance portal: https://www.mas.gov.sg/development/fintech

---

## 2. Domain selected

**Credit scoring + model risk management (MRM)** with a **fair-lending / algorithmic fairness** overlay.

This sits squarely in Lecture 1 (fair lending history, disparate impact reversal, MRM timelines) and the synthetic **SCB-CS-001** retail portfolio shift scenario.

---

## 3. Political and regulatory divergence (what politicians chose differently)

### United States — deregulatory shift on *fairness liability*, continued pressure on *traditional model risk*

| Theme | Policy choice | Effect on RegTech |
|-------|---------------|-------------------|
| **Disparate impact** | Executive and agency posture (2025–2026) to **reduce outcome-based liability**; Regulation B rewrite toward **intent** | Statistical approval-rate tests lose **federal enforcement** teeth; tools re-labelled litigation/ESG advisory |
| **HMDA / data infrastructure** | World's richest fair-lending **data** built, now **curtailed** in use | Monitoring still possible; **regulatory consequence** of disparity alerts weakens |
| **OCC 2026-13 (MRM)** | **Principles-based** replacement for SR 11-7; **GenAI/agentic AI explicitly out of scope** | **Traditional credit scores remain governed**; validation, drift, revalidation still expected |
| **CFPB fair access / debanking** | Shift from redlining enforcement to **lawful-business debanking** politics | Different product narrative than fair-lending analytics |

**Biden-era explainability (contrast):** CFPB guidance on AI adverse action (May 2024) — https://www.consumerfinance.gov/about-us/newsroom/cfpb-issues-guidance-on-credit-denials-by-lenders-using-artificial-intelligence/

**Trump-era Reg B (contrast):** https://www.consumerfinancialserviceslawmonitor.com/2026/04/cfpb-finalizes-regulation-b-subpart-a-rule-largely-as-proposed/

### Singapore — tightening *conduct + AI governance*, no US-style race data mandate

| Theme | Policy choice | Effect on RegTech |
|-------|---------------|-------------------|
| **FEAT** | Fairness, Ethics, Accountability, Transparency for AI/finance | **Outcome and governance** scrutiny; ethnicity in local data can support monitoring |
| **MAS AI MRM** | Ongoing robustness under **distribution shift** | Stricter operational response to PSI / performance decay than US “WARN-only” postures |
| **Fair lending data** | No US HMDA equivalent; **native ethnicity** often available in domestic credit operations | Direct ARR-style monitoring feasible (unlike US non-mortgage ECOA constraints) |

### Side-by-side (lecture taxonomy)

| Dimension | US (2026 trajectory) | Singapore |
|-----------|----------------------|-----------|
| Core statute for credit fairness | ECOA / Reg B | MAS conduct + FEAT (not civil-rights-data infrastructure) |
| Outcome-based standard | Disparate impact **retreating** | FEAT **outcome monitoring** emphasis |
| AI credit governance | OCC 2026-13 (**excludes GenAI only**) | MAS 2024–25 AI MRM **tightening** |
| Mandatory race reporting | HMDA (mortgage); weak for non-mortgage | No HMDA analogue |

---

## 4. Rationale for pairing US + Singapore

1. **Same bank, same model class** (retail PD-style score)—cleanest classroom story for jurisdiction-aware tooling.
2. **Maximum regulatory contrast in 2026:** US **splits** MRM (still binding on traditional models) from fairness enforcement (weakening); Singapore **does not** copy that split.
3. **Data realism:** Course synthetic set includes Singapore **ethnicity** fields—supports FEAT path while US path demonstrates **fairness-under-unawareness** + optional **BISG** exploratory stub (see CFPB proxy methodology lecture).

---

## 5. Scope boundary for later tasks

- Entity: **Standard Chartered** (not a fictional bank).
- Domain: **Credit scoring under MRM**, not AML, not reputational-risk sentiment tools.
- Jurisdictions implemented in Task 3: **US_OCC** vs **SG_MAS** (not EU/OSFI, though cited as comparators in lectures).
