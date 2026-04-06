import pickle
import pandas as pd

def load_model():
    with open("../models/model.pkl", "rb") as f:
        return pickle.load(f)

def predict(data: dict):
    model = load_model()
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return int(prediction)