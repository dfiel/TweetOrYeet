from cryptography.fernet import Fernet
import os
import time


class Encrypter:

    def __init__(self):
        self.key = None
        self.crypter = None

    def load_key(self, filename):
        with open(filename, 'r') as file:
            self.crypter = Fernet(file.read())

    def encrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            data = file.read()
        with open(file_path, 'wb') as file:
            file.write(self.crypter.encrypt(data))

    def decrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            data = file.read()
        with open(file_path, 'wb') as file:
            file.write(self.crypter.decrypt(data))
