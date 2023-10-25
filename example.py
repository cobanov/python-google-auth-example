from generate_user import TOTPGenerator, initialize_database


email = "mertcobanov@gmail.com"

initialize_database()

totp_generator = TOTPGenerator(email, issuer_name="Cobanov")
totp_generator.generate_qr_code(qr_code_filename)
