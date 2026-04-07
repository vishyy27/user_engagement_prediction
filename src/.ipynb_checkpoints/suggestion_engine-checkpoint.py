def generate_suggestion(data, score):
    suggestions = []

    if data["daily_active_time"] < 30:
        suggestions.append("Send personalized notifications to increase app usage")

    if data["posts_last_week"] < 2:
        suggestions.append("Encourage content creation with prompts or rewards")

    if data["likes_last_week"] < 5:
        suggestions.append("Show more engaging or trending content")

    if data["friends_participating"] < 3:
        suggestions.append("Suggest connecting with more friends")

    if data["time_of_day"] == "night":
        suggestions.append("Send evening engagement notifications")

    if score < 30:
        suggestions.append("Trigger re-engagement campaign (emails/push)")

    if not suggestions:
        return "Maintain current engagement strategy"

    return " | ".join(suggestions)