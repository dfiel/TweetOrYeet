import encryption

DEBUG = True


def main():
    if DEBUG:
        system_root = 'TestDir'
    else:
        system_root = '.'
    encrypter = encryption.Encrypter()
    encrypter.load_key('fernet.key')
    encryption.traverse_dirs(system_root, decrypt=encrypter)
    print("Data Decrypted")


if __name__ == '__main__':
    main()