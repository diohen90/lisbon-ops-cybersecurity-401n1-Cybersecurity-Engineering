#!/usr/bin/python3
# Script : Challenge06.py
# Purpose: Asks the user to select an option for encryption or decryption
# Why    : Automating encryption and decryption of files using Python

from cryptography.fernet import Fernet
import os

def generate_key():
    """
    Generates a random encryption key using the Fernet module.
    """
    return Fernet.generate_key()

def load_key(key_path):
    """
    Loads a saved key from a given file path.
    """
    return open(key_path, "rb").read()

def save_key(key_path, key):
    """
    Saves an encryption key to a given file path.
    """
    with open(key_path, "wb") as f:
        f.write(key)

def encrypt_file(file_path, key):
    """
    Encrypts a target file and replaces it with the encrypted version.
    """
    with open(file_path, "rb") as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(file_path, "wb") as f:
        f.write(encrypted)

def decrypt_file(file_path, key):
    """
    Decrypts a target file and replaces it with the decrypted version.
    """
    with open(file_path, "rb") as f:
        encrypted_data = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as f:
        f.write(decrypted)

def encrypt_message(message, key):
    """
    Encrypts a cleartext string and returns the ciphertext.
    """
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    print("Encrypted message:", encrypted.decode())

def decrypt_message(ciphertext, key):
    """
    Decrypts a ciphertext string and returns the cleartext.
    """
    fernet = Fernet(key)
    decrypted = fernet.decrypt(ciphertext.encode())
    print("Decrypted message:", decrypted.decode())

# Prompt user to select a mode
mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n"))

# Load or generate encryption key
key_path = "key.key"
if os.path.exists(key_path):
    key = load_key(key_path)
else:
    key = generate_key()
    save_key(key_path, key)

if mode == 1:
    # Prompt user for target file path
    file_path = input("Enter the file path to encrypt: ")
    encrypt_file(file_path, key)
elif mode == 2:
    # Prompt user for target file path
    file_path = input("Enter the file path to decrypt: ")
    decrypt_file(file_path, key)
elif mode == 3:
    # Prompt user for message to encrypt
    message = input("Enter the message to encrypt: ")
    encrypt_message(message, key)
elif mode == 4:
    # Prompt user for ciphertext to decrypt
    ciphertext = input("Enter the ciphertext to decrypt: ")
    decrypt_message(ciphertext, key)
else:
    print("Invalid mode selected.")
