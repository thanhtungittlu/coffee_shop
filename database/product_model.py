from peewee import *
from .base_model import BaseModel

class PRODUCTS(BaseModel):
    id             = IntegerField(db_column='id', primary_key= True)
    name           = CharField(db_column='name')
    price          = DecimalField(db_column='price')
    coffee_origin  = CharField(db_column='coffee_origin')

    class Meta:
        db_table = 'products'