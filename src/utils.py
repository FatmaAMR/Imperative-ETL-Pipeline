import pandas as pd

def show_data_info(df: pd.DataFrame, name: str = "Dataset") -> None:
    """
    Display basic information about the DataFrame imperatively:
    - Shape (rows, columns)
    - Columns
    - Number of missing values per column
    - Data types of columns
    - First 5 rows (preview)
    """
    print(f"\n=== Info for {name} ===")
    print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    
    print("\nColumns and Data Types:")
    print(df.dtypes)
    
    print("\nMissing Values per Column:")
    print(df.isna().sum())
    
    print("\nFirst 5 Rows Preview:")
    print(df.head())
    
    print("="*30)



def get_columns_with_missing_values(df: pd.DataFrame) -> list:
    """
    Return a list of column names that contain missing values.
    Also prints how many missing values each column has.
    """
    missing_columns = []

    print("\n=== Columns With Missing Values ===")
    for col in df.columns:
        missing_count = df[col].isna().sum()
        if missing_count > 0:
            print(f"- {col}: {missing_count} missing")
            missing_columns.append(col)

    if not missing_columns:
        print("No missing values found in any column.")

    print("="*35)
    return missing_columns
