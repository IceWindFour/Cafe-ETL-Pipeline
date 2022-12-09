import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user = "postgres",
    password = "pass",
    host = "127.0.0.1",
    port = "5432"
)

print("Opened datebase successfully")

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS order_table
    (date_and_time TEXT PRIMARY KEY,
branch_name TEXT,
item TEXT,
price FLOAT,
total_price FLOAT,
payment_type TEXT);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS orders_details_table
    (order_id SERIAL PRIMARY KEY,
branch_name TEXT,
total_price FLOAT,
payment_type TEXT,
date_and_time TEXT,
FOREIGN KEY(date_and_time)
REFERENCES order_table(date_and_time));
""")

cur.execute("""CREATE TABLE IF NOT EXISTS orders_products_table
    (order_id INT,
product_id SERIAL PRIMARY KEY,
item_price FLOAT,
quantity INT,
FOREIGN KEY(order_id)
REFERENCES orders_details_table(order_id));
""")

cur.execute("""CREATE TABLE IF NOT EXISTS products_table
    (product_id INT,
products_name TEXT,
FOREIGN KEY(product_id)
REFERENCES orders_products_table(product_id));
""")

cur.execute("""CREATE TABLE IF NOT EXISTS test_table
    (date_time TEXT,
branch TEXT,
item TEXT,
price float,
total_price float,
payment_type TEXT);
""")

print("Table created successfully")

conn.commit()
conn.close()