# from pathlib import Path
import pandas as pd
import numpy as np

col_names = [
    "timestamp",
    "store_name",
    "customer_name",
    "products",
    "total_price",
    "payment_method",
    "card_number"
]
to_drop = [
    'customer_name',
    'card_number'
    ]

# file_path = "reports_from_branches/chesterfield_25-08-2021_09-00-00.csv"

def turn_file_into_dataframe(file_path, col_names):
    df = pd.read_csv(file_path, names=col_names)
    df = df.drop(to_drop, axis=1)
    return df

df = turn_file_into_dataframe("reports_from_branches/chesterfield_25-08-2021_09-00-00.csv", col_names)

print(df)

