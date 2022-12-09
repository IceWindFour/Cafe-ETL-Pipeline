import os
import numpy as np
import pandas as pd

#gets the current working directory
os.listdir(os.getcwd())

# Loops through the file directory and checks if the file is a csv file then appends the name of the file to the empty list
csv_files = []
for file in os.listdir(os.getcwd()):
    if file.endswith(".csv"):
        csv_files.append(file)
csv_files

#Creates a new folder "CSV_datasets" in the current directory. Exception handling if the file name already exists.
dataset_dir = 'CSV_datasets'
try:
    mkdir = 'mkdir {0}'.format(dataset_dir)
    os.system(mkdir)
except:
    print("error")

print(mkdir)

#Moves only the csv files to the new folder
for csv in csv_files:
    mv_file = "mv '{0}'{1}".format(csv, dataset_dir)
    os.system(mv_file)
    print(mv_file)
