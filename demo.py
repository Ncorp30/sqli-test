import sqlite3

def login(username):
    try:
        with sqlite3.connect("test.db") as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE username=?"
            cursor.execute(query, (username,))
            return cursor.fetchone()
    except sqlite3.Error:
        return None
