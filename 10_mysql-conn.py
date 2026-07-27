import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import pandas as pd 

def get_connection():
    try:
        print("Loading necessary credentails from dotenv")

        load_dotenv()

        conn = mysql.connector.connect(
            host=os.getenv("HOST"),
            port=os.getenv("PORT"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD")
        )
        if conn.is_connected():
            print("SUCCESS: Connection successful...")
        return conn 
    
    except Error as e:
        print(f"ERROR: Could not able to connect: {e}")    
        return None   
     
get_connection()
