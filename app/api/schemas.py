# schemas.py
from typing import Optional
from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserCreate(BaseModel):
    email: EmailStr
    password: str  
    is_admin: bool = False

class UserUpdate(BaseModel):
    is_admin: Optional[bool] = None

class UserOut(BaseModel):
    email: EmailStr
    is_admin: bool

class ProductCreate(BaseModel):
    sku: str
    name: str
    brand: str
    price: float
    stock: int

class ProductUpdate(BaseModel):
    name: str
    brand: str
    price: float
    stock: int

class ProductOut(BaseModel):
    sku: str
    name: str
    brand: str
    price: float
    stock: int