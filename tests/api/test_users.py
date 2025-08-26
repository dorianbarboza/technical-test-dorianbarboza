# tests/api/test_users.py
import pytest
from fastapi import status

from tests.factories import create_user


# Test GET /users/admins
def test_list_admins(client, monkeypatch):
    fake_admins = [create_user()]

    monkeypatch.setattr(
        "app.application.user_use_cases.ListAdminsUseCase.execute",
        lambda self: fake_admins
    )

    response = client.get("/users/admins")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert data[0]["email"] == "admin@test.com"
    assert data[0]["is_admin"] is True


# Test POST /users/admins
def test_create_user(client, monkeypatch):
    input_data = {
        "email": "newadmin@test.com",
        "is_admin": True,
        "password":"f438fhp3849"
    }

    fake_user = create_user(email="newadmin@test.com")

    monkeypatch.setattr(
        "app.application.user_use_cases.CreateUserUseCase.execute",
        lambda self, user_dict, current_user: fake_user
    )

    response = client.post("/users/admins", json=input_data)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["email"] == "newadmin@test.com"
    assert data["is_admin"] is True


# Test PUT /users/admins/{email}
def test_update_user(client, monkeypatch):
    updated_user = create_user()

    monkeypatch.setattr(
        "app.application.user_use_cases.UpdateUserUseCase.execute",
        lambda self, email, update_dict, current_user: updated_user
    )

    response = client.put("/users/admins/admin@test.com", json={"is_admin": False})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["is_admin"] is True  # reflejando el fake_user


# Test DELETE /users/admins/{email}
def test_delete_user(client, monkeypatch):
    monkeypatch.setattr(
        "app.application.user_use_cases.DeleteUserUseCase.execute",
        lambda self, email, current_user: None
    )

    response = client.delete("/users/admins/admin@test.com")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["detail"] == "Admin deleted successfully"
