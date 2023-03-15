from flask_restful import Resource
from database.orders_model import ORDERS
from database.product_model import PRODUCTS
from database.customer_model import CUSTOMERS

from redis_db.connect_redis import r
from config import config
from kafka_object.producer import producer
from loguru import logger
import json

class Orders(Resource):
    
    def get(self, order_id):
        
        return {"Messege get": order_id}
    
    def put(self, order_id):
        return {'message put': order_id}

    def delete(self, order_id):
        return {'message delete': order_id}

class OrdersList(Resource):
    def get(self):
        list_orders = r.get('list_orders')
        if list_orders:
            logger.info("Load from redis")
            return json.loads(list_orders)
        else:
            logger.info("Load from database")

            orders = (ORDERS.select(ORDERS.id, CUSTOMERS.first_name, CUSTOMERS.last_name, PRODUCTS.name.alias("product_name"))
                .join(PRODUCTS , on = (ORDERS.product_id == PRODUCTS.id))
                .join(CUSTOMERS, on = (ORDERS.customer_id == CUSTOMERS.id)))
            dataDict = list(orders.dicts()) 

            r.set('list_orders', json.dumps(dataDict), ex = 3600)           
            return dataDict
    def post(self):
        return {'message': 'Orders added successfully'}


