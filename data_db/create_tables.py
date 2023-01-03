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

cur.execute("""CREATE TABLE IF NOT EXISTS orders_details_table
    (order_id SERIAL PRIMARY KEY,
date_time TEXT,
branch TEXT,
total_price FLOAT,
payment_type TEXT)
""")

cur.execute("""CREATE TABLE IF NOT EXISTS orders_products_table
    (order_id SERIAL,
product_id SERIAL PRIMARY KEY,
item TEXT,
price FLOAT,
quantity INT,
FOREIGN KEY(order_id)
REFERENCES orders_details_table(order_id));
""")

cur.execute("""CREATE TABLE IF NOT EXISTS products_table
    (product_id_fk INT,
products_name TEXT,
FOREIGN KEY(product_id_fk)
REFERENCES orders_products_table(product_id));
""")

print("Table created successfully")

conn.commit()
conn.close()