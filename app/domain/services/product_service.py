# services/product_service.py
from typing import List

from app.domain.entities.product import Product
from app.domain.entities.user import User
from app.domain.repositories.product_repository import IProductRepository
from app.domain.repositories.user_repository import IUserRepository
from app.utils.notifications import notify_admins  
from app.core.config import EMAIL_ADMIN



class ProductService:
    def __init__(self, product_repo: IProductRepository, user_repo: IUserRepository):
        self.product_repo = product_repo
        self.user_repo = user_repo

    def list_products(self) -> List[Product]:
        products = self.product_repo.list_all()
        # if not current_user.is_admin:
            # incremento de vistas para usuarios anónimos
        for p in products:
            p.increment_views()
            self.product_repo.update(p)
        return products

    def create_product(self, product: Product, current_user: User) -> Product:
        if not current_user.is_admin:
            raise PermissionError("Only admins can create products")
        created = self.product_repo.add(product)
        # notificar a otros admins
        admins = self.user_repo.list_admins()
        for admin in admins:
            if admin.email != current_user.email:
                notify_admins(admin.email, f"Producto creado: {product.sku}")
        return created

    def update_product(self, sku: str, data: dict, current_user: User) -> Product:
        if not current_user.is_admin:
            raise PermissionError("Only admins can update products")
        product = self.product_repo.get_by_sku(sku)
        if not product:
            raise ValueError("Product not found")
        product.update(**data)
        updated = self.product_repo.update(product)
     
        admins = self.user_repo.list_admins()
        emails_tuple = list(map(lambda admin: admin.email, admins))
        
        message_text = f"Producto actualizado: {sku}"
        try:
            
        # Notf admin changes
        # TODO: all admin notification emails are limited to: dorianbarbozazebrands@gmail.com, 
        # This limitation is only for the sandbox environment.
        # In a production SES environment, emails could be sent to any address without restriction.

            for admin in admins:
                if admin.email != current_user.email:
                    print(1)
                    notify_admins(emails_tuple, message_text)
        except Exception as e:
            print("")

        notify_admins(EMAIL_ADMIN, message_text)
               
        return updated

    def delete_product(self, sku: str, current_user: User):
        if not current_user.is_admin:
            raise PermissionError("Only admins can delete products")
        self.product_repo.delete(sku)
