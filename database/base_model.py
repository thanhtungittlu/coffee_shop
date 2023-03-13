from peewee import *
from .connect_mysql import my_db

class BaseModel(Model):
    class Meta:
        database = my_db