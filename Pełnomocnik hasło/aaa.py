import hashlib
import os

salt = b'' # Get the salt you stored for *this* user
key = b'MF)\xe70\xdb\x84\xc1p\x80!\xee\x84\xa5\x7fH@\xc1`\xc3\x1937\x8f+\x15\xee\xfa\x068\xa7c' # Get this users key calculated

password_to_check = '0xdeadbeef' # The password provided by the user to check

# Use the exact same setup you used to generate the key, but this time put in the password to check
new_key = hashlib.pbkdf2_hmac(
    'sha256',
    password_to_check.encode('utf-8'), # Convert the password to bytes
    salt,
    100000
)

print(new_key)
if new_key == key:
    print('Password is correct')
else:
    print('Password is incorrect')
