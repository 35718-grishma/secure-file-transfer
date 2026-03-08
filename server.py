import socket
from encryption import decrypt_file, generate_key
import os

HOST = "0.0.0.0"
PORT = 5000

# generate key if not exists
if not os.path.exists("secret.key"):
    generate_key()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server listening on port", PORT)

conn, addr = server.accept()
print("Connected by", addr)

file_name = "received_file.enc"

with open(file_name, "wb") as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print("Encrypted file received!")

decrypt_file(file_name, "received_file_decrypted")

print("File decrypted successfully!")

conn.close()
server.close()