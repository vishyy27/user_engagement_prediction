import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from fastapi import FastAPI
import pandas as pd

from src.predict import predict_engagement
from src.reason_engine import generate_reason
from src.suggestion_engine import generate_suggestion

app = FastAPI()


@app.get("/")
def home():
    return {"message": "User Engagement Intelligence API 🚀"}


@app.post("/predict")
def predict(data: dict):

    #Ensuring correct feature order
    df = pd.DataFrame([data])

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

    #Step 1: Prediction → Score
    score, engaged = predict_engagement(df)

    #Step 2: Reason generation
    reason = generate_reason(data)

    #Step 3: Suggestion generation
    suggestion = generate_suggestion(data, score)

    #Final response
    return {
        "engagement_score": score,
        "engaged": engaged,
        "reason": reason,
        "suggestion": suggestion
    }