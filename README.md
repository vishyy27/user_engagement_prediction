
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
````

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

* 0–30: Low engagement
* 30–70: Moderate engagement
* 70–100: High engagement

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

* Modular structure using FastAPI
* Separation of concerns:

  * API Layer: Request handling
  * Service Layer: Business logic
  * ML Layer: Prediction and intelligence

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

* users
* predictions
* feedback

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

## Phase 4: Intelligent User Engagement System

### Objective

Introduce stateful learning and adaptive intelligence using user behavior tracking.

### Key Enhancements

#### 1. User Profile System (Feature Store)

A new `user_profile` table stores:

* avg_engagement_score
* total_predictions
* last_score
* last_active

This enables the system to learn from historical user behavior.

---

#### 2. Feature Store Layer

Provides centralized access to user engagement data and supports adaptive decision-making.

---

#### 3. Event Logging System

Tracks user actions such as:

* prediction_requested
* high_engagement
* low_engagement

Stored in the `events` table.

---

#### 4. Adaptive Suggestion Engine

Suggestions are generated using both current input and historical user behavior.

Examples:

* Low average engagement → re-engagement strategies
* High activity users → gamification strategies

Includes fallback logic to ensure non-empty responses.

---

#### 5. Updated Pipeline

Input → Prediction → Score
→ User Profile Update
→ Event Logging
→ Reason Engine
→ Adaptive Suggestions
→ Database Storage
→ Response

---

#### 6. New Tables

* user_profile
* events

---

## Phase 5: Real-Time Engagement Intelligence System

### Objective

Transform the system into a real-time, behavior-driven intelligence engine capable of continuous learning and adaptive decision-making.

### Key Enhancements

#### 1. Event-Driven Architecture

The system operates based on user events rather than static inputs.

---

#### 2. Continuous Learning System

User profiles are dynamically updated after each prediction, enabling long-term personalization.

---

#### 3. Intelligent Decision Layer

The system performs:

* Prediction
* Explanation
* Recommendation
* Adaptation

---

#### 4. Production-Grade Architecture

* Feature Store pattern
* Event Logging system
* Modular service-based design
* Stateful backend

---

#### 5. System Evolution

| Capability            | Phase 1 | Phase 3 | Phase 5 |
| --------------------- | ------- | ------- | ------- |
| Prediction            | Yes     | Yes     | Yes     |
| Explainability        | No      | Yes     | Yes     |
| Suggestions           | No      | Yes     | Yes     |
| Database              | No      | Yes     | Yes     |
| User Memory           | No      | Yes     | Yes     |
| Event Tracking        | No      | No      | Yes     |
| Adaptive Intelligence | No      | No      | Yes     |
| Real-Time System      | No      | No      | Yes     |

---

## API Endpoints

| Endpoint    | Method | Description                         |
| ----------- | ------ | ----------------------------------- |
| `/`         | GET    | Health check                        |
| `/predict`  | POST   | Full engagement prediction pipeline |
| `/feedback` | POST   | Store user feedback                 |

---

## Example Response

```json
{
  "user_id": "user_1",
  "engagement_score": 59,
  "engaged": 1,
  "reason": "Good engagement behavior",
  "suggestion": "Maintain current engagement strategy"
}
```

---

## Input Features

* age
* daily_active_time
* posts_last_week
* likes_last_week
* activity_type
* past_participation_rate
* friends_participating
* time_of_day
* day_of_week

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
│   ├── suggestion_service.py
│   ├── event_logger.py
│
├── src/
│   ├── train.py
│   ├── preprocess.py
│   ├── predict.py
│   ├── reason_engine.py
│
├── database/
│   ├── db.py
│   ├── models.py
│   ├── feature_store.py
│
├── models/
│   └── model.pkl
│
├── notebooks/
├── README.md
```

---

## Tech Stack

* Python
* FastAPI
* Scikit-learn
* Pandas
* SQLAlchemy
* PostgreSQL / SQLite
* Uvicorn

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
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Key Contributions

* Designed an end-to-end ML pipeline for engagement prediction
* Implemented probabilistic engagement scoring
* Built a reasoning engine for explainability
* Developed an adaptive suggestion system
* Created a modular backend using FastAPI
* Integrated database with SQLAlchemy ORM
* Implemented feature store and user profile tracking
* Built event-driven architecture for behavior tracking
* Developed a stateful intelligent system

---

## Future Work

* Model-based explainability (SHAP/LIME)
* User segmentation (clustering)
* Reinforcement learning for recommendations
* Real-time streaming pipelines
* Analytics dashboard
* Cloud deployment

---

## Author

Vishwas Desai
