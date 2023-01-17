import os
import numpy as np
import pandas as pd
import psycopg2
import psycopg2.extras as extras

from cleaning import cleaning_and_arranging_df

file_path = "reports_from_branches/chesterfield_25-08-2021_09-00-00.csv"
column_names = [
    "date_time",
    "branch",
    "customer",
    "order_content",
    "total_price",
    "payment_type",
    "credit_card_number",
]
df = pd.read_csv(file_path, names=column_names)

cleaned_df = cleaning_and_arranging_df(df)

to_drop = ["customer", "credit_card_number"]


def dropping_pip(df):
    df = df.drop(to_drop, axis=1)
    return df


final_df = dropping_pip(cleaned_df)

print(final_df)

# conn = psycopg2.connect(
#     database="postgres",
#     user = "postgres",
#     password = "pass",
#     host = "127.0.0.1",
#     port = "5432"
# )


def execute_values(conn, df, table):

    tuples = [tuple(x) for x in df.to_numpy()]

    cols = ",".join(list(df.columns))
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


conn = psycopg2.connect(
    database="postgres", user="postgres", password="pass", host="localhost", port="5432"
)


# df = pd.read_csv('mockFileWithHeaders.csv')

execute_values(conn, final_df, "test_table")
