# infrastructure/models.py
from sqlalchemy import Column, String, Float, Integer, Boolean
from app.infrastructure.database import Base

class ProductORM(Base):
    __tablename__ = "products"
    sku = Column(String, primary_key=True, unique=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    brand = Column(String, nullable=False)
    views = Column(Integer, default=0)
    stock = Column(Integer, default=0)

    def to_dict(self):
        return {
            "sku": self.sku,
            "name": self.name,
            "price": self.price,
            "brand": self.brand,
            "views": self.views,
            "stock": self.stock
        }


class UserORM(Base):
    __tablename__ = "users"
    email = Column(String(255), primary_key=True,unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)


    def to_dict(self):
        return {
            "email": self.email,
            "hashed_password": self.hashed_password,
            "is_admin": self.is_admin
        }
