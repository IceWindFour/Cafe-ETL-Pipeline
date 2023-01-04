import os
import numpy as np
import pandas as pd
import psycopg2
import psycopg2.extras as extras

file_path = "../reports_from_branches/chesterfield_25-08-2021_09-00-00.csv"
column_names = ["date_time", "branch", "customer", "order_content", "total_price", "payment_type", "credit_card_number"]
df = pd.read_csv(file_path, names=column_names)

def cleaning_and_arranging_df(df):
     
    #spliting the first time, turn order_content into a list
    df["order_content"]= df["order_content"].str.split(',')

    #spliting the order_content into individual row
    df = df.explode("order_content")

    #spliting from the last -, turn it into a list
    df["order_content"] = df["order_content"].str.rsplit('-', 1)

    #putting the two list items into two newly created columns
    df[['basket_item','item_price']] = pd.DataFrame(df.order_content.tolist(), index= df.index)

    #striping whitespaces
    df['item_price'] = df['item_price'].str.strip()
    df['basket_item'] = df['basket_item'].str.strip()

    #drop old columns
    df = df.drop(columns=["order_content"])

    #rearrange columns
    new_col = ["date_time", "branch", "customer", "basket_item","item_price", "total_price", "payment_type","credit_card_number"]
    df = df[new_col]

    return df

df = cleaning_and_arranging_df(df)

drop_for_product = ["date_time", "branch", "customer", "total_price", "payment_type","credit_card_number"]
# drop_for_basket = ["date_time", "branch", "customer", "basket_item","item_price", "total_price", "payment_type","credit_card_number"]
drop_for_transaction = ["customer", "basket_item","item_price","credit_card_number"]

def dropping_colums(df,drop_cols):
    df = df.drop(drop_cols, axis=1)
    return df

product_df = dropping_colums(df, drop_for_product)
product_df.drop_duplicates()

transaction_df = dropping_colums(df, drop_for_transaction)
transaction_df["date_time"] = pd.to_datetime(transaction_df["date_time"])
transaction_df = transaction_df.drop_duplicates()



def execute_values(conn, df, table):

    tuples = [tuple(x) for x in df.to_numpy()]

    cols = ','.join(list(df.columns))
    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("the dataframe is inserted")
    cursor.close()

def execute_values_on_conflict(conn, df, table):
    
    tuples = [tuple(x) for x in df.to_numpy()]

    cols = ','.join(list(df.columns))
    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)

    query = query + "ON CONFLICT (basket_item) DO NOTHING"
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("the dataframe is inserted")
    cursor.close()


conn = psycopg2.connect(database="postgres", user = "postgres", password = "pass", host = "localhost", port = "5432")

execute_values_on_conflict(conn, product_df, 'products')
# execute_values(conn, basket_df, 'baskets')
execute_values(conn, transaction_df, 'transactions')