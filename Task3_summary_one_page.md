# SCB ModelGuard — One-Page Summary for Business Leaders

**To:** Retail banking executive committee and board risk committee  
**From:** Meridian Model Assurance — SCB ModelGuard product team  
**Re:** Standard Chartered retail score **SCB-CS-001** after the 2025–2026 economic downturn  
**Date:** May 2026

---

### What problem does this solve?

Today, compliance is often tracked in **static Excel trackers and Word memos** that snapshot last quarter’s approval rate. Those tools cannot answer a harder 2026 question: *“The economy changed—does the same credit score still mean the same thing?”*

Between 2022–2023 and 2025–2026 on our demonstration portfolio, median customer income fell about **eleven percent**, unemployment **more than doubled**, average loan size rose sharply, and **one in three** live applications ultimately defaulted versus **one in four** during training. Approvals had to fall from roughly **ninety-nine percent to ninety percent** just to keep the bank solvent. A spreadsheet comparison of “approvals last year vs this year” would show a gap—but not *why* the scoring engine itself may be misleading risk committees.

**SCB ModelGuard** is a live radar, not a filing cabinet. It watches whether the bank’s score still ranks risky customers correctly, whether the **shape of the applicant pool** has changed, and whether approval patterns remain fair—then translates results separately for **US** and **Singapore** supervisors.

---

### What did we find on the same book of business?

On identical underlying applications, the tool gives **two different answers**:

| Region | Traffic light | Plain-English meaning |
|--------|---------------|------------------------|
| **United States** | **Yellow (WARN)** | “Your traditional credit model still needs a serious validation review—population shift is real—but federal rules no longer treat statistical fairness alone as an automatic emergency. Keep lending if you document model-risk work; **separately** watch state lawsuits and ESG reputational risk.” |
| **Singapore** | **Red (FAIL)** | “The score distribution has moved too far for MAS-style AI governance. **Stop expanding** this model to more live volume until a human committee signs off. Fairness metrics are also watched here using ethnicity data Singapore allows.” |

This is the **compliance paradox**: one model, one data feed, two national laws. The tool is not “inconsistent”—**the politics are**.

---

### Why yellow in America but red in Singapore?

**Not because America is lax on credit risk.** OCC rules in 2026 still apply fully to **classic** credit scores (only generative AI is carved out). We measured a **large shift in who receives low scores**—a warning sign that the model’s world has changed. Washington’s framework, however, now emphasises **bank judgement and validation paperwork** before forcing a hard stop, and **removed federal teeth** from ethnicity-based statistical tests. So the product flashes **yellow**: escalate model validation, refresh documentation, but do not pretend fairness statistics are a federal tripwire.

**Singapore is stricter on drift.** The same shift crosses tighter lines: score instability, more weak applicants, and a **ten-point jump** in portfolio defaults. MAS expects **outcome stewardship** under FEAT—not merely a memo saying “we reviewed the model.” Hence **red**: pause growth, convene the committee, prepare a root-cause pack.

---

### What we will not pretend

- The tool does **not** approve or reject loans.  
- It does **not** replace lawyers on US state fair-lending exposure.  
- It does **not** automatically email MAS—that is a human governance choice.  
- It uses **synthetic data** for class; production would add explainability for declined customers.

---

### If you remember only one sentence

**SCB ModelGuard tells you when the economic weather changed your credit model’s meaning—and tells each country’s regulator the truth their law demands, even when those truths conflict.**

---

*Team: CHEN SHIYU (G2505198B), LIU YU (G2505967E), LIU YUAN (G2506419B). Technical detail: Task3_design.md. Metrics run: `python Task3_run.py`.*
