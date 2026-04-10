from fastapi import APIRouter
from services.feedback_service import store_feedback

router = APIRouter()

@router.post("/feedback")
def feedback_api(data: dict):
    store_feedback(
        data["user_id"],
        data["action"],
        data["success"]
    )

    return {"message": "Feedback stored successfully"}