#!/usr/bin/python3
"""
A simple Python script to create the 'alx_book_store' database in MySQL.
- If the database already exists, the script will not fail.
- The script handles connection and exceptions properly.
- No SELECT or SHOW statements are used.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    """Creates the 'alx_book_store' database if it doesn't exist."""
    connection = None
    try:
        # Connect to MySQL Server (edit user/password as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"   # Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it doesn’t already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL or creating database: {e}")

    finally:
        # Ensure cursor and connection are properly closed
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()

