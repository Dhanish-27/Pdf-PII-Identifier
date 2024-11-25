from cryptography.fernet import Fernet
import json


def decrypt_data(encrypted_data, cipher_suite):
    decrypted_data = {}
    for key, encrypted_values in encrypted_data.items():
        decrypted_data[key] = [cipher_suite.decrypt(value.encode()).decode() for value in encrypted_values]
    return decrypted_data


key_file = "encryption_key.key"  # Replace with your key file name
with open(key_file, "rb") as file:
    key = file.read()

cipher_suite = Fernet(key)

encrypted_file = "encrypted_data.json"  
with open(encrypted_file, "r") as file:
    encrypted_data = json.load(file)


decrypted_data = decrypt_data(encrypted_data, cipher_suite)

decrypted_file = "decrypted_data.json"
with open(decrypted_file, "w") as file:
    json.dump(decrypted_data, file, indent=4)

print("Decryption completed. Decrypted data saved in 'decrypted_data.json'.")
