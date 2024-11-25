# forms.py
from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField()
    decryption=forms.FileField()
    key=forms.FileField()