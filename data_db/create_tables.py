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
(ID SERIAL PRIMARY KEY,
Date_Time TEXT,
Branch TEXT,
Full_name TEXT,
Proudcts TEXT,
Price FLOAT,
Payment_method TEXT,
Card_number TEXT);
""")

print("Table created successfully")

conn.commit()
conn.close()