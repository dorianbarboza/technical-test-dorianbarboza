# infrastructure/repositories/user_repository.py
from typing import List, Optional

from app.domain.entities.user import User
from app.domain.repositories.user_repository import IUserRepository

class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self._users = {}  # clave = email, valor = User

    def add(self, user: User) -> User:
        self._users[user.email] = user
        return user

    def get_by_email(self, email: str) -> Optional[User]:
        return self._users.get(email)

    def list_admins(self) -> List[User]:
        return [u for u in self._users.values() if u.is_admin]

    def update(self, user: User) -> User:
        if user.email not in self._users:
            raise ValueError("User not found")
        self._users[user.email] = user
        return user

    def delete(self, email: str) -> None:
        if email in self._users:
            del self._users[email]
