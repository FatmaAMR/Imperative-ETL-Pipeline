from src import load_data, show_data_info

df = load_data("csv", "data/raw/dirty_cafe_sales.csv")

show_data_info(df, "Cafe Sales Data")
