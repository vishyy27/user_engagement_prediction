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

    user = db.query(UserProfile).filter(
        UserProfile.user_id == user_id
    ).first()

    if not user:
        user = UserProfile(
            user_id=user_id,
            avg_engagement_score=new_score,
            total_predictions=1,
            last_score=new_score
        )
        db.add(user)

    else:
        user.total_predictions += 1
        user.last_score = new_score

        user.avg_engagement_score = (
            (user.avg_engagement_score * (user.total_predictions - 1) + new_score)
            / user.total_predictions
        )

    db.commit()
    db.close()