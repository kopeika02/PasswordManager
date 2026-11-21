import json
import secrets
import base64
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
DB_FILE = "vault.bin"

def derive_key(master_password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=600_000,
    )
    key = kdf.derive(master_password.encode("utf-8"))
    return base64.urlsafe_b64encode(key)

def load_data(master_password):
    try:
        with open(DB_FILE, 'rb') as f:
            salt = f.read(16)
            encrypted = f.read()
    except FileNotFoundError:
        return {}

    key = derive_key(master_password, salt)
    try:
        raw = Fernet(key).decrypt(encrypted)
        return json.loads(raw.decode("utf-8"))
    except InvalidToken:
        raise ValueError("Неверный мастер-пароль")

def save_data(data, master_password):

    raw = json.dumps(data, ensure_ascii=False).encode("utf-8")
    salt = secrets.token_bytes(16)
    key = derive_key(master_password, salt)
    encrypted = Fernet(key).encrypt(raw)

    with open(DB_FILE, 'wb') as f:
        f.write(salt+encrypted)

def add_password(service, login, password, master_password):
    cdata = load_data(master_password)
    cdata[service] = {"login": login, "password": password}
    save_data(cdata, master_password)

def get_password(service, master_password):

    cdata = load_data(master_password)
    service_data = cdata.get(service)
    if service_data is None:
        return None
    return cdata.get(service)

def list_services(master_password):

    cdata = load_data(master_password)
    return list(cdata)

if __name__ == "__main__":
    add_password("github", "vasya", "abc123", "test123")
    print(get_password("github", "test123"))  # abc123
    print(list_services("test123"))  # ['github']
