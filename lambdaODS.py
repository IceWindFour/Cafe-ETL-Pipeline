import os
import numpy as np
import pandas as pd
import psycopg2
import psycopg2.extras as extras

file_path = "reports_from_branches/chesterfield_25-08-2021_09-00-00.csv"
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
    df[['product_name','price']] = pd.DataFrame(df.order_content.tolist(), index= df.index)

    #striping whitespaces
    df['price'] = df['price'].str.strip()
    df['product_name'] = df['product_name'].str.strip()

    #drop old columns
    df = df.drop(columns=["order_content"])

    #rearrange columns
    new_col = ["date_time", "branch", "customer", "product_name","price", "total_price", "payment_type","credit_card_number"]
    df = df[new_col]

    return df

df = cleaning_and_arranging_df(df)

drop_for_order_details = ['customer','product_name','price','credit_card_number',]
drop_for_order_products = ['date_time','branch','customer','total_price','payment_type','credit_card_number',]
drop_for_products_table = ['date_time','branch','customer','price','total_price','payment_type','credit_card_number',]

drop_for_branch = ["product_name","price","date_time", "customer", "total_price", "payment_type", "credit_card_number"]
drop_for_product = ["branch","price","date_time", "customer", "total_price", "payment_type", "credit_card_number"]
drop_for_order = ["customer","branch","product_name","credit_card_number","price"]

def dropping_colums(df,drop_cols):
    df = df.drop(drop_cols, axis=1)
    return df

order_details_df = dropping_colums(df, drop_for_order_details)
order_products_df = dropping_colums(df, drop_for_order_products)
products_table_df = dropping_colums(df, drop_for_products_table)
products_table_df = products_table_df.drop_duplicates(subset=['product_name'])

branch_df = dropping_colums(df, drop_for_branch)
branch_df = branch_df.drop_duplicates()
product_df = dropping_colums(df, drop_for_product)
product_df = product_df.drop_duplicates()
order_df = dropping_colums(df, drop_for_order)
# product_df = product_df.sort_values(by='product_name')


# print(branch_df)
# print(product_df)
# print(order_df)


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


conn = psycopg2.connect(database="postgres", user = "postgres", password = "pass", host = "localhost", port = "5432")

execute_values(conn, branch_df, 'branchs')
execute_values(conn, product_df, 'products')
execute_values(conn, order_df, 'orders')







# def test_update(conn):
#     cur = conn.cursor()
#     cur.execute("""UPDATE products_table
#     SET product_id_fk = product_id
#     FROM orders_products_table
#     WHERE product_id_fk is null;
#     """)
#     conn.commit()
#     conn.close()


# def execute_values(conn, df, table, cols):

#     tuples = [tuple(x) for x in df.to_numpy()]

#     # cols = ','.join(list(df.columns))
#     # SQL query to execute
#     query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
#     cursor = conn.cursor()
#     try:
#         extras.execute_values(cursor, query, tuples)
#         conn.commit()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print("Error: %s" % error)
#         conn.rollback()
#         cursor.close()
#         return 1
#     print("the dataframe is inserted")
#     cursor.close()


# conn = psycopg2.connect(database="postgres", user = "postgres", password = "pass", host = "localhost", port = "5432")

# execute_values(conn, order_details_df, 'orders_details_table', col_orders_details_table)
# execute_values(conn, order_products_df, 'orders_products_table', col_orders_products_table)
# execute_values(conn, products_table_df, 'products_table', col_products_table)

# test_update(conn)