from database.db import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    #Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id TEXT PRIMARY KEY,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    #Predictions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        score INTEGER,
        prediction INTEGER,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    #Feedback table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        action_taken TEXT,
        success INTEGER,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()