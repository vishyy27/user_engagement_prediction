import pickle
import numpy as np

model = pickle.load(open("models/model_v2.pkl", "rb"))
encoders = pickle.load(open("models/encoders.pkl", "rb"))

def predict_v2(features):
    # encode categorical fields
    for col, encoder in encoders.items():
        if col in features:
            features[col] = encoder.transform([features[col]])[0]

    X = np.array(list(features.values())).reshape(1, -1)

    probs = model.predict_proba(X)[0]

    return {
        "engagement_score": int(probs[1] * 100),
        "confidence": round(max(probs), 2)
    }