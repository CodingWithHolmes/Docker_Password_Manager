import pyotp

testingkey = pyotp.random_base32()

print(testingkey)

provisioning_uri = pyotp.totp.TOTP(testingkey).provisioning_uri(name='codingwithholmes@google.com', issuer_name='1Pass But Worse')

print(provisioning_uri)

