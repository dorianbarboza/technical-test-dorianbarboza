# tests/factories.py
from app.api.schemas import UserOut
from app.api.schemas import ProductOut

def create_user(email="admin@test.com", is_admin=True):
    return UserOut(
        email=email,
        is_admin=is_admin
    )


def create_product(sku="01ERTRFG",name="Macbook Pro 14",brand="Apple", price=35000.0,stock=10):
    return ProductOut(
        sku=sku,
        name=name,
        brand=brand,
        price=price,
        stock=stock
    )