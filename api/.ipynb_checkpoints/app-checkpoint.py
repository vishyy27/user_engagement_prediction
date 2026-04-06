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
    prediction = model.predict(df)
    return {"engaged": int(prediction[0])}
    