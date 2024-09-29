from flask import Flask
from config import db
from auth import auth_bp
from file_operations import file_bp

app = Flask(__name__)


#register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(file_bp)

if __name__ == "__main__":
    app.run(debug=False)  