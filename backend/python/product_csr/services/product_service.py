from product_csr.repositories.product_repository import ProductRepository

class ProductService:

    def __init__(self):
        self.repo = ProductRepository()

    def create_product(self, data):
        required_fields = ["name", "price", "category", "brand", "quantity"]

        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} is required")

        if data["price"] <= 0:
            raise ValueError("Price must be positive")

        return self.repo.create(data)

    def get_all_products(self):
        return self.repo.get_all()