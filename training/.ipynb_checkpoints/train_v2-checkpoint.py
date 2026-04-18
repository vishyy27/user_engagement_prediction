import pandas as pd
import xgboost as xgb
import pickle

df = pd.read_csv("data/training_data.csv")

X = df.drop("label", axis=1)
y = df["label"]

model = xgb.XGBClassifier(
    n_estimators=150,
    max_depth=6,
    learning_rate=0.1
)

model.fit(X, y)

pickle.dump(model, open("models/model_v2.pkl", "wb"))