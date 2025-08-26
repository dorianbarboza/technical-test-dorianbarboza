# services/user_service.py
from typing import List

from app.domain.entities.user import User
from app.domain.repositories.user_repository import IUserRepository


from passlib.context import CryptContext
from app.domain.services.auth_service import AuthService


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, user_repo: IUserRepository, auth_service: AuthService):
        self.user_repo = user_repo
        self.auth_service = auth_service

    def create_user(self, email: str, password: str, is_admin: bool = False, current_user: User = None) -> User:
        if current_user and not current_user.is_admin:
            raise PermissionError("Only admins can create users")
        hashed_pw = pwd_context.hash(password)
        user = User(email=email, hashed_password=hashed_pw, is_admin=is_admin)
        return self.user_repo.add(user)

    def authenticate(self, email: str, password: str) -> str | None:
        user = self.user_repo.get_by_email(email)
        if not user or not pwd_context.verify(password, user.hashed_password):
            return None
        return self.auth_service.create_access_token({"sub": user.email})
    
    def get_user_from_token(self, token: str) -> User | None:
        
        user = self.auth_service.decode_access_token(token)

        if not user:
            return None
        return self.user_repo.get_by_email(user.email)


    def update_user(self, email: str, data: dict, current_user: User) -> User:
        if not current_user.is_admin:
            raise PermissionError("Only admins can update users")
        user = self.user_repo.get_by_email(email)
        
        if not user:
            raise ValueError("User not found")
        
        # if data["email"]:
            # raise ValueError("No se puede cambiar el correo")
        if data["is_admin"]:
            user.is_admin = data["is_admin"]
        # if data["password"]:
            # raise ValueError("No se puede cambiar la contrasena")

        # for k, v in data.items():
        #     setattr(user, k, v)
        return self.user_repo.update(user)

    def delete_user(self, email: str, current_user: User):
        if not current_user.is_admin:
            raise PermissionError("Only admins can delete users")
        self.user_repo.delete(email)

    def list_admins(self) -> List[User]:
        return self.user_repo.list_admins()
