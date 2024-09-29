from flask import Blueprint, request, jsonify, send_file
from models import upload_file, list_files, get_file
import os

file_bp = Blueprint('file_ops', __name__)

ALLOWED_EXTENSIONS = {'pptx', 'docx', 'xlsx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

UPLOAD_FOLDER = "F:\\VScode\\Python\\Py2\\Assessment\\uploads"  # <-- Set the upload path here

@file_bp.route('/upload', methods=['POST'])
def upload():
    # check file presence
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    
    #check extensions
    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type. Only pptx, docx, and xlsx allowed."}), 400
    
    try:
        
        response = upload_file(file, file.filename, UPLOAD_FOLDER)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": f"Failed to upload file: {str(e)}"}), 500

@file_bp.route('/download/<encrypted_url>', methods=['GET'])
def download(encrypted_url):
    try:
       
        filepath = get_file(encrypted_url, UPLOAD_FOLDER)
        if filepath and os.path.exists(filepath):
            return send_file(filepath)
        return jsonify({"error": "File not found or unauthorized access"}), 404
    except Exception as e:
        return jsonify({"error": f"Failed to download file: {str(e)}"}), 500
