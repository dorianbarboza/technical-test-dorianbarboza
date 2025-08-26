# application/user_use_cases.py
from typing import List

from app.domain.entities.user import User
from app.domain.services.user_service import UserService


class CreateUserUseCase:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def execute(self, user_data: dict, current_user: User) -> User:
        return self.user_service.create_user(
            email=user_data["email"],
            password=user_data["password"],
            is_admin=user_data.get("is_admin", False),
            current_user=current_user
        )


class UpdateUserUseCase:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def execute(self, email: str, update_data: dict, current_user: User) -> User:
      
        return self.user_service.update_user(email, update_data, current_user)


class DeleteUserUseCase:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def execute(self, email: str, current_user: User):
        return self.user_service.delete_user(email, current_user)


class ListAdminsUseCase:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def execute(self) -> List[User]:
        return self.user_service.list_admins()

