import pyotp
import qrcode
import sqlite3
import uuid
import os

DB_PATH = "user_database.sqlite"


class TOTPGenerator:
    def __init__(self, email, issuer_name="Cobanov"):
        self.email = email
        self.issuer_name = issuer_name
        self.unique_id = str(uuid.uuid4())

    def generate_totp_uri(self):
        totp = pyotp.random_base32()
        self.key = totp

        uri = pyotp.totp.TOTP(totp).provisioning_uri(
            name=self.email, issuer_name=self.issuer_name
        )

        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (unique_id, email, key) VALUES (?, ?, ?)",
                (self.unique_id, self.email, self.key),
            )
            conn.commit()

        return uri

    def generate_qr_code(self, filename):
        uri = self.generate_totp_uri()
        img = qrcode.make(uri)
        img.save(filename)
        print(f"QR code saved as '{filename}'")


def initialize_database():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                unique_id TEXT NOT NULL,
                email TEXT NOT NULL,
                key TEXT NOT NULL
            )
        """
        )
        conn.commit()


if __name__ == "__main__":
    os.makedirs("qr_codes", exist_ok=True)
    email = "mertcobanov@gmail.com"

    initialize_database()

    totp_generator = TOTPGenerator(email, issuer_name="Cobanov")
    qr_code_filename = f"qr_codes/qr_{totp_generator.unique_id}.png"
    totp_generator.generate_qr_code(qr_code_filename)
