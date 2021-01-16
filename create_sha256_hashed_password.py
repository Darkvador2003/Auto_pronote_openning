import hashlib, os
from getpass import getpass

password = getpass("Type your password \n(it's normal if you can't see what you're typing'):  ")
salt = os.urandom(32)
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

print(f"""This your salt: {salt} and this is your key: {key}
You should copy paste them into the lines 5 and 6 of main.py. """

