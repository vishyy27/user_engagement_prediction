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


def update_user_profile(user_id, score):
    conn = get_connection()
    cursor = conn.cursor()

    #Checking if user exists in user_profile
    cursor.execute(
        "SELECT total_predictions FROM user_profile WHERE user_id = ?",
        (user_id,)
    )
    row = cursor.fetchone()

    if row:
        total_predictions = row[0] + 1

        cursor.execute("""
        UPDATE user_profile
        SET last_score = ?, total_predictions = ?
        WHERE user_id = ?
        """, (float(score), total_predictions, user_id))

    else:
        cursor.execute("""
        INSERT INTO user_profile (user_id, last_score, total_predictions)
        VALUES (?, ?, ?)
        """, (user_id, float(score), 1))

    conn.commit()
    conn.close()