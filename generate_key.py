from cryptography.fernet import Fernet
import os


def validated_input():
    while True:
        text = input("Enter Choice: ")
        if text != 'Y' and text != 'N':
            print("Invalid Input")
            print()
            continue
        return text


def generate_fernet_key():
    if os.path.exists('fernet.key'):
        print("Encryption key already exists. Do you want to overwrite?")
        print("Enter Y or N")
        print()
        if validated_input() == 'N':
            print("Exiting...")
            exit()
    with open('fernet.key', 'wb') as file:
        file.write(Fernet.generate_key())
    print("Key Generated")
    print("!--                             IMPORTANT                               --!")
    print()
    print("                 STORE A COPY OF THIS KEY IN A SECURE PLACE                ")
    print("SHOULD THE DEAD MAN SWITCH ENGAGE, YOU WILL REQUIRE THIS KEY FOR DECRYPTION")
    print("THIS KEY CANNOT BE BRUTE FORCED, AND YOUR DATA WILL BE LOST WITHOUT THE KEY")
    print()
    print("!--                             IMPORTANT                               --!")


if __name__ == '__main__':
    generate_fernet_key()