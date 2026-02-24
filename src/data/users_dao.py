from .db import get_connection

def create_user(name, email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (name,email) VALUES (%s,%s)",
        (name, email)
    )
    conn.commit()
    new_id = cur.lastrowid
    cur.close()
    conn.close()
    return new_id

def get_user(user_id):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM users WHERE user_id=%s", (user_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def get_all_users():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def update_user(user_id, name, email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET name=%s,email=%s WHERE user_id=%s",
        (name, email, user_id)
    )
    conn.commit()
    ok = cur.rowcount > 0
    cur.close()
    conn.close()
    return ok

def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE user_id=%s", (user_id,))
    conn.commit()
    ok = cur.rowcount > 0
    cur.close()
    conn.close()
    return ok