from product_csr.models import Product

class ProductRepository:

    def create(self, data):
        product = Product(**data)
        product.save()
        return product.to_dict()

    def get_all(self):
        return [product.to_dict() for product in Product.objects()]