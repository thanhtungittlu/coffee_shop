from flask_restful import Resource
from database.product_model import PRODUCTS
from flask import jsonify, request
from playhouse.shortcuts import model_to_dict
from redis_db.connect_redis import r
from config import config
from kafka_object.producer import producer

class Product(Resource):
    
    def get(self, product_id):
        product_querry = PRODUCTS.get(PRODUCTS.id == product_id) 
        product = model_to_dict(product_querry)

        # Lưu thông tin vào Redis
        r.set(f"product_{product_id}", str(product))
        
        
        # # Gửi thông tin vào topic kafka
        producer.send(
            config.TOPIC_KAFKA, r.get(f"product_{product_id}")
        )


        return jsonify({'data': product})
    
    
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
        


