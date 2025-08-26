# scripts/create_first_admin.py
from app.infrastructure.database import get_db
from app.infrastructure.repositories.postgresql_user_repository import PostgresUserRepository
from app.domain.services.user_service import UserService, AuthService
from app.application.user_use_cases import CreateUserUseCase
from app.domain.entities.user import User
from app.core.config import EMAIL_ADMIN, EMAIL_ADMIN_PWD

def create_first_admin():
    db = next(get_db())  
    user_repo = PostgresUserRepository(db)
    auth_service = AuthService()
    user_service = UserService(user_repo, auth_service)
    use_case = CreateUserUseCase(user_service)

    admin_data = {
        "email": EMAIL_ADMIN[0],
        "password": EMAIL_ADMIN_PWD,
        "is_admin": True
    }

    existing_admin = user_repo.get_by_email(admin_data["email"])
    if existing_admin:
        print(f"Admin {admin_data['email']} exists.")
        return existing_admin

    try:
        admin_user = use_case.execute(admin_data, current_user=None) 
        print(f"Admin create: {admin_user.email}")
        return admin_user
    except Exception as e:
        print(f"Error create admin: {e}")