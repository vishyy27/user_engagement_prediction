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
