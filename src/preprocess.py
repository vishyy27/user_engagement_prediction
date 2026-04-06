from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

def get_preprocessor():
    categorical_features = ["activity_type", "time_of_day", "day_of_week"]

    numerical_features = [
        "age",
        "daily_active_time",
        "posts_last_week",
        "likes_last_week",
        "past_participation_rate",
        "friends_participating"
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
            ("num", "passthrough", numerical_features)
        ]
    )

    return preprocessor