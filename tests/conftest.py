# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from unittest.mock import MagicMock

from app.api.routes import auth, users, products
from app.api.dependencies import get_current_user

@pytest.fixture(scope="module")
def app():
    test_app = FastAPI()
    test_app.include_router(auth.router)
    test_app.include_router(users.router)
    test_app.include_router(products.router)

    # Override global del current_user
    test_app.dependency_overrides[get_current_user] = lambda: {"email": "admin@test.com", "role": "admin"}

    return test_app

@pytest.fixture
def client(app):
    return TestClient(app)

@pytest.fixture
def mock_db():
    return MagicMock()
