import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (not to a specific database yet)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="RueSQL-1234"
    )

    if mydb.is_connected():
        cur = mydb.cursor()
        # Create database if it doesn't exist
        cur.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
except Error as err:
    print(f"Error: {err}")
finally:
    # Close connection if open
    if 'mydb' in locals() and mydb.is_connected():
        cur.close()
        mydb.close()
