from mongoengine import connect
import os

connect(
    db="product_db",
    username=os.getenv("MONGO_USER", "root"),
    password=os.getenv("MONGO_PASS", "example"),
    host=os.getenv("MONGO_HOST", "localhost"),
    port=int(os.getenv("MONGO_PORT", 27019)),
    authentication_source="admin"
)