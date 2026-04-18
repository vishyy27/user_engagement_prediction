from database.db import get_connection
from database.models import UserProfile
from services.rl_engine import choose_action

#Get user profile
def get_user_profile(user_id):
    db = get_connection()

    user = db.query(UserProfile).filter(
        UserProfile.user_id == user_id
    ).first()

    db.close()

    if not user:
        return None

    return user.avg_engagement_score, user.total_predictions

#Main logic
def generate_suggestion(data, score, user_id, segment=None):
    suggestions = []

    #Fallback
    if data.get("daily_active_time", 0) < 30:
        suggestions.append("Send personalized notifications to increase app usage")

    if data.get("posts_last_week", 0) < 2:
        suggestions.append("Encourage content creation with prompts or rewards")

    if data.get("likes_last_week", 0) < 5:
        suggestions.append("Show more engaging content to boost interaction")

    #User Profile Logic
    profile = get_user_profile(user_id)

    if profile:
        avg_score, total = profile

        if avg_score is not None and avg_score < 30:
            suggestions.append("User has consistently low engagement → trigger re-engagement campaign")

        if total is not None and total > 5:
            suggestions.append("Loyal user → use rewards or gamification strategies")

    #RL Based Decision
    rl_suggestion = None

    if segment:
        action = choose_action(segment)

        action_map = {
            "Send Notification": "Send a targeted push notification at optimal time",
            "Recommend Content": "Recommend personalized content based on interests",
            "Offer Discount": "Provide limited-time incentives to boost engagement",
            "Trigger Email": "Send a re-engagement email campaign"
        }

        rl_suggestion = action_map.get(action)

    #Priority
    if rl_suggestion:
        return rl_suggestion

    #Fallback
    if suggestions:
        return " | ".join(suggestions)

    return "Maintain engagement with personalized content and timely notifications"