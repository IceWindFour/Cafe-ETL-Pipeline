#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
from pathlib import Path
import numpy as np


# In[2]:


#Checks working directory
get_ipython().system('dir')


# In[39]:


os.listdir(os.getcwd())


# In[40]:


def get_csv_file():
    csv_files = []
    for file in os.listdir(os.getcwd()):
        if file.endswith(".csv"):
            csv_files.append(file)
        else:
            pass
    return csv_files


# In[41]:


get_csv_file()


# In[42]:


def make_directory(csv_files,dataset_dir):
    dataset_dir = 'datasets'
    try:
        mkdir = 'mkdir {0}'.format(dataset_dir)
        os.system(mkdir)
    except:
        print("error")
    for csv in csv_files:
        mv_file = "mv '{0}' {1}".format(csv, dataset_dir)
        os.system(mv_file)
        print(mv_file)
    return
    


# In[56]:


# Defining the names of the columns
col_names = [
    "date_time",
    "branch",
    "customer_name",
    "products",
    "total_price",
    "payment_method",
    "card_number",
]


# In[57]:


#Asif's File path
file_path = "chesterfield_25-08-2021_09-00-00.csv"

# Undo this to test directory file_path = "reports_from_branches/chesterfield_25-08-2021_09-00-00.csv"


# In[58]:



def into_df(file_path:str,col_names:list = col_names) -> pd.DataFrame:
    """Converts the csv file to a pandas dataframe"""
    try:
        df = pd.read_csv(Path(file_path),names= col_names)
        return df
    except FileNotFoundError:
        print("No such file exists")


# In[59]:


drop_col = ["customer_name", "card_number"]

#Deletes the columns that have costumers personal details
def delete_col(df,colums_to_drop):
    try:
        df.drop(colums_to_drop,axis= 1,inplace= True)
        df["date_time"] = pd.to_datetime(df["date_time"])
        return df
    except:
        print('error')


# In[60]:


#Main
drop_col = ["customer_name", "card_number"]
into_df(file_path,col_names)
new_df = delete_col(into_df(file_path,col_names),drop_col)

#Reset index to start from 1
new_df.index =  np.arange(1, len(new_df) + 1)


# In[61]:


new_df


# In[ ]:




