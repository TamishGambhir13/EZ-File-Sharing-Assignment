from itsdangerous import URLSafeTimedSerializer
from cryptography.fernet import Fernet

# Token generation for email verification
SECRET_KEY = 'your-secret-key' 
salt = 'email-confirm'

def generate_verification_token(email):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    return serializer.dumps(email, salt=salt)

def verify_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    try:
        email = serializer.loads(token, salt=salt, max_age=expiration)
    except:
        return False
    return email

# Encryption for URLs (File Download)
fernet = Fernet(Fernet.generate_key())  
def encrypt_url(url):
    return fernet.encrypt(url.encode()).decode()

def decrypt_url(encrypted_url):
    return fernet.decrypt(encrypted_url.encode()).decode()
