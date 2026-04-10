from database.db import get_connection

def create_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO users (user_id)
    VALUES (?)
    """, (user_id,))

    conn.commit()
    conn.close()