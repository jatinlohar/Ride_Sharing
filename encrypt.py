import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def hash_user_input_key(user_input_key):
    # Use SHA-256 to hash the user input key
    hashed_key = hashlib.sha256(user_input_key.encode('utf-8')).digest()
    return hashed_key

def aes_encrypt(message, key):
    # Generate a random 128-bit (16-byte) IV (Initialization Vector)
    iv = os.urandom(16)

    # Create an AES cipher object with CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())

    # Encrypt the message
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message.encode('utf-8')) + encryptor.finalize()

    # Return the IV and ciphertext
    return iv + ciphertext

def aes_decrypt(encrypted_data, key):
    # Extract the IV from the encrypted data
    iv = encrypted_data[:16]

    # Create an AES cipher object with CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())

    # Decrypt the message
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(encrypted_data[16:]) + decryptor.finalize()

    # Return the decrypted message
    return decrypted_message.decode('utf-8')

# Example usage
import os

# Get user input for the key
user_input_key = "1234567890"
hashed_key = hash_user_input_key(user_input_key)

file1 = open("drivers.txt","r+")
driver_data = file1.read().split('\n')
file1.close()

for i in driver_data:
    encrypted_data = aes_encrypt(i, hashed_key)
    print(encrypted_data)

    # # Decryption
    # print(i)
    decrypted_message = aes_decrypt(i, hashed_key)
    print(decrypted_message)
