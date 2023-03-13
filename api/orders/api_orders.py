from flask_restful import Resource


class Orders(Resource):
    
    def get(self, order_id):
        
        return {"Messege get": order_id}
    
    def put(self, order_id):
        return {'message put': order_id}

    def delete(self, order_id):
        return {'message delete': order_id}

class OrdersList(Resource):
    def get(self):
        return {'message': 'Orders Get list successfully'}
    def post(self):
        return {'message': 'Orders added successfully'}


