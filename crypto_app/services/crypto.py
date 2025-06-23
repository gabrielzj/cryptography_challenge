import os
import ast
from cryptography.fernet import Fernet

class CryptoService:
    def __init__(self, key: str = None):
        key = key or os.environ["FERNET_SECRET_KEY"]
        # posso ter múltiplos objetos CryptoService, por isso indicar o obj dessa instância
        # permite que o obj 'fernet' exista fora do construtor
        if not key:
            raise ValueError("FERNET_SECRET_KEY is missing or empty.")
        self.fernet = Fernet(key)
        
    def cryptography(self, data: bytes) -> bytes:
        # Garantir que data seja bytes
        if isinstance(data, str):
            data = data.encode('utf-8')
        elif not isinstance(data, bytes):
            raise TypeError(f"Expected string or bytes for encryption input, got {type(data)}")
        
        # self.fernet.encrypt(data) -> entrada: bytes → saída: bytes (codificados em base64 seguro)
        # decode('utf-8') -> transforma os bytes em string UTF-8 pra ir pro banco
        return self.fernet.encrypt(data).decode('utf-8')   
    
    def decryptography(self, token):
        try:
            if isinstance(token, str) and token.startswith("b'"):
                token = ast.literal_eval(token).decode('utf-8')
            
            plain_text = self.fernet.decrypt(token)
            
            # token.encode('utf-8') -> pega string e transforma pra bytes
            # self.fernet.decrypt() -> retorna dados em bytes
            return plain_text
        except Exception as e:
            print(f"Erro na descriptografia: {e}", token)
            return f'Erro de descriptografia: {str(e)}'
        # return self.fernet.decrypt(token).decode('utf-8')