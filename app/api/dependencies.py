from fastapi import Security, Depends, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
from app.application.auth_use_case import AuthUseCase
from app.domain.services.user_service import UserService
from app.domain.services.auth_service import AuthService
from app.infrastructure.repositories.postgresql_user_repository import PostgresUserRepository
from app.infrastructure.database import get_db
from sqlalchemy.orm import Session

# Cabecera para Swagger Authorize
api_key_scheme = APIKeyHeader(name="Authorization", auto_error=False)

def get_current_user(
    authorization: str = Security(api_key_scheme),
    db: Session = Depends(get_db)
):
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token requerido")

    # Quita prefijo Bearer
    token = authorization.split(" ")[-1]

    auth_service = AuthService()
    user_service = UserService(PostgresUserRepository(db), auth_service)
    auth_use_case = AuthUseCase(user_service)

    user = auth_use_case.validate_token(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido o expirado")
    return user
