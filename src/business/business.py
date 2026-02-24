# Business Layer
# Purpose: expose ALL CRUD operations from data layer.
# You can add business rules here later (validation, logging, etc).

from src.data.users_dao import (
    create_user, get_user, get_all_users, update_user, delete_user
)
from src.data.systems_dao import (
    create_system, get_system, get_all_systems, update_system, delete_system
)
from src.data.vulnerabilities_dao import (
    create_vulnerability, get_vulnerability, get_all_vulnerabilities,
    update_vulnerability, delete_vulnerability
)
from src.data.scans_dao import (
    create_scan, get_scan, get_all_scans, update_scan, delete_scan
)

# ---------------- USERS ----------------

def add_user(name, email):
    return create_user(name, email)

def fetch_user(user_id):
    return get_user(user_id)

def fetch_all_users():
    return get_all_users()

def edit_user(user_id, name, email):
    return update_user(user_id, name, email)

def remove_user(user_id):
    return delete_user(user_id)

# ---------------- SYSTEMS ----------------

def add_system(hostname, ip_address, owner_id):
    return create_system(hostname, ip_address, owner_id)

def fetch_system(system_id):
    return get_system(system_id)

def fetch_all_systems():
    return get_all_systems()

def edit_system(system_id, hostname, ip_address, owner_id):
    return update_system(system_id, hostname, ip_address, owner_id)

def remove_system(system_id):
    return delete_system(system_id)

# ---------------- VULNERABILITIES ----------------

def add_vulnerability(title, severity, description):
    return create_vulnerability(title, severity, description)

def fetch_vulnerability(vuln_id):
    return get_vulnerability(vuln_id)

def fetch_all_vulnerabilities():
    return get_all_vulnerabilities()

def edit_vulnerability(vuln_id, title, severity, description):
    return update_vulnerability(vuln_id, title, severity, description)

def remove_vulnerability(vuln_id):
    return delete_vulnerability(vuln_id)

# ---------------- SCANS ----------------

def add_scan(system_id, vuln_id, scan_date, status):
    return create_scan(system_id, vuln_id, scan_date, status)

def fetch_scan(scan_id):
    return get_scan(scan_id)

def fetch_all_scans():
    return get_all_scans()

def edit_scan(scan_id, system_id, vuln_id, scan_date, status):
    return update_scan(scan_id, system_id, vuln_id, scan_date, status)

def remove_scan(scan_id):
    return delete_scan(scan_id)