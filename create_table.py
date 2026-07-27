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

    create_table_query = """
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT
    )
    """

    cursor.execute(create_table_query)
    print("Table created successfully")

    conn.commit()
    cursor.close()
    conn.close()

except Error as e:
    print(f"Error: {e}")
