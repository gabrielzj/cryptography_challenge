import os
from cryptography.fernet import Fernet

# transforma string em bytes usando utf-8
key = os.environ["FERNET_SECRET_KEY"].encode()
f = Fernet(key)

def encrypt(inf, **kwargs):
    token = f.encrypt(inf)
    return token

def decrypt(token, **kwargs):
    return f.decrypt(token)