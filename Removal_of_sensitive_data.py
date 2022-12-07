
import csv

import pandas as pd

def remove_sensitive_data(filename):
    df = pd.read_csv(f'{filename}')
    to_drop = [
    'Full Name',
    'Card Number'
    ]
    df = df.drop(to_drop, axis=1)
    return df

print(remove_sensitive_data('chesterfield_25-08-2021_09-00-00.csv'))



