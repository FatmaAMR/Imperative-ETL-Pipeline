from src import (
    load_data, auto_handle_missing,print_to_console, save_csv, save_json, save_plot, save_summary_report
)
from src.visualize_data import plot_bar, plot_line, plot_histogram
import pandas as pd

# 1. Load data
df = load_data("csv", "data/raw/dirty_cafe_sales.csv")
print_to_console(df, "Original Data")

# 2. Clean missing values
df_cleaned = auto_handle_missing(df)
print_to_console(df_cleaned, "Cleaned Data")

# 3. Convert types
df_cleaned["Quantity"] = pd.to_numeric(df_cleaned["Quantity"], errors="coerce")
df_cleaned["Price Per Unit"] = pd.to_numeric(df_cleaned["Price Per Unit"], errors="coerce")
df_cleaned["Total Spent"] = pd.to_numeric(df_cleaned["Total Spent"], errors="coerce")
df_cleaned["Transaction Date"] = pd.to_datetime(df_cleaned["Transaction Date"], errors="coerce")
df_cleaned = auto_handle_missing(df_cleaned)
print_to_console(df_cleaned, "Cleaned & Typed Data")

# 4. Save CSV / JSON
save_csv(df_cleaned, "cleaned_cafe_sales.csv")
save_json(df_cleaned, "cleaned_cafe_sales.json")

# 5. Visualization
tasks = [
    {"type": "bar", "x": "Location", "y": "Total Spent"},
    {"type": "line", "x": "Transaction Date", "y": "Total Spent"},
    {"type": "hist", "col": "Total Spent", "bins": 10}
]

for task in tasks:
    if task["type"] == "bar":
        if task["x"] in df_cleaned.columns and task["y"] in df_cleaned.columns:
            print(f"[INFO] Plotting Bar Chart: {task['y']} by {task['x']}")
            fig = plot_bar(df_cleaned, task["x"], task["y"])
            save_plot(fig, f"{task['y']}_by_{task['x']}_bar.png")

    elif task["type"] == "line":
        if task["x"] in df_cleaned.columns and task["y"] in df_cleaned.columns:
            df_sorted = df_cleaned.sort_values(task["x"])
            print(f"[INFO] Plotting Line Chart: {task['y']} over {task['x']}")
            fig = plot_line(df_sorted, task["x"], task["y"])
            save_plot(fig, f"{task['y']}_over_{task['x']}_line.png")

    elif task["type"] == "hist":
        if task["col"] in df_cleaned.columns:
            print(f"[INFO] Plotting Histogram: {task['col']}")
            fig = plot_histogram(df_cleaned, task["col"], bins=task.get("bins", 10))
            save_plot(fig, f"{task['col']}_histogram.png")

# 6. Save summary.txt1
save_summary_report("summary.txt")

print("\n[INFO] All visualizations completed and saved.")
