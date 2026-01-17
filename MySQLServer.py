import mysql.connector
from mysql.connector import Error


connection = None
cursor = None

try:
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'admin'
    )

    if connection.is_connected():
        cursor = connection.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print ("Database 'alx_book_store' created successfully!")

except mysql.connector.Error  as e :
    print(f"Error connecting to MYSQL: {e}")

finally:
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()