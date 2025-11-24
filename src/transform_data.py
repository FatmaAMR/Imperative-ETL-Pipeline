# ============================================================
# TRANSFORMATION MODULE (Imperative Version)
# ============================================================

import pandas as pd

df = pd.read_csv('./data/raw/Sample - Superstore.csv') 

def filter_rows(df, condition):
    filtered = []
    for index, row in df.iterrows():
        if condition(row):
            filtered.append(row.to_dict())
    return pd.DataFrame(filtered)


def add_new_column(df, name, function):
    for index, row in df.iterrows():    
        df.at[index,name] = function(row)
    return df
    

def standardize_date_column(df, column):
    for index, row in df.iterrows():
        df.at[index, column] = pd.to_datetime(row[column]).strftime('%Y-%m-%d')
    return df
def aggregate_data(df, group_by_col, agg_col, method):
    totals = {}

    for index, row in df.iterrows():
        key = row[group_by_col]
        value = row[agg_col]

        if key not in totals:
            totals[key] = []

        totals[key].append(value)

    if method == 'sum':
        return {k: sum(v) for k, v in totals.items()}
    elif method == 'count':
        return {k: len(v) for k, v in totals.items()}
    elif method == 'mean':
        return {k: sum(v) / len(v) for k, v in totals.items()}


def sort_data(df, column, ascending=True):
    rows = df.to_dict('records')

    for i in range(len(rows)):
        for j in range(0, len(rows) - i - 1):
            if (ascending and rows[j][column] > rows[j+1][column]) or \
               (not ascending and rows[j][column] < rows[j+1][column]):
                rows[j], rows[j+1] = rows[j+1], rows[j]

    return pd.DataFrame(rows)

