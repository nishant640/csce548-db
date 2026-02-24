import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Nishant3035",
    "database": "vuln_tracker"
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)