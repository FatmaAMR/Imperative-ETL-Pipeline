import pandas as pd

def remove_missing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows with any missing values.
    """
    initial_rows = len(df)
    df_cleaned = df.dropna()
    removed_rows = initial_rows - len(df_cleaned)
    print(f"[INFO] Removed {removed_rows} rows with missing values")
    return df_cleaned


def fill_missing(df: pd.DataFrame, fill_values: dict) -> pd.DataFrame:
    """
    Fill missing values with specified defaults.
    
    fill_values: dictionary where keys are column names and values are the default to fill.
    Example: {'sales': 0, 'region': 'Unknown'}
    """
    df_filled = df.copy()
    for col, default in fill_values.items():
        if col in df_filled.columns:
            missing_count = df_filled[col].isna().sum()
            df_filled[col].fillna(default, inplace=True)
            print(f"[INFO] Filled {missing_count} missing values in '{col}' with {default}")
    return df_filled


def auto_handle_missing(df: pd.DataFrame, strategy_num="mean", strategy_cat="mode") -> pd.DataFrame:
    """
    Automatically handles missing data based on column type.

    strategy_num:   'mean' or 'median' for numerical columns
    strategy_cat:   'mode' for categorical/text/boolean/datetime

    Returns a cleaned DataFrame.
    """
    df_clean = df.copy()
    
    for col in df_clean.columns:
        missing_count = df_clean[col].isna().sum()
        if missing_count == 0:
            continue   # skip column with no missing values

        col_type = df_clean[col].dtype
        
        print(f"\n[INFO] Handling '{col}' ({col_type}) - Missing values: {missing_count}")

        try:
            if pd.api.types.is_numeric_dtype(col_type):
                if strategy_num == "mean":
                    fill_value = df_clean[col].mean()
                else:
                    fill_value = df_clean[col].median()

                df_clean[col].fillna(fill_value, inplace=True)
                print(f"[OK] Numeric column → filled with {strategy_num}: {fill_value}")

            elif pd.api.types.is_categorical_dtype(col_type) or df_clean[col].dtype == object:
                fill_value = df_clean[col].mode(dropna=True)[0] if not df_clean[col].mode(dropna=True).empty else "Unknown"
                df_clean[col].fillna(fill_value, inplace=True)
                print(f"[OK] Categorical column → filled with mode: {fill_value}")

            elif pd.api.types.is_bool_dtype(col_type):
                fill_value = df_clean[col].mode(dropna=True)[0]
                df_clean[col].fillna(fill_value, inplace=True)
                print(f"[OK] Boolean column → filled with mode: {fill_value}")
                
            elif pd.api.types.is_datetime64_any_dtype(col_type):
                mq = df_clean[col].mode(dropna=True)
                if not mq.empty:
                    fill_value = mq[0]
                else:
                    fill_value = df_clean[col].dropna().min()

                df_clean[col].fillna(fill_value, inplace=True)
                print(f"[OK] Datetime column → filled with: {fill_value}")

            else:
                df_clean[col].fillna("Unknown", inplace=True)
                print(f"[WARN] Unknown dtype → filled with 'Unknown'")

        except Exception as e:
            print(f"[ERROR] Could not fill column '{col}': {e}")

    print("\n[INFO] Missing-data handling completed.")
    return df_clean

