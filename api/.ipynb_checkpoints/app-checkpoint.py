from fastapi import FastAPI
from api.schema import PredictionRequest, FeedbackRequest
from services.prediction_service import predict_user
from services.user_service import create_user
from services.feedback_service import store_feedback

app = FastAPI()

@app.get("/")
def home():
    return {"message": "User Engagement Intelligence API"}


@app.post("/predict")
def predict(data: PredictionRequest):

    data = data.dict()

    user_id = data.get("user_id")

    #Ensuring user exists
    create_user(user_id)

    #Running full pipeline
    result = predict_user(data)

    return result


@app.post("/feedback")
def feedback(data: FeedbackRequest):

    data = data.dict()  

    store_feedback(
        data["user_id"],
        data["action"],
        data["success"]
    )

    return {"message": "Feedback stored successfully"}