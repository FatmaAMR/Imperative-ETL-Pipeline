from src import load_data, show_data_info, auto_handle_missing


df = load_data("csv", "data/raw/dirty_cafe_sales.csv")

show_data_info(df, "Original Data")

df_cleaned = auto_handle_missing(df)

show_data_info(df_cleaned, "Cleaned Data")
