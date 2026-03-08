from cryptography.fernet import Fernet

KEY_FILE = "secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

def load_key():
    return open(KEY_FILE, "rb").read()

def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    enc_file = file_path + ".enc"

    with open(enc_file, "wb") as f:
        f.write(encrypted)

    return enc_file


def decrypt_file(enc_file, output_file):
    key = load_key()
    fernet = Fernet(key)

    with open(enc_file, "rb") as f:
        encrypted_data = f.read()

    decrypted = fernet.decrypt(encrypted_data)

    with open(output_file, "wb") as f:
        f.write(decrypted)