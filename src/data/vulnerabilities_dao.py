from .db import get_connection

def create_vulnerability(title, severity, description):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO vulnerabilities (title, severity, description) VALUES (%s,%s,%s)",
        (title, severity, description)
    )
    conn.commit()
    new_id = cur.lastrowid
    cur.close()
    conn.close()
    return new_id

def get_vulnerability(vuln_id):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM vulnerabilities WHERE vuln_id=%s", (vuln_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def get_all_vulnerabilities():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM vulnerabilities")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def update_vulnerability(vuln_id, title, severity, description):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE vulnerabilities SET title=%s, severity=%s, description=%s WHERE vuln_id=%s",
        (title, severity, description, vuln_id)
    )
    conn.commit()
    ok = cur.rowcount > 0
    cur.close()
    conn.close()
    return ok

def delete_vulnerability(vuln_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM vulnerabilities WHERE vuln_id=%s", (vuln_id,))
    conn.commit()
    ok = cur.rowcount > 0
    cur.close()
    conn.close()
    return ok