from flask import Blueprint
from api.orders.api_orders import Orders, OrdersList
from flask_restful import Api


orders_bp = Blueprint('orders', __name__)
api = Api(orders_bp)

api.add_resource(OrdersList, '/orders')
api.add_resource(Orders, '/order/<int:order_id>')\
