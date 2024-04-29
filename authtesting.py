import pyotp


secret_key = "DZZ46UNLJNFMCUAZM6PBIDBNQBVU6LLG"

totp = pyotp.TOTP(secret_key)

print("Current OTP:", totp.now())
