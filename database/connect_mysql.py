from peewee import *
from config import config

# Connect to a MySQL database on network.
my_db = MySQLDatabase(
    database = config.DATABASE,
    user= config.USER_DATABASE, 
    password= config.PASSWORD_DATABASE,
    host= config.SERVER_DATABASE, 
    port= int(config.PORT_DATABASE), 
)




