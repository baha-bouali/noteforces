import sqlite3

DB_NAME = "noteforces.db"


def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS NOTES(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tag TEXT,
                rating INTEGER, 
                ideas TEXT,
                time_spent INTEGER,
                editorial BOOLEAN,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()