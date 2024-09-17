# services.py

from .database import Session
from .models import Product, Category, Supplier

def add_product(name, quantity, category_name, supplier_name):
    session = Session()
    category = session.query(Category).filter_by(name=category_name).first()
    supplier = session.query(Supplier).filter_by(name=supplier_name).first()

    product = Product(name=name, quantity=quantity, category=category, supplier=supplier)
    session.add(product)
    session.commit()
    session.close()

def list_products():
    session = Session()
    products = session.query(Product).all()
    session.close()
    return products