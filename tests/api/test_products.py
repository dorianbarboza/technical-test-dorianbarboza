# tests/api/test_products.py
import pytest
from fastapi import status
from tests.factories import create_product

def test_list_products(client, monkeypatch):
    fake_products = [create_product(), create_product(name="Another Product")]

    monkeypatch.setattr(
        "app.application.product_use_cases.ListProductsUseCase.execute",
        lambda self: fake_products
    )

    response = client.get("/products")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "Macbook Pro 14"

def test_create_product(client, monkeypatch):
    input_data = {
        "sku": "01ERTRFG",
        "name": "New Product",
        "brand": "Generic",
        "price": 200.0,
        "stock": 10
}

    fake_product = create_product(name="New Product", price=200.0)

    monkeypatch.setattr(
        "app.application.product_use_cases.CreateProductUseCase.execute",
        lambda self, data_dict, current_user: fake_product
    )

    response = client.post("/products", json=input_data)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["name"] == "New Product"
    assert data["price"] == 200.0
