class Product:
    
    def __init__(self, sku: str, name: str, price: float, brand: str, stock: int, views: int = 0):
        self.sku = sku
        self.name = name
        self.price = price
        self.brand = brand
        self.views = views
        self.stock = stock

    def increment_views(self):
        """Incrementa el contador de consultas por usuarios anónimos"""
        self.views += 1

    def update(self, name: str = None, price: float = None, brand: str = None, stock: int = None):
        """Actualiza los campos del producto de manera controlada"""
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if brand is not None:
            self.brand = brand
        if stock is not None:
            self.stock = stock
