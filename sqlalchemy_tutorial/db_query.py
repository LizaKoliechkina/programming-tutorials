import sqlalchemy as sa

from connect_db import Product, connection


def insert_record(index, name, price, desc):
    insert_value = sa.insert(Product).values(
        index=index, name=name, price=price, description=desc
    )
    connection.execute(insert_value)


def insert_multiple_records():
    pass


def retrieve_data():
    select_products = sa.select(Product)
    products = connection.execute(select_products)
    return products.all()


def update_product_price(prod_id: int, new_price: float):
    update_query = sa.update(Product).values(price=new_price).where(Product.index == prod_id)
    connection.execute(update_query)
