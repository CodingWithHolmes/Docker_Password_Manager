from tkinter import ttk
from tkinter import *
import pyotp
from Crypto.Random import get_random_bytes
import json
import pyqrcode

# ---------------------------- FIRST TIME SETUP ------------------------------- #
"""
This is the first time setup for the app. It generates the keys needed for the app and stores them in a json file.
I originally was trying to do this all in one file, using some creative but jank workarounds to get it to work. 
I ultimately didn't like it and it would run into errors that could be resolved by having a separate setup file.
This is a significantly cleaner/less error prone solution and I'm happy with it.
You will only need to run this once, then can just run the main.py file.
"""


def first_time_setup():
    # Generate the keys needed for the app
    keys = {}
    key_list = []
    otpkey = pyotp.random_base32()
    aes_key = get_random_bytes(16)
    aes_key_str = aes_key.decode("utf-16")

    # Store the keys in a json file
    key_list.append(aes_key_str)
    key_list.append(otpkey)

    keys["keys"] = key_list
    with open('Data/keys.json', 'w') as out_file:
        json.dump(keys, out_file, indent=4)

    # QR code generation to use to set up Google OTP
    # change the name and issuer_name to whatever you want to display in google auth app
    provisioning_uri = pyotp.totp.TOTP(otpkey).provisioning_uri(name='V2', issuer_name='LPM')
    qr_code = pyqrcode.create(provisioning_uri)
    qr_code.png('qrcode.png', scale=3)

    # ---------------------------- QR CODE TKINTER UI ------------------------------- #
    def qrcode_window():
        setup_window = Tk()
        setup_window.title("1Pass At Home")
        setup_window.config(padx=20, pady=20)

        setup_label = ttk.Label(text="Scan the QR code below with the Google Authenticator app, "
                                     "hit finished when done.")
        setup_label.grid(row=0, column=0)

        img2 = PhotoImage(file="qrcode.png")
        canvas = Canvas(width=250, height=250)
        canvas.create_image(125, 125, image=img2)
        canvas.grid(row=1, column=0)

        setup_button = ttk.Button(text="Finished", command=setup_window.destroy)
        setup_button.grid(row=2, column=0)

        setup_window.mainloop()

    qrcode_window()


first_time_setup()
