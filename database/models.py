from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Text, TIMESTAMP
from sqlalchemy.sql import func

Base = declarative_base()

#Users Table
class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True)
    created_at = Column(TIMESTAMP, server_default=func.now())


#Predictions Table
class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String)
    score = Column(Integer)
    prediction = Column(Integer)
    timestamp = Column(TIMESTAMP, server_default=func.now())


#Feedback Table
class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String)
    action_taken = Column(Text)
    success = Column(Integer)
    timestamp = Column(TIMESTAMP, server_default=func.now())


#User Profile Table
class UserProfile(Base):
    __tablename__ = "user_profile"

    user_id = Column(String, primary_key=True)
    avg_engagement_score = Column(Float)
    total_predictions = Column(Integer)
    last_score = Column(Float)
    last_active = Column(TIMESTAMP, server_default=func.now())