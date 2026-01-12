import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS keys (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    brand TEXT,
    duration TEXT,
    key TEXT,
    expiry TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT,
    user_id INTEGER,
    brand TEXT,
    duration TEXT,
    price INTEGER,
    status TEXT
)
""")

conn.commit()
