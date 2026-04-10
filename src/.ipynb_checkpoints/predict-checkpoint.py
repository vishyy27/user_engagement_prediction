import joblib
import pandas as pd

model = joblib.load("models/model.pkl")

def predict(df):

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    score = int(probability * 100)

    return score, int(prediction)