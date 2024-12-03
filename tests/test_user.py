from fastapi.testclient import TestClient
from app.main import app
from app import schemas
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.database import get_db


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)

def test_root():
    response = client.get("/")
    print(response.json().get("message"))
    assert response.json().get("message") == "Hello World"
    assert response.status_code == 200

def test_create_user():
    response = client.post("/users/", json={"email": "hp@gmail.com", "password": "string123"})
    new_user = schemas.UserOut(**response.json())
    assert new_user.email == "hp@gmail.com"
    assert response.status_code == 201
