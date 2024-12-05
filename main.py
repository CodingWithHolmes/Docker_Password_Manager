import pyotp
from Crypto.Random import get_random_bytes
import json
import pyqrcode
import time
from Crypto.Cipher import AES
import sys


# ---------------------------- FIRST TIME SETUP SCRIPT ------------------------------- #
def first_time_setup():
    # Generate the keys needed for the app
    otpkey = pyotp.random_base32()
    aes_key = get_random_bytes(16)
    aes_key_str = aes_key.decode("utf-16")

    print("Creating QR code for Google OTP setup")
    print("Please do not resize this window until you have scanned the QR code")
    print("-" * 50)  # Add a separator line
    time.sleep(3)
    
    # QR code generation
    provisioning_uri = pyotp.totp.TOTP(otpkey).provisioning_uri(name='TerminalAdmin', issuer_name='Docker LPM')
    qr_code = pyqrcode.create(provisioning_uri)
    
    # Generate QR code with consistent formatting
    qr_terminal = qr_code.terminal(module_color=5, background=123, quiet_zone=1)
    
    # Add top and bottom borders to help maintain shape
    border = "+" + "-" * (len(qr_terminal.split("\n")[0])) + "+"
    print(border)
    print(qr_terminal)
    print(border)
    print("-" * 50)  # Add a separator line
    print("Please scan the above QR code with the Google authenticator app")
    
    set_up_finished = False
    while not set_up_finished:
        user_response = input("Type 'Y' when you have scanned the QR code: ").upper()
        if user_response == "Y":
            # Only create and save keys.json after confirmation
            keys = {}
            key_list = [aes_key_str, otpkey]
            keys["keys"] = key_list
            
            with open('/app/data/keys.json', 'w') as out_file:
                json.dump(keys, out_file, indent=4)
                
            print("Your OTP and Encryption keys have been created and stored in keys.json, do NOT modify these values")
            print("Setup complete, closing program, re-run the program to start up the password manager")
            time.sleep(4)
            sys.exit(0)
        else:
            print("Please scan the QR code and type 'Y' to continue")


# ---------------------------- MAIN WINDOW ------------------------------- #
def password_manager():
    using_app = True

    # ---------------------------- MAIN ------------------------------- #
    print("Welcome! Put in a website name, type 'Exit' to close the password manager")
    while using_app:
        website_name = input("Website name: ").title()
        if website_name.lower() == 'exit':
            print("Closing password manager")
            sys.exit(0)  # Using sys.exit(0) for clean exit

        try:
            with open(f"/app/data/{website_name}.bin", "rb") as decrypted_file:
                tag = decrypted_file.read(16)
                nonce = decrypted_file.read(15)
                ciphertext = decrypted_file.read()
                cipher = AES.new(AES_KEY, AES.MODE_OCB, nonce=nonce)

                try:
                    message = cipher.decrypt_and_verify(ciphertext, tag)
                except ValueError:
                    print("The message was modified!")
                    sys.exit(1)

                print(f"Existing info for {website_name} has been found, listing below")
                print(message.decode())
                
                # Add update option
                while True:
                    update_choice = input("Would you like to update this entry? (Y/N): ").lower()
                    if update_choice == 'y':
                        email = input(f"Put in your new email/username for {website_name}: ")
                        password = input(f"Put in your new password for {website_name}: ")

                        encrypted_password = f'Email: {email} \nPassword: {password}'.encode()
                        cipher = AES.new(AES_KEY, AES.MODE_OCB)
                        ciphertext, tag = cipher.encrypt_and_digest(encrypted_password)
                        assert len(cipher.nonce) == 15

                        with open(f"/app/data/{website_name}.bin", "wb") as encrypted_file:
                            encrypted_file.write(tag)
                            encrypted_file.write(cipher.nonce)
                            encrypted_file.write(ciphertext)
                        print(f"Entry for {website_name} has been updated")
                        break
                    elif update_choice == 'n':
                        break
                    else:
                        print("Invalid input. Please type 'Y' or 'N'")

        except FileNotFoundError:
            print("No existing data found for this website")
            while True:
                user_choice = input("Would you like to add login info? (Y/N): ").lower()
                if user_choice == 'n':
                    break
                elif user_choice == 'y':
                    email = input(f"Put in your email/username for {website_name}: ")
                    password = input(f"Put in your password for {website_name}: ")

                    encrypted_password = f'Email: {email} \nPassword: {password}'.encode()
                    cipher = AES.new(AES_KEY, AES.MODE_OCB)
                    ciphertext, tag = cipher.encrypt_and_digest(encrypted_password)
                    assert len(cipher.nonce) == 15

                    with open(f"/app/data/{website_name}.bin", "wb") as encrypted_file:
                        encrypted_file.write(tag)
                        encrypted_file.write(cipher.nonce)
                        encrypted_file.write(ciphertext)
                    break
                else:
                    print("Invalid input. Please type 'Y', 'N'")


# ---------------------------- AUTHENTICATE OTP ------------------------------- #
def authenticate_otp_code():
    logged_in = False
    totp = pyotp.TOTP(SECRET_KEY)
    while not logged_in:
        otp_code = input("Input the 6-digit code in the Google Authenticator app: ")
        if otp_code == totp.now():
            print("Authentication correct, starting password manager...")
            time.sleep(1)
            password_manager()
        else:
            print("Error: Code is not correct")


try:
    f = open("/app/data/keys.json")
    print("keys.json found, starting password manager")
    data = json.load(f)
    AES_KEY = bytes(data['keys'][0], 'utf-8')
    print(type(AES_KEY))
    SECRET_KEY = data['keys'][1]
    authenticate_otp_code()
except FileNotFoundError:
    print("No keys.json file found running first time setup script")
    first_time_setup()
