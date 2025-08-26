# domain/repositories.py
from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.product import Product


class IProductRepository(ABC):

    @abstractmethod
    def add(self, product: Product) -> Product:
        """Agrega un producto nuevo"""
        pass

    @abstractmethod
    def get_by_sku(self, sku: str) -> Optional[Product]:
        """Obtiene un producto por SKU"""
        pass

    @abstractmethod
    def list_all(self) -> List[Product]:
        """Lista todos los productos"""
        pass

    @abstractmethod
    def update(self, product: Product) -> Product:
        """Actualiza un producto existente"""
        pass

    @abstractmethod
    def delete(self, sku: str) -> None:
        """Elimina un producto por SKU"""
        pass


