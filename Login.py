import sqlite3, hashlib

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    hashed = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password_hash = ?",
        (username, hashed))
    return cursor.fetchone() is not None

user = input("Username: ")
pwd = input("Password: ")
print("Login successful" if login(user, pwd) else "Login failed")
