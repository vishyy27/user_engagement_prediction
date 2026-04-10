# User Engagement Intelligence System

## Overview

This project is an end-to-end machine learning system designed to predict, analyze, and improve user engagement based on behavioral data.

It began as a binary classification model and has evolved into a production-ready intelligence system that combines:

- Machine learning predictions  
- Explainability through reasoning  
- Actionable recommendations  
- API-based deployment  
- Database integration  

The objective is to move beyond prediction and enable data-driven product decision making.

---

## Phase 1: Engagement Prediction

### Objective

Predict whether a user is engaged or not based on behavioral features.

### Implementation

- Model: RandomForestClassifier  
- Preprocessing: ColumnTransformer with OneHotEncoder  
- Pipeline: End-to-end workflow combining preprocessing and model  

### API

- `GET /` — Health check  
- `POST /predict` — Returns binary engagement prediction  

### Output

```json
{
  "engaged": 1
}
```

---

## Phase 2: Engagement Intelligence System

### Objective

Transform the system from a prediction model into an intelligence layer that supports decision-making.

### Key Enhancements

#### 1. Engagement Scoring

Binary output replaced with a continuous score derived from model probability.

```json
"engagement_score": 0–100
```

Score interpretation:

- 0–30: Low engagement  
- 30–70: Moderate engagement  
- 70–100: High engagement  

---

#### 2. Explainability Layer

A rule-based reasoning engine provides context for predictions.

```json
"reason": "Low activity time and low interaction"
```

---

#### 3. Suggestion Engine

A recommendation layer provides actionable steps to improve engagement.

```json
"suggestion": "Encourage interaction through targeted content and notifications"
```

---

#### 4. Enhanced API Response

```json
{
  "engagement_score": 32,
  "engaged": 0,
  "reason": "Low activity and low participation",
  "suggestion": "Encourage interaction through social features"
}
```

---

## Phase 3: Production-Ready Backend System

### Objective

Convert the intelligence system into a scalable backend service with proper API structure, validation, and persistent storage.

### Key Enhancements

#### 1. Backend Architecture

- Modular structure using FastAPI  
- Separation of concerns:
  - API Layer: Request handling  
  - Service Layer: Business logic  
  - ML Layer: Prediction and intelligence  

---

#### 2. Structured Request Handling

API accepts structured JSON input for prediction:

```json
{
  "user_id": "user_1",
  "age": 22,
  "daily_active_time": 20,
  "posts_last_week": 1,
  "likes_last_week": 5,
  "activity_type": "passive",
  "past_participation_rate": 0.2,
  "friends_participating": 1,
  "time_of_day": "evening",
  "day_of_week": "weekday"
}
```

---

#### 3. Database Integration

SQLite database added to store system outputs and user interactions.

Tables:

- users  
- predictions  
- feedback  

---

#### 4. End-to-End Pipeline

1. Input data received via API  
2. Data validated and converted into DataFrame  
3. Preprocessing applied via pipeline  
4. Model outputs probability  
5. Probability converted to engagement score  
6. Reason engine generates explanation  
7. Suggestion engine generates recommendations  
8. Results stored in database  
9. Response returned to client  

---

#### 5. Feedback System

Allows capturing user actions for future improvements.

```json
POST /feedback
{
  "user_id": "user_1",
  "action": "clicked_notification",
  "success": true
}
```

---

## API Endpoints

| Endpoint    | Method | Description                          |
|------------|--------|--------------------------------------|
| `/`        | GET    | Health check                         |
| `/predict` | POST   | Full engagement prediction pipeline  |
| `/feedback`| POST   | Store user feedback                  |

---

## Example Response

```json
{
  "user_id": "user_1",
  "engagement_score": 45,
  "engaged": 0,
  "reason": "Low activity and low participation",
  "suggestion": "Increase engagement through notifications and social features"
}
```

---

## Input Features

- age  
- daily_active_time  
- posts_last_week  
- likes_last_week  
- activity_type  
- past_participation_rate  
- friends_participating  
- time_of_day  
- day_of_week  

---

## Project Structure

```
User_Engagement_Prediction/
│
├── api/
│   └── app.py
│
├── services/
│   ├── prediction_service.py
│   ├── user_service.py
│   ├── feedback_service.py
│
├── src/
│   ├── train.py
│   ├── preprocess.py
│   ├── predict.py
│   ├── reason_engine.py
│   ├── suggestion_engine.py
│
├── database/
│   ├── db.py
│   └── setup_db.py
│
├── models/
│   └── model.pkl
│
├── notebooks/
├── README.md
```

---

## Tech Stack

- Python  
- FastAPI  
- Scikit-learn  
- Pandas  
- SQLite  
- Uvicorn  

---

## Running the Project

```bash
git clone <repository-url>
cd User_Engagement_Prediction

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python database/setup_db.py

uvicorn api.app:app --reload
```

API documentation:
http://127.0.0.1:8000/docs

---

## Key Contributions

- Designed an end-to-end ML pipeline for engagement prediction  
- Extended model output to probabilistic scoring  
- Built a reasoning layer for explainability  
- Implemented a suggestion engine for actionable insights  
- Developed a modular backend architecture using FastAPI  
- Integrated database for persistence and tracking  
- Implemented feedback loop structure  

---

## Future Work

- Replace rule-based reasoning with model-based explainability (e.g., SHAP)  
- Introduce user segmentation using clustering  
- Implement feedback-driven model retraining  
- Add real-time streaming pipeline  
- Build analytics dashboard  
- Deploy system on cloud infrastructure  

---

## Author

Vishwas Desai
