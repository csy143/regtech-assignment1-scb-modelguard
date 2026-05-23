"""
US exploratory fair-lending module (stub).

Per CFPB BISG methodology (surname + geography), US regulators may estimate
race/ethnicity proxies when prohibited variables are not collected in non-mortgage
credit files. SCB ModelGuard does NOT implement BISG inference in this assignment
build — OCC MRM mode strips ethnicity at ingest (fairness-under-unawareness).

To extend: ingest US applicant surname + ZIP, load Census surname tables,
compute posterior race probabilities, run exploratory disparity reports marked
ADVISORY ONLY (no automatic PASS/FAIL on US_OCC path).
"""

EXPLORATORY_ONLY = True
REGULATORY_REF = "CFPB BISG proxy methodology; Lecture BSIG deck"
