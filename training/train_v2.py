import pandas as pd
import xgboost as xgb
import pickle
from sklearn.preprocessing import LabelEncoder

# load data
df = pd.read_csv("data/training_data.csv")

# encode categorical columns
categorical_cols = ["activity_type", "time_of_day", "day_of_week"]

encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# split
X = df.drop("label", axis=1)
y = df["label"]

# train model
model = xgb.XGBClassifier(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1
)

model.fit(X, y)

# save model
pickle.dump(model, open("models/model_v2.pkl", "wb"))

# save encoders (IMPORTANT)
pickle.dump(encoders, open("models/encoders.pkl", "wb"))

print("model_v2 trained and saved")