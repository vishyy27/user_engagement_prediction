from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

# Load model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)


@app.get("/")
def home():
    return {"message": "User Engagement Prediction API"}


@app.post("/predict")
def predict(data: dict):
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

    prediction = model.predict(df)

    return {"engaged": int(prediction[0])}
    