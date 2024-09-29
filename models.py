from config import get_db_connection
from utils import encrypt_url
import os

# File Upload
def upload_file(file, filename, upload_folder):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        encrypted_url = encrypt_url(filename)
        
        # Save the file 
        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)
        
        # Insert record 
        cursor.execute("INSERT INTO files (filename, encrypted_url, owner_id) VALUES (%s, %s, %s)", (filename, encrypted_url, 1))  # Assuming owner_id is 1 for now
        db.commit()
        return {"message": "File uploaded successfully", "encrypted_url": encrypted_url}
    
    except Exception as e:
        return {"error": f"Failed to upload file: {str(e)}"}, 500

# File for Download
def get_file(encrypted_url, upload_folder):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT filename FROM files WHERE encrypted_url = %s", (encrypted_url,))
        file = cursor.fetchone()
        if file:
            return os.path.join(upload_folder, file[0])  # Return file path
        else:
            return None
    except Exception as e:
        return None
