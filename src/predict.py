import joblib
import pandas as pd

model = joblib.load("models/engagement_model.pkl")

def predict_user(data: dict):
    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }