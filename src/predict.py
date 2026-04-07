import pickle

#Loading once
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)


def predict_engagement(df):
    proba = model.predict_proba(df)[0][1]
    score = int(proba * 100)
    engaged = 1 if score >= 50 else 0

    return score, engaged