from data.users_dao import create_user, get_user, get_all_users, update_user, delete_user
from data.systems_dao import create_system, get_system, get_all_systems, update_system, delete_system
from data.vulnerabilities_dao import create_vulnerability, get_vulnerability, get_all_vulnerabilities, update_vulnerability, delete_vulnerability
from data.scans_dao import create_scan, get_scan, get_all_scans, update_scan, delete_scan

def line(title):
    print("\n" + "=" * 10 + f" {title} " + "=" * 10)

def main():
    # USERS
    line("USERS: READ ALL (existing)")
    print(get_all_users()[:3])  # show 3 rows only

    line("USERS: CREATE -> GET -> UPDATE -> DELETE")
    uid = create_user("Test User", "testuser999@test.com")
    print("created user_id:", uid)
    print("get:", get_user(uid))

    ok = update_user(uid, "Test User Updated", "testuser999@test.com")
    print("update ok:", ok)
    print("get after update:", get_user(uid))

    ok = delete_user(uid)
    print("delete ok:", ok)
    print("get after delete (should be None):", get_user(uid))

    # SYSTEMS
    line("SYSTEMS: READ ALL (existing)")
    print(get_all_systems()[:3])

    line("SYSTEMS: CREATE -> GET -> UPDATE -> DELETE")
    sid = create_system("test-host", "10.9.9.9", 1)
    print("created system_id:", sid)
    print("get:", get_system(sid))

    ok = update_system(sid, "test-host-updated", "10.9.9.9", 1)
    print("update ok:", ok)
    print("get after update:", get_system(sid))

    ok = delete_system(sid)
    print("delete ok:", ok)
    print("get after delete (should be None):", get_system(sid))

    # VULNERABILITIES
    line("VULNERABILITIES: READ ALL (existing)")
    print(get_all_vulnerabilities()[:3])

    line("VULNERABILITIES: CREATE -> GET -> UPDATE -> DELETE")
    vid = create_vulnerability("Test Vuln", "LOW", "temporary vuln for test")
    print("created vuln_id:", vid)
    print("get:", get_vulnerability(vid))

    ok = update_vulnerability(vid, "Test Vuln Updated", "MEDIUM", "updated")
    print("update ok:", ok)
    print("get after update:", get_vulnerability(vid))

    ok = delete_vulnerability(vid)
    print("delete ok:", ok)
    print("get after delete (should be None):", get_vulnerability(vid))

    # SCANS
    line("SCANS: READ ALL (existing)")
    print(get_all_scans()[:3])

    line("SCANS: CREATE -> GET -> UPDATE -> DELETE")
    scan_id = create_scan(1, 1, "2025-02-01", "OPEN")
    print("created scan_id:", scan_id)
    print("get:", get_scan(scan_id))

    ok = update_scan(scan_id, 1, 1, "2025-02-01", "RESOLVED")
    print("update ok:", ok)
    print("get after update:", get_scan(scan_id))

    ok = delete_scan(scan_id)
    print("delete ok:", ok)
    print("get after delete (should be None):", get_scan(scan_id))

if __name__ == "__main__":
    main()