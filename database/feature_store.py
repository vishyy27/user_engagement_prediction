from database.db import get_connection
from database.models import UserProfile

def get_user_features(user_id):
    db = get_connection()

    user = db.query(UserProfile).filter(
        UserProfile.user_id == user_id
    ).first()

    if not user:
        return {
            "avg_engagement_score": 0,
            "total_predictions": 0,
            "last_score": 0
        }

    return {
        "avg_engagement_score": user.avg_engagement_score or 0,
        "total_predictions": user.total_predictions or 0,
        "last_score": user.last_score or 0
    }

def update_user_features(user_id, new_score):
    db = get_connection()

    print("Updating user:", user_id)

    user = db.query(UserProfile).filter(
        UserProfile.user_id == user_id
    ).first()

    print("Found user:", user)

    if not user:
        print("Creating new user")

        user = UserProfile(
            user_id=user_id,
            avg_engagement_score=new_score,
            total_predictions=1,
            last_score=new_score
        )
        db.add(user)

    else:
        print("Updating existing user")

        total = user.total_predictions + 1
        avg = ((user.avg_engagement_score * user.total_predictions) + new_score) / total

        user.avg_engagement_score = avg
        user.total_predictions = total
        user.last_score = new_score

    db.commit()
    db.close()