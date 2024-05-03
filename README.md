# Local Password Manager

The password manager uses OTP with Google auth for login, and securely encrypts stored info with the Crypto.Cipher package and decrypts the info to display to user when requested.

As of right now, the code works as a secure local password manager. If you are wanting to use the code in its current state, follow the set up instructions below.

Currently a WIP, final product will be a standalone application available on Windows, MacOS, and Linux.

## SET UP INSTRUCTIONS (May 2nd, 2024)

### Required softwware
- [Google Authenticator](https://chromewebstore.google.com/detail/authenticator/bhghoamapcdpbohphigoooaddinpkbai?pli=1) (App or exstension, both work).
- [Node.js](https://nodejs.org/en/download) with npm installed (for QR code generation).

### OTP Setup
- Download or install the Google Authenticator app or exstension.
- On line 7 of [otptesting.py](/otptesting.py) change the "name" and "issuer_name" of the provisioning_uri to whatever you want. "name" is the email displayed in Google auth and "issuer_name" is the name of the application using the OTP code.
- Run otptesting.py and copy the "testingkey" and "provisioning_uri" to a text editor.
- IMPORTANT: put quotation marks around the ampersand symbol in the provisioning_uri ("&") or the QR code will not generate properly.
- Install node.js and npm if you haven't already.
- Open up the terminal, navigate to your project directory, and run the following command:
```
qrcode -o out.png "provisioning_uri that you copied"
```
- This will generate a QR code in out.png which you can find in the project directory.
- Scan the QR code with the Google auth app on your mobile device or with the Google auth chrome exstension.
- If done properly, you should see a new OTP set up with the issuer_name and name you chose.

### Excryption Key Setup
- Navigate to the [ciphertesting.py](/ciphertesting.py) file in the project directory.
- Run the file and copy the aes_key to a text editor.

### Final Steps
- In [main.py](/main.py) there will be two empty global variables: 'AES_KEY' & 'SECRET_KEY' (found on lines 9 & 10). 
- Change the value of AES_KEY to the aes_key you copied when you ran ciphertesting.py.
- Change the value of SECRET_KEY to the testingkey you copied when you ran otptesting.py.
- You can now run the program and use it as a password manager!
- When you run it, you will get a window asking for a 6-digit auth code, this is the code found in your Google auth app, after entering this code hit "submit" and this will 'log in' to the password manager.



### To Do:

- OTP setup guide on application

packaging (test on all OS)
- py2exe
- py2dmg
- py2deb

