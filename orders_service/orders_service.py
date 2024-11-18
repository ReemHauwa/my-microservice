from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

orders = {
    1: {"user_id": 1, "product": "Laptop", "price": 999},
    2: {"user_id": 2, "product": "Phone", "price": 599},
    3: {"user_id": 3, "product": "Tablet", "price": 599}
}

USERS_SERVICE_URL = 'http://users-service:5001'

# Get all orders
@app.route('/orders', methods=['GET'])
def get_all_orders():
    complete_orders = []
    for order_id, order in orders.items():
        try:
            user_response = requests.get(f'{USERS_SERVICE_URL}/users/{order["user_id"]}')
            user_data = user_response.json()
            complete_orders.append({
                "order_id": order_id,
                **order,
                "customer": user_data
            })
        except requests.RequestException as e:
            complete_orders.append({
                "order_id": order_id,
                **order,
                "customer": f"Error: Could not fetch user data - {str(e)}"
            })
    return jsonify(complete_orders)

# Get single order
@app.route('/orders/<int:order_id>')
def get_order(order_id):
    order = orders.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    
    try:
        user_response = requests.get(f'{USERS_SERVICE_URL}/users/{order["user_id"]}')
        user_data = user_response.json()
        return jsonify({
            "order_id": order_id,
            **order,
            "customer": user_data
        })
    except requests.RequestException as e:
        return jsonify({
            "order_id": order_id,
            **order,
            "customer": f"Error: Could not fetch user data - {str(e)}"
        })

if __name__ == '__main__':
    app.run(host=os.getenv('SERVICE_HOST', '0.0.0.0'), port=5002)