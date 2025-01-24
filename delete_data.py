import sqlite3
from utils.db_utils import DB_PATH  # Import your database path

def delete_all_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM health_data")  # Deletes all rows from the table
    conn.commit()
    conn.close()
    print("All data deleted successfully.")

delete_all_data()
