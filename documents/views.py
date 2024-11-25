# views.py
import os
from django.shortcuts import render, HttpResponse
from django.conf import settings
from .models import UploadedFile
from .forms import FileUploadForm
from django.contrib.auth.models import User
from .utilities import *
import PyPDF2
import re
from cryptography.fernet import Fernet
import json

def extract_and_encrypt(content, patterns,cipher_suite):
    extracted_data = {}
    for key, pattern in patterns.items():
        matches = re.findall(pattern, content)
        if matches:
            extracted_data[key] = [cipher_suite.encrypt(match.encode()).decode() for match in matches]
    return extracted_data

def decrypt_data(encrypted_data, cipher_suite):
    decrypted_data = {}
    for key, encrypted_values in encrypted_data.items():
        decrypted_data[key] = [cipher_suite.decrypt(value.encode()).decode() for value in encrypted_values]
    return decrypted_data



def checking(request):
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
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        file = request.FILES['file']
        #     str_username=str(request.user)
        #     # Create a folder with the same name as the file in the media directory
        #     upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads', str_username)

        #     file_path = os.path.join(upload_dir, str_username)
        #     if not os.path.exists(upload_dir):
        #         os.makedirs(f"{upload_dir}")
        #     file.name="sample.pdf"
            
            
            
            
            # text extraction from the PDF
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
            # Encryption
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        encrypted_data = extract_and_encrypt(text, pattern,cipher_suite) #file encryption
        upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads', str(request.user))
        if not os.path.exists(upload_dir):
            os.makedirs(f"{upload_dir}")
        with open(upload_dir + "\encrypted_data.json", "w") as file:
            json.dump(encrypted_data, file, indent=4)
        with open(upload_dir+"\encryption_key.key", "wb") as file:
            file.write(key)
        encrypted_data_link = f"<a href='/media/uploads/{str(request.user)}/encrypted_data.json'>Download Encrypted Data</a><br>"
        key_link = f"<a href='/media/uploads/{str(request.user)}/encryption_key.key'>Download Encryption Key</a>"
            
        return HttpResponse(encrypted_data_link + key_link)
    else:
        form = FileUploadForm()
    
    return render(request, "checking.html", {"form": form})

def decrypt(request):
    form = FileUploadForm(request.POST, request.FILES)
    if request.method=="POST":
        upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads', str(request.user)) 
        with open(upload_dir+"\encryption_key.key", "rb") as file:
            key = file.read()

        cipher_suite = Fernet(key) 
        with open(upload_dir+"\encrypted_data.json", "r") as file:
            encrypted_data = json.load(file)


            # else:
            #     decrypt = request.FILES['decryption']
            #     key_decrypt=request.FILES['key']
            #     with open(key_decrypt, "rb") as file:
            #         key = file.read()
            #     with open(decrypt, "r") as file:
            #         encrypted_data = json.load(file)
            
        decrypted_data = decrypt_data(encrypted_data, cipher_suite)
            
            
        with open(upload_dir+"\decrypted_data.json", "w") as file:
            json.dump(decrypted_data, file, indent=4)

        decrypted_data_link = f"<a href='/media/uploads/{str(request.user)}/decrypted_data.json'>Download Decrypted Data</a><br>"
        return HttpResponse(decrypted_data_link)
    return render(request,"decryption.html",{'form':form})

def index(request):
    return render(request,"index.html")