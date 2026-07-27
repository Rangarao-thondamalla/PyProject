import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os


def get_connection():
    try:
        print("Loading necessary credentials from dotenv")

        load_dotenv(dotenv_path='.env')

        conn = mysql.connector.connect(
            host=os.getenv("HOST"),
            port=int(os.getenv("PORT", 3306)),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DB")
        )
        if conn.is_connected():
            print("SUCCESS: Connection successful...")
        return conn

    except Error as e:
        print(f"ERROR: Could not connect: {e}")
        return None


get_connection()
