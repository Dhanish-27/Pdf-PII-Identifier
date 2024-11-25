import PyPDF2

def extract_text_from_pdf(pdf_path,username):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        
        with open(f"../../media/iploads{username}/extracted.txt", 'w', encoding='utf-8') as text_file:
            text_file.write(text)
        print(f"Text extracted and saved to extracted.txt")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    pdf_file_path = "unlocked.pdf"
    extract_text_from_pdf(pdf_file_path)