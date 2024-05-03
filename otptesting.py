import pyotp

testingkey = pyotp.random_base32()

print(testingkey)

provisioning_uri = pyotp.totp.TOTP(testingkey).provisioning_uri(name='email or whatever you want', issuer_name='name of password manager')

print(provisioning_uri)

