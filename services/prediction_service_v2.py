import pickle
import numpy as np

model = pickle.load(open("models/model_v2.pkl", "rb"))

def predict_v2(features):
    X = np.array(list(features.values())).reshape(1, -1)

    probs = model.predict_proba(X)[0]

    score = probs[1]
    confidence = max(probs)

    return {
        "engagement_score": int(score * 100),
        "confidence": round(confidence, 2)
    }