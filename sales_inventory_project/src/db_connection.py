import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="admin",
        password="chandan1997@A",
        database="sales_db"
    )