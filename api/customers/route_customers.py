from flask import Blueprint
from api.customers.api_customers import Customers, CustomersList
from flask_restful import Api


customers_bp = Blueprint('customers', __name__)
api = Api(customers_bp)

api.add_resource(CustomersList, '/customers')
api.add_resource(Customers, '/customer/<int:customer_id>')\
