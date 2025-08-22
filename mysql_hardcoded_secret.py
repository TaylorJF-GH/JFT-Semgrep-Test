# mysql_hardcoded_secret_bad.py
# WARNING: Intentionally insecure Python example.
# Demonstrates hardcoded MySQL credentials (for testing analyzers only).

import mysql.connector

def get_connection():
    # BAD: credentials hardcoded in source code
    conn = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="SuperSecret123!",  # CWE-798: Hardcoded Secret
        database="employees"
    )
    return conn

def main():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT NOW()")
    print("Current time from DB:", cursor.fetchone())
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
