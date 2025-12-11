# ============================================================
# OUTPUT MODULE (Imperative Version)
# ============================================================
# This file handles saving processed datasets and reports.
# Team members must implement:
#
# 1. save_csv(df, path)
#    - Saves final DataFrame to CSV inside /data/processed/.
#    - Must confirm directory exists, create if not.
#
# 2. save_json(df, path)
#    - Saves dataset in JSON format.
#    - Ensure correct orientation (records).
#
# 3. save_summary_report(summary, path)
#    - Save text-based summaries or analysis reports.
#    - Example: missing-value report, correlation report.
#
# 4. print_to_console(df, max_rows = 10)
#    - Display sample rows to user.
#    - Useful for debugging.
#
# 5. save_plot(fig, path)
#    - Used by visualization module.
#    - Ensures /plots/ directory exists.
#
# NOTES:
# - All saving functions should print confirmation messages.
# - Handle errors (invalid paths, permission issues).
# - ALWAYS save processed results to /data/processed/
# ============================================================
import os
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# GLOBAL LOG MEMORY
# -----------------------------
LOG_MESSAGES = []  # كل الرسائل هتتحوش هنا

def log(message: str):
    """Print message to console and store in log for summary"""
    print(message)
    LOG_MESSAGES.append(str(message))

# -----------------------------
# Ensure directory exists
# -----------------------------
def ensure_dir(path: str):
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        log(f"[INFO] Created directory: {directory}")

# -----------------------------
# Save CSV
# -----------------------------
def save_csv(df: pd.DataFrame, filename: str):
    path = os.path.join("data", "processed", filename)
    try:
        ensure_dir(path)
        df.to_csv(path, index=False)
        log(f"[SUCCESS] CSV saved → {path}")
    except Exception as e:
        log(f"[ERROR] Could not save CSV: {e}")

# -----------------------------
# Save JSON
# -----------------------------
def save_json(df: pd.DataFrame, filename: str):
    path = os.path.join("data", "processed", filename)
    try:
        ensure_dir(path)
        df.to_json(path, orient="records", indent=4)
        log(f"[SUCCESS] JSON saved → {path}")
    except Exception as e:
        log(f"[ERROR] Could not save JSON: {e}")

# -----------------------------
# Print DataFrame to Console + Log
# -----------------------------
def print_to_console(df: pd.DataFrame, title: str = "", max_rows: int = 10):
    if title:
        log(f"\n===== {title} =====")
    log(df.head(max_rows).to_string())
    log("========================\n")

# -----------------------------
# Save Matplotlib Figure
# -----------------------------
def save_plot(fig, filename: str):
    path = os.path.join("plots", filename)
    try:
        ensure_dir(path)
        fig.savefig(path, bbox_inches='tight', dpi=300)
        log(f"[SUCCESS] Plot saved → {path}")
    except Exception as e:
        log(f"[ERROR] Could not save plot: {e}")

# -----------------------------
# Save all logs to summary.txt
# -----------------------------
def save_summary_report(filename="summary.txt"):
    path = os.path.join("data", "processed", filename)
    try:
        ensure_dir(path)
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(LOG_MESSAGES))
        print(f"[SUCCESS] Summary saved → {path}")
    except Exception as e:
        print(f"[ERROR] Could not save summary: {e}")
