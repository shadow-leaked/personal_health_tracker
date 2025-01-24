import sqlite3
from utils.db_utils import DB_PATH  # Import the database path from db_utils.py

def fetch_all_data():
    # Connect to the database using the correct path
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM health_data")  # Fetch all rows from the health_data table
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    # Fetch data and print each row
    data = fetch_all_data()
    for row in data:
        print(row)
