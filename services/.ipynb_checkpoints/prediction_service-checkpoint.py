from src.predict import predict
from services.user_service import update_user_profile
from src.reason_engine import generate_reason
from services.suggestion_service import generate_suggestion
from database.db import get_connection
from database.models import Prediction
import pandas as pd

def predict_user(data):
    user_id = data.get("user_id")

    data_copy = data.copy()
    data_copy.pop("user_id", None)

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

    score, engaged = predict(df)

    update_user_profile(user_id, score)

    reason = generate_reason(data)
    suggestion = generate_suggestion(data, score, user_id)

    db = get_connection()

    new_prediction = Prediction(
        user_id=user_id,
        score=int(score),
        prediction=int(engaged)
    )

    db.add(new_prediction)
    db.commit()
    db.close()

    return {
        "user_id": user_id,
        "engagement_score": score,
        "engaged": engaged,
        "reason": reason,
        "suggestion": suggestion
    }