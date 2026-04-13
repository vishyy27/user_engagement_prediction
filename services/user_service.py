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


def update_user_profile(user_id, new_score):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT avg_engagement_score, total_predictions 
    FROM user_profile 
    WHERE user_id = ?
    """, (user_id,))
    
    row = cursor.fetchone()

    if row:
        avg_score, total = row

        total += 1
        new_avg = ((avg_score * (total - 1)) + new_score) / total

        cursor.execute("""
        UPDATE user_profile
        SET avg_engagement_score = ?, total_predictions = ?, last_score = ?, last_active = CURRENT_TIMESTAMP
        WHERE user_id = ?
        """, (new_avg, total, new_score, user_id))

    else:
        cursor.execute("""
        INSERT INTO user_profile (user_id, avg_engagement_score, total_predictions, last_score)
        VALUES (?, ?, ?, ?)
        """, (user_id, new_score, 1, new_score))

    conn.commit()
    conn.close()