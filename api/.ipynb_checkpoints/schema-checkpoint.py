from pydantic import BaseModel

class PredictionRequest(BaseModel):
    user_id: str
    age: int
    daily_active_time: float
    posts_last_week: int
    likes_last_week: int
    activity_type: str
    past_participation_rate: float
    friends_participating: int
    time_of_day: str
    day_of_week: str


class FeedbackRequest(BaseModel):
    user_id: str
    action: str
    success: bool