#!/usr/bin/python3
"""
A simple Python script to create the 'alx_book_store' database in MySQL.
If the database already exists, the script will not fail.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    """Connects to MySQL server and creates the 'alx_book_store' database."""
    connection = None
    try:
        # Connect to MySQL Server (update user/password if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'   # Replace with your actual MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL or creating database: {e}")

    finally:
        # Close the connection properly
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            # Optional message to confirm closure
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()

