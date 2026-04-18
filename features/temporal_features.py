import pandas as pd
import numpy as np

def build_temporal_features(user_history):
    df = pd.DataFrame(user_history)

    df = df.sort_values(by="timestamp")

    #Engagement trend
    engagement_values = df["engagement_score"].values

    if len(engagement_values) >= 2:
        trend = engagement_values[-1] - engagement_values[0]
    else:
        trend = 0

    #Session frequency
    session_freq = len(df)

    #Inactivity
    last_active = pd.to_datetime(df["timestamp"].max())
    now = pd.Timestamp.now()
    inactivity_days = (now - last_active).days

    return {
        "engagement_trend": trend,
        "session_frequency": session_freq,
        "inactivity_days": inactivity_days
    }