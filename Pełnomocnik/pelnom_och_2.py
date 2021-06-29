# from PBKDF2 import PBKDF2
# from Crypto.Cipher import AES
# import os
#
#
# salt = os.urandom(8)    # 64-bit salt
# key = PBKDF2("This passphrase is a secret.", salt).read(32) # 256-bit key
# iv = os.urandom(16)     # 128-bit IV
# cipher = AES.new(key, AES.MODE_CBC, iv)
import hashlib
import os


class SensitiveInfo:
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        nb = len(self.users)
        print(f"There are {nb} users: {' '.join(self.users)}")

    def add(self, user):
        self.users.append(user)
        print(f'Added user {user}')


def hashowanie(sec):
    salt = b''  # Get the salt you stored for *this* user
    # key = b'MF)\xe70\xdb\x84\xc1p\x80!\xee\x84\xa5\x7fH@\xc1`\xc3\x1937\x8f+\x15\xee\xfa\x068\xa7c' # Get this users key calculated

    password_to_check = sec  # The password provided by the user to check

    # Use the exact same setup you used to generate the key, but this time put in the password to check
    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        password_to_check.encode('utf-8'),  # Convert the password to bytes
        salt,
        100000
    )
    #print(new_key)
    return new_key

    # if new_key == key:
    #     print('Password is correct')
    # else:
    #     print('Password is incorrect')


class Info:
    """protection proxy to SensitiveInfo"""

    def __init__(self):
        self.protected = SensitiveInfo()
        #self.secret = '0xdeadbeef'

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input('what is the secret? ')
        f = open('../Pełnomocnik hasło/haslo.txt', 'r+')
        tekst = f.read()
        #print(f'{tekst} z pliku: ')
        hasha = str(hashowanie(sec))
        #print(f'typ hashowanego z pliku: {type(tekst)} typ hashowanego hasła: {type(hasha)}')
        #print(f'{hasha} hash podanego hasła: ')
        self.protected.add(user) if hasha == tekst else print("That's wrong!")
            # if sec == tekst else print("That's wrong!")
            #if sec == self.secret else print("That's wrong!")



# salt = b'' # Get the salt you stored for *this* user
# #key = b'MF)\xe70\xdb\x84\xc1p\x80!\xee\x84\xa5\x7fH@\xc1`\xc3\x1937\x8f+\x15\xee\xfa\x068\xa7c' # Get this users key calculated
#
# password_to_check = '0xdeadbeef' # The password provided by the user to check
#
# # Use the exact same setup you used to generate the key, but this time put in the password to check
# new_key = hashlib.pbkdf2_hmac(
#     'sha256',
#     password_to_check.encode('utf-8'), # Convert the password to bytes
#     salt,
#     100000
# )
#
# print(new_key)
# # if new_key == key:
# #     print('Password is correct')
# # else:
# #     print('Password is incorrect')


def main():
    info = Info()

    while True:
        print('1. read list |==| 2. add user |==| 3. quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            exit()
        else:
            print(f'unknown option: {key}')


if __name__ == '__main__':
    # # a = Keys('0xdeadbeef')
    # # b = Keys('0xdeadbeef')
    # c = '0xdeadbeef'
    # d = '0xdeadbeef'
    # # hasa = hash(a)
    # # hasb = hash(b)
    # hasc = hash(c)
    # hasd = hash(d)
    # # porownanie = hash(a) == hash(b)
    # porownanie2 = hash(c) == hash(d)
    # # print(f'porownanie: {porownanie}')
    # print(f'porownanie2: {porownanie2}')
    # # print(f'Nasze hashe a: {hasa} b: {hasb}')
    # print(hash(('0xdeadbeef', 2)))
    # print(hash(('0xdeadbeef', 2)))
    main()

