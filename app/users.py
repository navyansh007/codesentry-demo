import sqlite3


def get_user(conn: sqlite3.Connection, user_id: int):
    """Fetch a single user row by id."""
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
    return cur.fetchone()
