# Password Manager

This is an easy to set up and user-friendly password manager built on Python that uses TOTP for login, securely encrypts stored info with the Crypto.Cipher package, and decrypts the info to display to user when requested.

As of right now, the code is set up for use in a docker container, follow the set up instructions below.

If you are curious about how this project was made, I livestreamed around 95% of it, check it out on my [Twitch](https://www.twitch.tv/codingwithholmes)!

## SET UP INSTRUCTIONS (Dec 4th, 2024)

### Required softwware
- [Google Authenticator](https://chromewebstore.google.com/detail/authenticator/bhghoamapcdpbohphigoooaddinpkbai?pli=1) (App or exstension, both work).
- [Docker](https://www.docker.com/)


- Download the .zip and extract the Docker_Password_Manager_Master folder in a location of your choice
- Navigate the directory of that folder in a CLI instance
- Run the following commands

```
docker build -t password-manager .
```
This command builds the docker image with the info in the Docker file. 

Then run:
```
Docker volume create password-manager-data
```
This command creates a docker volume to store the password info

Lastly, run:
```
docker run -it --rm -v password-manager-data:/app/data password-manager
```
This command starts a container based off the password-manager image and uses the password-manager-data volume you created earlier to store your info. 

If it's the first time you are running the image, it will guide you througn the TOTP set up, be careful when resizing the terminal for the QR code as it will sometimes mess it up and you won't be able to scan it, if that happens, just control+c and rerun the above command. 

Once you have successfully scanned the QR code, the program will close on it's own, then you will re-run the docker run commmand above to start up the password manager and everything should be good to go!

### Using the Password Manager
After you have gone through the QR code and TOTP set up, you will be prompted to put in your 6-digit code to login. After logging in, you will be promtped to type in a website name. I usually type in things like 'Amazon' or 'bank', it's not super important as the website name is used just as a reference for retriving the info later. 
After typing a website name, the program will check to see if an entry for that website already exists, if not, you will be prompted to put in an email/password. If it does exist, it will show you the current username/password and then ask if you want to change it.
To close the program, type 'exit' as the website name. 
