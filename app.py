from flask import Flask


app = Flask(__name__)




from api.products.route_products import products_bp
app.register_blueprint(products_bp)


from api.customers.route_customers import customers_bp
app.register_blueprint(customers_bp)

from api.orders.route_orders import orders_bp
app.register_blueprint(orders_bp)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)