import psycopg2
import pandas as pd


# PostgreSQL connection parameters
host = "postgres"
port = "5432"
database = "de_db"
user = "de_user"
password = "de_pass"

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)
cur = conn.cursor()

# --- 1. CREATE TABLES ---

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    price NUMERIC
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    product_id INT REFERENCES products(product_id),
    quantity INT,
    order_date DATE
)
""")

conn.commit()
print("Tables created successfully!")

# --- 2. LOAD CSV DATA ---

# Users
df_users = pd.read_csv("data/users.csv")
for _, row in df_users.iterrows():
    cur.execute(
        "INSERT INTO users (user_id, name, email) VALUES (%s, %s, %s) ON CONFLICT (user_id) DO NOTHING",
        (row['user_id'], row['name'], row['email'])
    )

# Products
df_products = pd.read_csv("data/products.csv")
for _, row in df_products.iterrows():
    cur.execute(
        "INSERT INTO products (product_id, product_name, price) VALUES (%s, %s, %s) ON CONFLICT (product_id) DO NOTHING",
        (row['product_id'], row['product_name'], row['price'])
    )

# Orders
df_orders = pd.read_csv("data/orders.csv")
for _, row in df_orders.iterrows():
    cur.execute(
        """INSERT INTO orders (order_id, user_id, product_id, quantity, order_date)
           VALUES (%s, %s, %s, %s, %s)
           ON CONFLICT (order_id) DO NOTHING""",
        (row['order_id'], row['user_id'], row['product_id'], row['quantity'], row['order_date'])
    )

conn.commit()
print("Data loaded successfully!")

# --- 3. VALIDATE DATA ---

cur.execute("SELECT COUNT(*) FROM users")
print("Users rows:", cur.fetchone()[0])

cur.execute("SELECT COUNT(*) FROM products")
print("Products rows:", cur.fetchone()[0])

cur.execute("SELECT COUNT(*) FROM orders")
print("Orders rows:", cur.fetchone()[0])

cur.close()
conn.close()
