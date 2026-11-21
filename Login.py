import sqlite3

DB_PASSWORD = "admin123"

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)
    return cursor.fetchone() is not None

user = input("Username: ")
pwd = input("Password: ")
print("Login successful" if login(user, pwd) else "Login failed")
