from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

users = {
    1: {"name": "Tom Arda", "email": "tom@sample.com"},
    2: {"name": "Kili Berry", "email": "kili@sample.com"},
    3: {"name": "Taury Wood", "email": "taury@sample.com"},
}

# Get all users
@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(list(users.values()))

# Get single user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host=os.getenv('SERVICE_HOST', '0.0.0.0'), port=5001)