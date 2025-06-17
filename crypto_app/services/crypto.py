import os
from cryptography.fernet import Fernet

# transforma string em bytes usando utf-8
key = os.environ["FERNET_SECRET_KEY"].encode()
f = Fernet(key)

# def encrypt(inf, **kwargs):
#     token = f.encrypt(inf)
#     return token

# def decrypt(token, **kwargs):
#     return f.decrypt(token)

class CryptoService:
    def __init__(self, key: str = None):
        key = key or os.environ["FERNET_SECRET_KEY"]
        # posso ter múltiplos objetos CryptoService, por isso indicar o obj dessa instância
        # permite que o obj 'fernet' exista fora do construtor
        self.fernet = Fernet(key.encode())
        
    def encrypt(self, data: bytes) -> bytes:
        return self.fernet.encrypt(data)
    
    def decrypt(self, token: bytes) -> bytes:
        return self.fernet.decrypt(token)