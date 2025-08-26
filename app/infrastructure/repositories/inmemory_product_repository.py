# infrastructure/repositories/product_repository.py
from typing import List, Optional
from domain.entities import Product
from domain.repositories import IProductRepository

class InMemoryProductRepository(IProductRepository):
    def __init__(self):
        self._products = {}  # clave = sku, valor = Product

    def add(self, product: Product) -> Product:
        self._products[product.sku] = product
        return product

    def get_by_sku(self, sku: str) -> Optional[Product]:
        return self._products.get(sku)

    def list_all(self) -> List[Product]:
        return list(self._products.values())

    def update(self, product: Product) -> Product:
        if product.sku not in self._products:
            raise ValueError("Product not found")
        self._products[product.sku] = product
        return product

    def delete(self, sku: str) -> None:
        if sku in self._products:
            del self._products[sku]
