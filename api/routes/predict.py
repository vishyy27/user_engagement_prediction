from fastapi import APIRouter
from services.prediction_service import predict_user
from services.user_service import create_user

router = APIRouter()

@router.post("/predict")
def predict_api(data: dict):
    user_id = data.get("user_id")

    create_user(user_id)

    result = predict_user(data)

    return result