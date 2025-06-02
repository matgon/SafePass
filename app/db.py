import sqlite3

def get_db():
    conn = sqlite3.connect("database.db")
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_entry(site, username, password):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (site, username, password) VALUES (?, ?, ?)",
                   (site, username, password))
    conn.commit()
    conn.close()

def get_entries():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, site, username, password FROM passwords")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "site": r[1], "username": r[2], "password": r[3]} for r in rows]
