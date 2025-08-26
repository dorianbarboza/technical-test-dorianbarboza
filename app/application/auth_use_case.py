# app/application/use_cases/auth_use_case.py
from app.domain.services.user_service import UserService

class AuthUseCase:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def login(self, email: str, password: str) -> dict:
        token = self.user_service.authenticate(email, password)
        if not token:
            raise ValueError("Credenciales inválidas")
        return {"access_token": token, "token_type": "bearer"}
    


    def validate_token(self, token: str):
      
        user = self.user_service.get_user_from_token(token)
        if not user:
            raise ValueError("Token inválido")
        return user
