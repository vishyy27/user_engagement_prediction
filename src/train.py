import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

from preprocess import get_preprocessor

#Synthetic Data
np.random.seed(42)

n = 1000

df = pd.DataFrame({
    "age": np.random.randint(18, 60, n),
    "daily_active_time": np.random.randint(10, 300, n),
    "posts_last_week": np.random.randint(0, 20, n),
    "likes_last_week": np.random.randint(0, 200, n),
    "activity_type": np.random.choice(["tech", "sports", "music"], n),
    "past_participation_rate": np.random.rand(n),
    "friends_participating": np.random.randint(0, 10, n),
    "time_of_day": np.random.choice(["morning", "afternoon", "evening"], n),
    "day_of_week": np.random.choice(["weekday", "weekend"], n),
})

df["engaged"] = (
    (df["daily_active_time"] > 100) &
    (df["likes_last_week"] > 50)
).astype(int)

#Split
X = df.drop("engaged", axis=1)
y = df["engaged"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#Pipeline
preprocessor = get_preprocessor()

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestClassifier(random_state=42))
])

#Train
pipeline.fit(X_train, y_train)

#Save
with open("../models/model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("✅ Model trained and saved!")