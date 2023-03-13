from flask_restful import Resource
from database.product_model import PRODUCTS
from flask import jsonify, request
from playhouse.shortcuts import model_to_dict


class Product(Resource):
    
    def get(self, product_id):
        product = PRODUCTS.get(PRODUCTS.id == product_id)  
        return jsonify({'data': model_to_dict(product)})
    
    
    def put(self, product_id):
        data = request.get_json()
        product = PRODUCTS.get(PRODUCTS.id == product_id)
        product.name = data['name']
        product.price = data['price']
        product.coffee_origin = data['coffee_origin']
        product.save()
        return jsonify({'message': "Product update successfully", 'data': model_to_dict(product)})

    def delete(self, product_id):
        product = PRODUCTS.get(PRODUCTS.id == product_id)
        product.delete_instance()
        return jsonify({'message': 'Product has been deleted'})
        

class ProductList(Resource):
    def get(self):
        list_product = PRODUCTS.select()
        dataDict = list(list_product.dicts())    
        return jsonify({'data': dataDict})
    
    def post(self):
        data = request.get_json()
        product = PRODUCTS.create(name=data['name'], price=data['price'], coffee_origin=data['coffee_origin'])
        return jsonify({'message': "Product added successfully", 'data': model_to_dict(product)})
        


