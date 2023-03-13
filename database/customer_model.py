from peewee import *
from .base_model import BaseModel

class CUSTOMERS(BaseModel):
    id             = IntegerField(db_column='id', primary_key= True)
    first_name     = TextField(db_column='first_name')
    last_name      = TextField(db_column='last_name')
    gender         = CharField(db_column='gender')
    phone_number   = CharField(db_column='phone_number')

    class Meta:
        db_table = 'customers'