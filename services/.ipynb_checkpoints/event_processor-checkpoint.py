from database.feature_store import update_user_features

def process_event(event_type, user_id, data=None):

    if event_type == "prediction_requested":
        score = 50   #default dummy score

    elif event_type == "high_engagement":
        score = 90

    elif event_type == "low_engagement":
        score = 20

    else:
        score = 40

    #Update feature store
    update_user_features(user_id, score)