from database.db import get_connection

def store_feedback(user_id, action, success):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO feedback (user_id, action_taken, success)
    VALUES (?, ?, ?)
    """, (user_id, action, success))

    conn.commit()
    conn.close()