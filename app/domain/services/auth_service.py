# app/domain/services/auth_service.py
from datetime import datetime, timedelta
from jose import jwt, JWTError

from app.domain.entities.user import User
from app.core.config import (
    SECRET_KEY,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM
)

class AuthService:

    
    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    

    def decode_access_token(self, token: str) -> User:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email: str = payload.get("sub")
            if email is None:
                return None
            return User(email=email, hashed_password="",is_admin=True)  # TODO: issue hashed_password
        except JWTError:
            return None
