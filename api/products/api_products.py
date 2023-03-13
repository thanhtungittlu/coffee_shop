from flask_restful import Resource


class Product(Resource):
    
    def get(self, product_id):
        
        return {"Messege get": product_id}
    
    def put(self, product_id):
        return {'message put': product_id}

    def delete(self, product_id):
        return {'message delete': product_id}

class ProductList(Resource):
    def get(self):
        return {'message': 'Product Get list successfully'}
    def post(self):
        return {'message': 'Product added successfully'}


