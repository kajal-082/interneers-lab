from mongoengine import (
    Document,
    StringField,
    FloatField,
    IntField,
    DateTimeField
)
from datetime import datetime

class Product(Document):
    name = StringField(required=True)
    category = StringField()
    brand = StringField()
    price = FloatField()
    quantity = IntField()

    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        "collection": "products"
    }

    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super().save(*args, **kwargs)

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "category": self.category,
            "brand": self.brand,
            "price": self.price,
            "quantity": self.quantity,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
