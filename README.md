# Password Manager

This is an easy to set up and user-friendly password manager built on Python that uses TOTP for login, securely encrypts stored info with the Crypto.Cipher package, and decrypts the info to display to user when requested.

As of right now, the code is set up for use in a docker container, follow the set up instructions below.

If you are curious about how this project was made, I livestreamed around 95% of it, check it out on my [Twitch](https://www.twitch.tv/codingwithholmes)!

## SET UP INSTRUCTIONS (Dec 4th, 2024)

### Required softwware
- [Google Authenticator](https://chromewebstore.google.com/detail/authenticator/bhghoamapcdpbohphigoooaddinpkbai?pli=1) (App or exstension, both work).

### Package Installation Help
This program uses several Python packages to run, while most are straight forward installs you can find in requirements.txt, there are sometimes issues with the pypng module. If installing that package is not working, run the following command. 

```
python -m pip install git+https://gitlab.com/drj11/pypng@pypng-0.20220715.0
```

### First Time Setup
This program has 2 python files, FirstTimeSetup.py and main.py, FirstTimeSetup.py creates and stores your encryption and Google OTP keys. It also generates a QR code to scan to set up your login with Google OTP.
- After pulling or downloading the repo, and installing the packages in requirements.txt, run FirstTimeSetup.py.
- You will see a TKinter GUI appear with a QR code, scan that QR code with the Google Authenticator app, once you have done that, hit the "finished" button to close the program
- TIP: You can change the name that displays in the Google auth app by editing the 'name' and 'issuer_name' kwargs in line 36 of FirstTimeSetup.py (you will need to re-run FirstTimeSetup.py if you have already ran it to update the values) 
- Once the program has closed, you'll notice a keys.json file has been created in the C:/LPMData directory of the project. Do not edit the values in keys.json or it will prevent you from logging in properly or encrypting the data


### Main 
- After running the FirstTimeSetup.py file, you can run main.py. You will only need to use main.py from here on out. 
- When you first run the program you will notice a TKinter GUI asking you for a 6-digit auth code
- You can find this code in the Google authenticator app, enter the 6 digits and hit the 'login' button
- You will then be in the main fuction of the app, input a website name, email, and password (you can also generate a password) 
- Hit the 'add' button to add the website info, this will encrypt and store the info in the C:/LPMData directory with a file name as '(website_name).bin'
- To search up a website you have stored, type out the website name and select the search button

