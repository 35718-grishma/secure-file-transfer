import unittest
import os
from encryption import encrypt_file, decrypt_file, generate_key

class TestEncryption(unittest.TestCase):

    def setUp(self):
        generate_key()

        with open("test.txt", "w") as f:
            f.write("hello secure file transfer")

    def test_encryption_decryption(self):

        encrypted = encrypt_file("test.txt")

        decrypt_file(encrypted, "decrypted.txt")

        with open("decrypted.txt", "r") as f:
            content = f.read()

        self.assertEqual(content, "hello secure file transfer")

    def tearDown(self):
        os.remove("test.txt")
        os.remove("test.txt.enc")
        os.remove("decrypted.txt")

if __name__ == "__main__":
    unittest.main()