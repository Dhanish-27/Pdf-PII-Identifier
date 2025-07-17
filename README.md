# 📄 PDF PII Identifier & Encryption System

This project provides a secure solution to identify and protect sensitive information (PII) in PDF documents. It is designed to help users detect personal data like mobile numbers, bank account numbers, and PAN card numbers, and ensure they are stored securely using encryption.

## 🔍 Feature 1: PII Detection & Encryption

- Upload any PDF document.
- The system automatically scans and identifies common PII patterns using regex.
- Extracted PII is encrypted using symmetric key encryption.
- The encrypted PII is stored in a separate file.
- A unique encryption key is generated and provided to the user for future decryption.

## 🔓 Feature 2: PII Decryption with Key

- Users can upload the previously encrypted file along with the encryption key.
- If the key is valid, the original PII is decrypted and shown securely.
- If an incorrect key is provided, the system prevents access by displaying incorrect or unreadable data.

## 🛡️ Purpose

- Ensure privacy by separating and securing sensitive data.
- Protect against unauthorized access even if files are exposed.
- Provide a simple mechanism to identify and handle PII in documents.

## ⚠️ Notes

- Currently supports detection of:
  - Indian Mobile Numbers
  - Bank Account Numbers
  - PAN Card Numbers
- Can be extended to support more PII formats (Aadhar, Email, etc.)

## 📌 Project Goal

To provide an easy-to-use tool for privacy-aware document processing that highlights, encrypts, and restricts access to sensitive data using strong encryption techniques.

---

🔗 **Repository:** [github.com/Dhanish-27/Pdf-PII-Identifier](https://github.com/Dhanish-27/Pdf-PII-Identifier)
