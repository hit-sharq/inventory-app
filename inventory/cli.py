# cli.py

import click
from .database import init_db
from .services import add_product, list_products

@click.group()
def cli():
    pass

@cli.command()
def init():
    """Initialize the database."""
    init_db()
    click.echo("Database initialized.")

@cli.command()
@click.argument('name')
@click.argument('quantity', type=int)
@click.argument('category')
@click.argument('supplier')
def add(name, quantity, category, supplier):
    """Add a product to the inventory."""
    add_product(name, quantity, category, supplier)
    click.echo(f"Added product: {name}")

@cli.command()
def list():
    """List all products in inventory."""
    products = list_products()
    for product in products:
        click.echo(f'Product: {product.name}, Quantity: {product.quantity}')

if __name__ == '__main__':
    cli()