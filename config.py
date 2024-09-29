import mysql.connector

# Database connection configuration
def get_db_connection():
    db = mysql.connector.connect(
        host="localhost",  
        user="root", 
        password="112233****667788", # changed password
        database="file_sharing"  
    )
    return db
