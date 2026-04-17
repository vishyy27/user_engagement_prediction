from database.db import get_connection
from database.models import UserProfile

def get_user_profile(user_id):
    db = get_connection()

    user = db.query(UserProfile).filter(
        UserProfile.user_id == user_id
    ).first()

    db.close()

    if not user:
        return None

    return user.avg_engagement_score, user.total_predictions


def generate_suggestion(data, score, user_id):
    suggestions = []

    #Existing rule-based logic
    if data["daily_active_time"] < 30:
        suggestions.append("Send personalized notifications to increase app usage")

    if data["posts_last_week"] < 2:
        suggestions.append("Encourage content creation with prompts or rewards")

    #Adaptive logic
    profile = get_user_profile(user_id)

    if profile:
        avg_score, total = profile

        if avg_score is not None and avg_score < 30:
            suggestions.append("User consistently low engagement → trigger re-engagement campaign")

        if total is not None and total > 5:
            suggestions.append("Long-term user → use rewards or gamification strategies")

        if not suggestions:
            suggestions.append("Maintain current engagement strategy — user is performing well")

    return " | ".join(suggestions)