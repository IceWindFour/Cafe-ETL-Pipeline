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


cur.execute("""CREATE TABLE IF NOT EXISTS products
    (product_id SERIAL PRIMARY KEY,
    basket_item TEXT UNIQUE,
    item_price FLOAT)
""")

cur.execute("""CREATE TABLE IF NOT EXISTS transactions
    (transaction_id SERIAL PRIMARY KEY,
branch TEXT NOT NULL,
total_price FLOAT,
payment_type TEXT,
date_time TIMESTAMP)
""")

cur.execute("""CREATE TABLE IF NOT EXISTS baskets
    (basket_item_id SERIAL PRIMARY KEY,
    transaction_id INT,
    product_id INT,
    FOREIGN KEY(product_id) REFERENCES products(product_id),
    FOREIGN KEY(transaction_id) REFERENCES transactions(transaction_id))
""")


print("Table created successfully")

conn.commit()
conn.close()