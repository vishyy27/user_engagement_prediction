def generate_reason(data):
    reasons = []

    if data["daily_active_time"] < 30:
        reasons.append("low activity time")

    if data["posts_last_week"] < 2:
        reasons.append("low posting behavior")

    if data["likes_last_week"] < 5:
        reasons.append("low interaction")

    if data["friends_participating"] < 3:
        reasons.append("low social circle engagement")

    if data["past_participation_rate"] < 0.3:
        reasons.append("low past participation")

    if not reasons:
        return "Good engagement behavior"

    return ", ".join(reasons)