import re
from cryptography.fernet import Fernet
import json

# Define regex patterns for different information types
patterns = {
    "aadhaar": r"\b\d{4} \d{4} \d{4}\b",  # Aadhaar format: 1234 5678 9101
    "pan": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",  # PAN format: ABCDE1234F
    "bank_account": r"\b\d{9,18}\b",  # Bank account numbers (9 to 18 digits)
    "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",  # Email addresses
    "mobile": r"\b(?:\+91|91|0)?[6-9][0-9]{9}\b",  # Indian mobile numbers
    "voter_id": r"\b[A-Z]{3}[0-9]{7}\b",  # Voter ID format: ABC1234567
    "driving_license": r"\b[A-Z]{2}[0-9]{2} [0-9]{11}\b",  # Driving License format: MH12 12345678901
}
pattern={
    "aadhaar_enrolmnent":r"\d{4}/\d+/\d+",
    "aadhaar_virtual":r"\d{4} \d{4} \d{4}",
    "mobile":r"\+91.\d{10}|\d{10}|\d{5} \d{5}",
    "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "voter_id": r"\b[A-Z]{3}[0-9]{7}\b",
    "pan": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
    "TN":r"TN-\d+",
    "bank_account": r"\b\d{9,18}\b",
}

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to find and encrypt data
def extract_and_encrypt(content, patterns):
    extracted_data = {}
    for key, pattern in patterns.items():
        matches = re.findall(pattern, content)
        if matches:
            extracted_data[key] = [cipher_suite.encrypt(match.encode()).decode() for match in matches]
    return extracted_data

# Read the input document
input_file = "extracted.txt"  
with open(input_file, "r") as file:
    content = file.read()

# Extract and encrypt data
encrypted_data = extract_and_encrypt(content, pattern)

# Save encrypted data and key to files
with open("encrypted_data.json", "w") as file:
    json.dump(encrypted_data, file, indent=4)

with open("encryption_key.key", "wb") as file:
    file.write(key)
