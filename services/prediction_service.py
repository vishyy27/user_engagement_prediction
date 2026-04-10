from src.predict import predict
from src.reason_engine import generate_reason
from src.suggestion_engine import generate_suggestion
from database.db import get_connection
import pandas as pd

def predict_user(data):
    user_id = data.get("user_id")

    # 🔥 REMOVE user_id before model
    data_copy = data.copy()
    data_copy.pop("user_id", None)

    # Convert to DataFrame
    df = pd.DataFrame([data_copy])

    df = df[[
        "age",
        "daily_active_time",
        "posts_last_week",
        "likes_last_week",
        "activity_type",
        "past_participation_rate",
        "friends_participating",
        "time_of_day",
        "day_of_week"
    ]]

    # Prediction
    score, engaged = predict(df)

    # Reasoning & Suggestion
    reason = generate_reason(data)
    suggestion = generate_suggestion(data, score)

    # Store in DB
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions (user_id, score, prediction)
    VALUES (?, ?, ?)
    """, (user_id, int(score), int(engaged)))

    conn.commit()
    conn.close()

    return {
        "user_id": user_id,
        "engagement_score": score,
        "engaged": engaged,
        "reason": reason,
        "suggestion": suggestion
    }