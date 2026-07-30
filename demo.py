import sqlite3

def authenticate_user(username):
    conn = sqlite3.connect("test.db")
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone()
    finally:
        conn.close()
