# api/routes/users.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.domain.services.user_service import UserService
from app.domain.services.auth_service import AuthService
from app.infrastructure.repositories.postgresql_user_repository import PostgresUserRepository
# from app.infrastructure.repositories.inmemory_user_repository import InMemoryUserRepository
from app.infrastructure.database import get_db
from app.application.user_use_cases import (
    CreateUserUseCase,
    UpdateUserUseCase,
    DeleteUserUseCase,
    ListAdminsUseCase
)
from app.api.dependencies import get_current_user
from app.api.schemas import UserCreate, UserUpdate, UserOut


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/admins", response_model=List[UserOut])
def list_admins(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
    ):
    user_service = UserService(PostgresUserRepository(db), AuthService())
    use_case = ListAdminsUseCase(user_service)
    return use_case.execute()


@router.post("/admins", response_model=UserOut)
def create_user(
    user_data: UserCreate, 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
    ):
    user_service = UserService(PostgresUserRepository(db), AuthService())
    use_case = CreateUserUseCase(user_service)
    try:
        return use_case.execute(user_data.dict(), current_user)
    except PermissionError as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))


@router.put("/admins/{email}", response_model=UserOut)
def update_admin(
    email: str, 
    update_data: UserUpdate, 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
    ):
    
    user_service = UserService(PostgresUserRepository(db), AuthService())
    use_case = UpdateUserUseCase(user_service)

    try:
        return use_case.execute(email, update_data.dict(), current_user)
    except PermissionError as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/admins/{email}")
def delete_admin(
    email: str, 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
    ):

    user_service = UserService(PostgresUserRepository(db), AuthService())
    use_case = DeleteUserUseCase(user_service)
    
    try:
        use_case.execute(email, current_user)
        return {"detail": "Admin deleted successfully"}
    except PermissionError as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))
