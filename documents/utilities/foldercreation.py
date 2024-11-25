import os

BASE_DIR = "../../media/uploads/"

def create_user_folder(user_identifier):
    user_folder = os.path.join(BASE_DIR, f"{user_identifier}")
    os.makedirs(user_folder, exist_ok=True)
    
    return user_folder

# Ensure the base directory exists
os.makedirs(BASE_DIR, exist_ok=True)



