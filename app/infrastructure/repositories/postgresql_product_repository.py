# infrastructure/repositories/product_repository_pg.py
from sqlalchemy.orm import Session
from app.domain.entities.product import Product
from app.domain.repositories.product_repository import IProductRepository
from app.infrastructure.models import ProductORM

class PostgresProductRepository(IProductRepository):
    def __init__(self, db: Session):
        self.db = db

    def add(self, product: Product) -> Product:
        orm_obj = ProductORM(**product.__dict__)
        self.db.add(orm_obj)
        self.db.commit()
        self.db.refresh(orm_obj)
        return Product(**orm_obj.to_dict())

    def get_by_sku(self, sku: str) -> Product:
        orm_obj = self.db.query(ProductORM).filter(ProductORM.sku == sku).first()
        return Product(**orm_obj.to_dict()) if orm_obj else None

    def list_all(self) -> list[Product]:
        orm_objs = self.db.query(ProductORM).all()
        return [Product(**o.to_dict()) for o in orm_objs]

    def update(self, product: Product) -> Product:
        orm_obj = self.db.query(ProductORM).filter(ProductORM.sku == product.sku).first()
        if not orm_obj:
            raise ValueError("Product not found")
        for attr, value in product.__dict__.items():
            setattr(orm_obj, attr, value)
        self.db.commit()
        self.db.refresh(orm_obj)
        return Product(**orm_obj.to_dict())

    def delete(self, sku: str) -> None:
        orm_obj = self.db.query(ProductORM).filter(ProductORM.sku == sku).first()
        if orm_obj:
            self.db.delete(orm_obj)
            self.db.commit()
