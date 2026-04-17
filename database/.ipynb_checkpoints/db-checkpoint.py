
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+psycopg2://postgres.okhuxmobameefocbahpe:u5TgECEjmqqs9y2P@aws-1-ap-south-1.pooler.supabase.com:5432/postgres"

engine = create_engine(
    DATABASE_URL,
    connect_args={"sslmode": "require"}
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_connection():
    return SessionLocal()