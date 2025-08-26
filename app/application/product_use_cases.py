# application/product_use_cases.py
from typing import List

from app.domain.entities.product import Product
from app.domain.entities.user import User
from app.domain.services.product_service import ProductService


class ListProductsUseCase:
    def __init__(self, product_service: ProductService):
        self.product_service = product_service

    def execute(self) -> List[Product]:
        return self.product_service.list_products()


class CreateProductUseCase:
    def __init__(self, product_service: ProductService):
        self.product_service = product_service

    def execute(self, product_data: dict, current_user: User) -> Product:
        product = Product(**product_data)
        return self.product_service.create_product(product, current_user)


class UpdateProductUseCase:
    def __init__(self, product_service: ProductService):
        self.product_service = product_service

    def execute(self, sku: str, update_data: dict, current_user: User) -> Product:
        return self.product_service.update_product(sku, update_data, current_user)


class DeleteProductUseCase:
    def __init__(self, product_service: ProductService):
        self.product_service = product_service

    def execute(self, sku: str, current_user: User):
        self.product_service.delete_product(sku, current_user)
