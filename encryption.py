from cryptography.fernet import Fernet
import os


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

    def encrypt_with_name(self, file_path):
        with open(file_path, 'rb') as file:
            data = file.read()
        split_path = os.path.split(file_path)
        name = self.crypter.encrypt(split_path[1].encode()).decode()
        new_path = os.path.join(split_path[0], name)
        with open(new_path, 'wb+') as file:
            file.write(self.crypter.encrypt(data))
        os.remove(file_path)

    def decrypt_with_name(self, file_path):
        with open(file_path, 'rb') as file:
            data = file.read()
        split_path = os.path.split(file_path)
        name = self.crypter.decrypt(split_path[1].encode()).decode()
        new_path = os.path.join(split_path[0], name)
        with open(new_path, 'wb+') as file:
            file.write(self.crypter.decrypt(data))
        os.remove(file_path)

    def decrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            data = file.read()
        with open(file_path, 'wb') as file:
            file.write(self.crypter.decrypt(data))
