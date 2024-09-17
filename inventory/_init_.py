# inventory/__init__.py
from .models import Product, Category, Supplier
from .database import init_db
from .services import add_product, list_products

__all__ = ["Product", "Category", "Supplier", "init_db", "add_product", "list_products"]