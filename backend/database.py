# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, Session, declarative_base
# import os
# from dotenv import load_dotenv

# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")
# BASE_URL = os.getenv("BASE_URL", "http://localhost:5000")

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# Base = declarative_base()

# def get_db() -> Session:
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///:memory:")
BASE_URL = os.getenv("BASE_URL", "http://localhost:5000")

if DATABASE_URL:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    Base = declarative_base()
else:
    engine = None
    SessionLocal = None
    Base = declarative_base()
    print("⚠️ DATABASE_URL не задан — база данных не будет использоваться")

def get_db() -> Session:
    if SessionLocal is None:
        raise RuntimeError("База данных не сконфигурирована. Проверь DATABASE_URL или настройку приложения.")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
