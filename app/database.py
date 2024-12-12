from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your PlanetScale connection string
DATABASE_URL = "mysql+mysqlconnector://sq_ballfedtry:13d9e0d2646f0cf4def95f6ebff9fabb59bba417@i-0ea.h.filess.io:3307/sq_ballfedtry"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
