from flask import Blueprint
from api.products.api_products import Product, ProductList
from flask_restful import Api


products_bp = Blueprint('products', __name__)
api = Api(products_bp)

api.add_resource(ProductList, '/products')
api.add_resource(Product, '/product/<int:product_id>')\
