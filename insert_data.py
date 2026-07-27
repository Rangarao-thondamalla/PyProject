import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os


def get_connection():
    load_dotenv(dotenv_path='.env')
    return mysql.connector.connect(
        host=os.getenv("HOST"),
        port=int(os.getenv("PORT", 3306)),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DB")
    )


try:
    conn = get_connection()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO students (name, age)
    VALUES (%s, %s)
    """
    data = ("Alice", 20)

    cursor.execute(insert_query, data)
    conn.commit()

    print("Data inserted successfully")

    cursor.close()
    conn.close()

except Error as e:
    print(f"Error: {e}")
