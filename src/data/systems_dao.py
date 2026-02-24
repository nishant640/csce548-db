from .db import get_connection

def create_system(hostname, ip_address, owner_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO systems (hostname, ip_address, owner_id) VALUES (%s,%s,%s)",
        (hostname, ip_address, owner_id)
    )
    conn.commit()
    new_id = cur.lastrowid
    cur.close()
    conn.close()
    return new_id

def get_system(system_id):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM systems WHERE system_id=%s", (system_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def get_all_systems():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM systems")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def update_system(system_id, hostname, ip_address, owner_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE systems SET hostname=%s, ip_address=%s, owner_id=%s WHERE system_id=%s",
        (hostname, ip_address, owner_id, system_id)
    )
    conn.commit()
    ok = cur.rowcount > 0
    cur.close()
    conn.close()
    return ok

def delete_system(system_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM systems WHERE system_id=%s", (system_id,))
    conn.commit()
    ok = cur.rowcount > 0
    cur.close()
    conn.close()
    return ok