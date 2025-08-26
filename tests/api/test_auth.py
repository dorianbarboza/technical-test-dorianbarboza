def test_login(client, monkeypatch):
    fake_response = {"access_token": "fake-token", "token_type": "bearer"}

    monkeypatch.setattr(
        "app.application.auth_use_case.AuthUseCase.login",
        lambda self, email, password: fake_response
    )

    response = client.post("/auth/login", json={"email": "test@test.com", "password": "1234"})
    assert response.status_code == 200
    assert response.json() == fake_response
