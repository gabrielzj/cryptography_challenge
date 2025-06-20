import os
from cryptography.fernet import Fernet

class CryptoService:
    def __init__(self, key: str = None):
        key = key or os.environ["FERNET_SECRET_KEY"]
        # posso ter múltiplos objetos CryptoService, por isso indicar o obj dessa instância
        # permite que o obj 'fernet' exista fora do construtor
        if not key:
            raise ValueError("FERNET_SECRET_KEY is missing or empty.")
        self.fernet = Fernet(key)
        
    # data é do tipo bytes, é esperado que a função retorno algo do tipo bytes
    def cryptography(self, data: bytes) -> bytes:
        if not isinstance(data, bytes):
            raise TypeError(f"Expected string for decryption input, got {type(data)}")
        # self.fernet.encrypt(data) -> entrada: bytes → saída: bytes (codificados em base64 seguro)
        # decode('utf-8') -> transforma os bytes (base64) em string UTF-8
        return self.fernet.encrypt(data).decode('utf-8')
    
    def decryptography(self, token: bytes) -> bytes:
        if not isinstance(token, str):
            raise TypeError(f"Expected string for decryption input, got {type(token)}")
        # token.encode('utf-8') -> pega string e transforma pra bytes
        # self.fernet.decrypt() -> retorna dados em bytes
        return self.fernet.decrypt(token.encode('utf-8'))