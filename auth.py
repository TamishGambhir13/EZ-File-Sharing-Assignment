from flask import Blueprint, request, jsonify
from models import create_user, verify_email, login_user
import re

auth_bp = Blueprint('auth', __name__)

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.form
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    
   
    if not username or not password or not email:
        return jsonify({"error": "All fields (username, password, email) are required"}), 400
    
    
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format"}), 400
    
    
    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters long"}), 400
    
   
    response = create_user(username, password, email)
    return jsonify(response)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.form
    username = data.get('username')
    password = data.get('password')
    
    
    if not username or not password:
        return jsonify({"error": "Both username and password are required"}), 400
    
  
    response = login_user(username, password)
    return jsonify(response)
