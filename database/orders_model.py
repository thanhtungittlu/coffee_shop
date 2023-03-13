from peewee import *
from .base_model import BaseModel
from .product_model import PRODUCTS
from .customer_model import CUSTOMERS


class ORDERS(BaseModel):
    id              = IntegerField(db_column='id', primary_key= True)
    product_id      = ForeignKeyField(PRODUCTS, db_column='product_id', backref='orders')
    customer_id     = ForeignKeyField(CUSTOMERS, db_column='customer_id', backref='orders')
    order_time      = DateTimeField (db_column='order_time')

    class Meta:
        db_table = 'orders'