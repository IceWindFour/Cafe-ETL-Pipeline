import os
import numpy as np
import pandas as pd


os.listdir(os.getcwd())

csv_files = []
for file in os.listdir(os.getcwd()):
    if file.endswith(".csv"):
        csv_files.append(file)
csv_files


dataset_dir = 'CSV_datasets'
try:
    mkdir = 'mkdir {0}'.format(dataset_dir)
    os.system(mkdir)
except:
    print("error")

print(mkdir)

for csv in csv_files:
    mv_file = "mv '{0}'{1}".format(csv, dataset_dir)
    os.system(mv_file)
    print(mv_file)