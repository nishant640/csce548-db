from .db import get_connection

def create_scan(system_id, vuln_id, scan_date, status):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO scans (system_id, vuln_id, scan_date, status) VALUES (%s,%s,%s,%s)",
        (system_id, vuln_id, scan_date, status)
    )
    conn.commit()
    new_id = cur.lastrowid
    cur.close()
    conn.close()
    return new_id

def get_scan(scan_id):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM scans WHERE scan_id=%s", (scan_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def get_all_scans():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM scans")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def update_scan(scan_id, system_id, vuln_id, scan_date, status):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE scans SET system_id=%s, vuln_id=%s, scan_date=%s, status=%s WHERE scan_id=%s",
        (system_id, vuln_id, scan_date, status, scan_id)
    )
    conn.commit()
    ok = cur.rowcount > 0
    cur.close()
    conn.close()
    return ok

def delete_scan(scan_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM scans WHERE scan_id=%s", (scan_id,))
    conn.commit()
    ok = cur.rowcount > 0
    cur.close()
    conn.close()
    return ok