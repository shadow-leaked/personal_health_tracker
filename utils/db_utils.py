import sqlite3
DB_PATH = "health_data.db"
# Connect to SQLite database or create one if it doesn't exist
def connect_db():
    conn = sqlite3.connect("health_data.db")  # This creates health_data.db in the project folder
    return conn

# Create a table for storing health data
def create_table():
    """
    Creates a database table if it doesn't already exist.
    """
    conn = sqlite3.connect("health_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS health_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            weight REAL,
            height REAL,
            bmi REAL,
            steps_walked INTEGER,
            water_intake REAL,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()
    print("Table created successfully.")

# Initialize the database
if __name__ == "__main__":
    create_table()

# To insert in the database
def insert_data(name, age, gender, weight, height, bmi, steps_walked, water_intake, date):
    """
    Inserts health data into the database.
    """
    conn = sqlite3.connect("health_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO health_data (name, age, gender, weight, height, bmi, steps_walked, water_intake, date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, age, gender, weight, height, bmi, steps_walked, water_intake, date))
    conn.commit()
    conn.close()
    print("Data inserted successfully.")


