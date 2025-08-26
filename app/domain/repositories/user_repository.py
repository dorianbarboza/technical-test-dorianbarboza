# domain/repositories.py
from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    def add(self, user: User) -> User:
        """Agrega un usuario nuevo"""
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        """Obtiene un usuario por email"""
        pass

    @abstractmethod
    def list_admins(self) -> List[User]:
        """Lista todos los usuarios administradores"""
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        """Actualiza un usuario existente"""
        pass

    @abstractmethod
    def delete(self, email: str) -> None:
        """Elimina un usuario por email"""
        pass
