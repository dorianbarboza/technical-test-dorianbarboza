# infrastructure/repositories/user_repository_pg.py
from sqlalchemy.orm import Session
from app.domain.entities.user import User
from app.domain.repositories.user_repository import IUserRepository
from app.infrastructure.models import UserORM

class PostgresUserRepository(IUserRepository):
    def __init__(self, db: Session):
        self.db = db

    def add(self, user: User) -> User:
        orm_obj = UserORM(**user.__dict__)
        self.db.add(orm_obj)
        self.db.commit()
        self.db.refresh(orm_obj)
        return User(**orm_obj.to_dict())

    def get_by_email(self, email: str) -> User:
        orm_obj = self.db.query(UserORM).filter(UserORM.email == email).first()
        return User(**orm_obj.to_dict()) if orm_obj else None

    def list_admins(self) -> list[User]:
        orm_objs = self.db.query(UserORM).filter(UserORM.is_admin == True).all()
        return [User(**o.to_dict()) for o in orm_objs]

    def update(self, user: User) -> User:
        orm_obj = self.db.query(UserORM).filter(UserORM.email == user.email).first()
        if not orm_obj:
            raise ValueError("User not found")
        for attr, value in user.__dict__.items():
            setattr(orm_obj, attr, value)
        self.db.commit()
        self.db.refresh(orm_obj)
        return User(**orm_obj.to_dict())

    def delete(self, email: str) -> None:
        orm_obj = self.db.query(UserORM).filter(UserORM.email == email).first()
        if orm_obj:
            self.db.delete(orm_obj)
            self.db.commit()
