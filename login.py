import pyotp
import sqlite3

DB_PATH = "user_database.sqlite"


def get_totp_key(email):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT key FROM users WHERE email = ?", (email,))
        key = cursor.fetchone()
        if key:
            return key[0]
        else:
            return None


def main():
    email = input("Enter your email address: ")
    key = get_totp_key(email)

    if key:
        totp = pyotp.TOTP(key)
        authenticator_code = input("Enter your authenticator code: ")

        if totp.verify(authenticator_code):
            print("Authentication successful. Code is valid.")
        else:
            print("Authentication failed. Code is not valid.")
    else:
        print("User not found in the database. Please register first.")


if __name__ == "__main__":
    main()
