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


cur.execute("""CREATE TABLE IF NOT EXISTS branchs
    (branch_id SERIAL PRIMARY KEY,
    branch TEXT UNIQUE)
""")

cur.execute("""CREATE TABLE IF NOT EXISTS baskets
    (basket_id SERIAL PRIMARY KEY,
    basket_item TEXT,
    item_price FLOAT)
""")

cur.execute("""CREATE TABLE IF NOT EXISTS transactions
    (transaction_id SERIAL PRIMARY KEY,
branch_id INT NOT NULL,
basket_id INT NOT NULL,
total_price FLOAT,
payment_type TEXT,
date_time TIMESTAMP,
FOREIGN KEY(branch_id) REFERENCES branchs(branch_id),
FOREIGN KEY(basket_id) REFERENCES baskets(basket_id))
""")

print("Table created successfully")

conn.commit()
conn.close()