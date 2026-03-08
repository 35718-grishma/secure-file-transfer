import socket
import tkinter as tk
from tkinter import filedialog, messagebox
from encryption import encrypt_file
import os

HOST = "127.0.0.1"
PORT = 5000

file_path = ""

def browse_file():
    global file_path
    file_path = filedialog.askopenfilename()
    label_file.config(text=file_path)

def send_file():
    if file_path == "":
        messagebox.showerror("Error", "Please select a file")
        return

    encrypted_file = encrypt_file(file_path)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))

        with open(encrypted_file, "rb") as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                client.send(data)

        messagebox.showinfo("Success", "File sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

    finally:
        client.close()

root = tk.Tk()
root.title("Secure File Transfer")
root.geometry("400x200")

title = tk.Label(root, text="Secure File Transfer System", font=("Arial", 14))
title.pack(pady=10)

label_file = tk.Label(root, text="No file selected")
label_file.pack()

browse_btn = tk.Button(root, text="Browse File", command=browse_file)
browse_btn.pack(pady=5)

send_btn = tk.Button(root, text="Send File", command=send_file)
send_btn.pack(pady=5)

root.mainloop()