from database.db import get_connection
from database.models import UserProfile

def update_user_profile(user_id, new_score):
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
        total = user.total_predictions + 1
        avg = ((user.avg_engagement_score * user.total_predictions) + new_score) / total

        user.avg_engagement_score = avg
        user.total_predictions = total
        user.last_score = new_score

    db.commit()
    db.close()