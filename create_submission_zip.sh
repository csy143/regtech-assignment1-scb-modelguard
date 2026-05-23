#!/bin/bash
# Assignment 1 Session 1 — submission ZIP (Tasks 1–3 documents)
set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
ZIP_NAME="Assignment1_Session1_SUBMIT.zip"

echo "Regenerating Task3 outputs..."
MPLCONFIGDIR="${MPLCONFIGDIR:-/tmp/mpl}" python3 Task3_run.py

echo "Creating $ZIP_NAME ..."
rm -f "$ZIP_NAME"
zip -r "$ZIP_NAME" \
  README.md \
  Task1_selection_research.md \
  Task2_values_audit.md \
  Task3_summary_one_page.md \
  Task3_design.md \
  Task3_management_deck.pdf \
  Task3_audio_walkthrough.mp3 \
  Task3_jurisdictions.yaml \
  Task3_model_card.yaml \
  Task3_outputs/Task3_report_US_OCC.md \
  Task3_outputs/Task3_report_SG_MAS.md \
  Task3_outputs/Task3_metrics_baseline.json \
  Task3_outputs/Task3_sensitivity.csv \
  Task3_outputs/Task3_sensitivity_pivot.csv \
  Task3_outputs/Task3_evaluations.json \
  Task3_outputs/figures \
  -x "*.DS_Store"

echo "Done: $(pwd)/$ZIP_NAME"
unzip -l "$ZIP_NAME" | tail -20
