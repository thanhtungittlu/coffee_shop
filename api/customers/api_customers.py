from flask_restful import Resource


class Customers(Resource):
    
    def get(self, customer_id):
        
        return {"Messege get": customer_id}
    
    def put(self, customer_id):
        return {'message put': customer_id}

    def delete(self, customer_id):
        return {'message delete': customer_id}

class CustomersList(Resource):
    def get(self):
        return {'message': 'Customers Get list successfully'}
    def post(self):
        return {'message': 'Customers added successfully'}


