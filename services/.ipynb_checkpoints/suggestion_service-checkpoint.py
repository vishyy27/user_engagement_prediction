from database.db import get_connection

def get_user_profile(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT avg_engagement_score, total_predictions 
    FROM user_profile 
    WHERE user_id = ?
    """, (user_id,))

    row = cursor.fetchone()
    conn.close()
    return row

def generate_suggestion(data, score, user_id):
    suggestions = []

    #Existing rule-based logic
    if data["daily_active_time"] < 30:
        suggestions.append("Send personalized notifications to increase app usage")

    if data["posts_last_week"] < 2:
        suggestions.append("Encourage content creation with prompts or rewards")

    #New adaptive logic
    profile = get_user_profile(user_id)

    if profile:
        avg_score, total = profile

        if avg_score is not None and avg_score < 30:
            suggestions.append("User consistently low engagement → trigger re-engagement campaign")

        if total is not None and total > 5:
            suggestions.append("Long-term user → use rewards or gamification strategies")

    return " | ".join(suggestions)