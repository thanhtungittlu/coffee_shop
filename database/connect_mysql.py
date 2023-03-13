from peewee import *

# Connect to a MySQL database on network.
my_db = MySQLDatabase(
    database = "coffee_store",
    user='root', 
    password='01032023',
    host='127.0.0.1', 
    port=3306, 
)




