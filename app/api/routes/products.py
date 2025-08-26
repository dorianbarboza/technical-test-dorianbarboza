
# api/routes/products.py

from typing import List
from fastapi import APIRouter, Depends

from app.application.product_use_cases import (
    ListProductsUseCase, 
    CreateProductUseCase, 
    UpdateProductUseCase, 
    DeleteProductUseCase
    )
from app.domain.services.product_service import ProductService
from app.domain.services.user_service import UserService
from app.infrastructure.repositories.postgresql_product_repository import PostgresProductRepository
from app.infrastructure.repositories.postgresql_user_repository import PostgresUserRepository
from app.infrastructure.database import get_db
from app.api.dependencies import get_current_user
from app.api.schemas import ProductCreate, ProductUpdate, ProductOut


router = APIRouter(prefix="/products", tags=["products"])


@router.get("", response_model=List[ProductOut])
def list_products(
    # current_user=Depends(get_current_user), 
    db = Depends(get_db)
    ):
    product_service = ProductService(
        product_repo=PostgresProductRepository(db),
        user_repo=PostgresUserRepository(db)
    )
    use_case = ListProductsUseCase(product_service)
    return use_case.execute()


@router.post("", response_model=ProductOut)
def create_product(
    data: ProductCreate, 
    current_user=Depends(get_current_user),
    db=Depends(get_db)
    ):
    product_service = ProductService(
        product_repo=PostgresProductRepository(db),
        user_repo=PostgresUserRepository(db)
    )
    use_case = CreateProductUseCase(product_service)
    return use_case.execute(data.dict(), current_user)


@router.put("", response_model=ProductOut)
def update_product(
    sku: str,
    product_data: ProductUpdate, 
    current_user=Depends(get_current_user),
    db=Depends(get_db)
    ):
    product_service = ProductService(
        product_repo=PostgresProductRepository(db),
        user_repo=PostgresUserRepository(db)
    )
    use_case = UpdateProductUseCase(product_service)
    return use_case.execute(sku, product_data.dict(), current_user)


@router.delete("/{sku}", status_code=204)
def delete_product(
    sku: str,
    current_user=Depends(get_current_user),
    db=Depends(get_db)
):
    product_service = ProductService(
        product_repo=PostgresProductRepository(db),
        user_repo=PostgresUserRepository(db)
    )
    use_case = DeleteProductUseCase(product_service)
    use_case.execute(sku, current_user)
    return 