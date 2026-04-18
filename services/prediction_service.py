from features.temporal_features import build_temporal_features
from services.prediction_service_v2 import predict_v2
from services.segmentation_service import segment_user
from services.rl_engine import choose_action, update_q

from src.predict import predict
from services.user_service import update_user_profile
from src.reason_engine import generate_reason
from services.suggestion_service import generate_suggestion

from database.db import get_connection
from database.models import Prediction

import pandas as pd
from datetime import datetime


def get_user_history(user_id):
    db = get_connection()

    rows = db.query(Prediction).filter(
        Prediction.user_id == user_id
    ).all()

    db.close()

    history = []

    for row in rows:
        history.append({
            "engagement_score": row.score,
            "timestamp": str(row.created_at) if hasattr(row, "created_at") else str(datetime.utcnow())
        })

    return history


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

    #fallback model
    base_score, _ = predict(df)

    #temporal features
    user_history = get_user_history(user_id)

    if len(user_history) < 2:
        temporal_features = {
            "engagement_trend": 0,
            "session_frequency": len(user_history),
            "inactivity_days": 0
        }
    else:
        temporal_features = build_temporal_features(user_history)

    #advanced model
    prediction_v2 = predict_v2(temporal_features)

    score = prediction_v2["engagement_score"]
    confidence = prediction_v2["confidence"]

    if confidence < 0.55:
        score = int(base_score)

    engaged = int(score > 50)

    #segmentation
    segment = segment_user(temporal_features)

    #RL decision
    action = choose_action(segment)

    #temporary reward
    reward = 1 if engaged else 0
    update_q(segment, action, reward)

    #update profile
    update_user_profile(user_id, score)

    #reasoning and suggestion
    reason = generate_reason(data)

    suggestion = generate_suggestion(
        data,
        score,
        user_id,
        segment
    )

    #store prediction
    db = get_connection()

    new_prediction = Prediction(
        user_id=user_id,
        score=int(score),
        prediction=engaged,
        created_at=datetime.utcnow()
    )

    db.add(new_prediction)
    db.commit()
    db.close()

    return {
        "user_id": user_id,
        "engagement_score": score,
        "confidence": confidence,
        "segment": segment,
        "recommended_action": action,
        "engaged": engaged,
        "reason": reason,
        "suggestion": suggestion
    }