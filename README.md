# TOTP Authentication System

This is a simple two-part Python-based TOTP (Time-Based One-Time Password) authentication system consisting of a user registration script and a login script. It allows users to register their email and generate TOTP QR codes for authentication.

## Features

- User registration with email and TOTP generation.
- Secure storage of user information and TOTP keys in a SQLite database.
- User login with TOTP verification.

## Requirements

```bash
pip install pyotp qrcode
```

## Usage

### TOTP Registration Script (totp_registration.py)

1. Run the registration script (totp_registration.py).

2. Enter your email address.

3. The script will generate a TOTP QR code and save it as a PNG image in the qr_codes directory.

### User Login Script (login.py)

1. Run the login script (login.py).

2. Enter your email address.

3. The script will prompt you to enter the authenticator code from your TOTP app.

4. The code will be validated, and you will receive feedback regarding the authentication result.

## Database

User information and TOTP keys are stored in an SQLite database (user_database.sqlite).

## License

This project is licensed under the MIT [License](https://chat.openai.com/c/LICENSE) - see the LICENSE file for details.

## Acknowledgments

- This project uses the PyOTP library for TOTP functionality.
- This project uses the qrcode library for generating QR codes.
