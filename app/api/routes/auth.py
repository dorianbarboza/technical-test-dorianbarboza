# app/api/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.domain.services.user_service import UserService
from app.domain.services.auth_service import AuthService
from app.infrastructure.repositories.postgresql_user_repository import PostgresUserRepository
from app.application.auth_use_case import AuthUseCase
from app.api.schemas import LoginRequest


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def login(
    data: LoginRequest, 
    db: Session = Depends(get_db)
    ):

    user_repo = PostgresUserRepository(db)
    auth_service = AuthService()
    user_service = UserService(user_repo, auth_service)
    use_case = AuthUseCase(user_service)

    try:
        return use_case.login(data.email, data.password)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )
