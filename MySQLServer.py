#!/usr/bin/python3
"""
Script to create the 'alx_book_store' database in MySQL.
"""

import mysql.connector
from mysql.connector import Error

try:
    # Establish connection to the MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"  # Replace with your MySQL root password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create database if it doesn't exist (no SELECT or SHOW statements)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as err:
    print(f"Error: {err}")

finally:
    # Close all connections properly
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()

