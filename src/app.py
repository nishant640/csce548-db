import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="vuln_tracker"
)

cursor = db.cursor()

def show_scans():
    cursor.execute("""
        SELECT systems.hostname, vulnerabilities.title, scans.status
        FROM scans
        JOIN systems ON scans.system_id = systems.system_id
        JOIN vulnerabilities ON scans.vuln_id = vulnerabilities.vuln_id
    """)

    for row in cursor.fetchall():
        print(row)

def add_user(name, email):
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (name, email)
    )
    db.commit()
    print("User added.")

while True:
    print("\n1. View scans")
    print("2. Add user")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_scans()
    elif choice == "2":
        name = input("Name: ")
        email = input("Email: ")
        add_user(name, email)
    elif choice == "3":
        break
