from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId,json_util
from bson.errors import InvalidId
from config import connectionStringURL
import json
app = Flask(__name__)
client = MongoClient(connectionStringURL)

db = client['userdb']
users_collection = db['users']
@app.route('/status', methods=['GET'])
def check_connection():
    try:
        client.admin.command('ping')
        return jsonify({'message': 'MongoDB connected'}), 200
    except Exception as e:
        return jsonify({'message': 'MongoDB connection error', 'error': str(e)}), 500

@app.route('/users', methods=['GET'])
def get_all_users():
    try:
        users = list(users_collection.find())
        return json.loads(json_util.dumps(users)), 200
    except Exception as e:
        return jsonify({'message': 'Error occurred', 'error': str(e)}), 500

@app.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = users_collection.find_one({'_id': ObjectId(user_id)})
        if user:
            return json.loads(json_util.dumps(user)), 200
        return jsonify({'message': 'User not found'}), 404
    except InvalidId:
        return jsonify({'message': 'Invalid user ID'}), 400
    except Exception as e:
        return jsonify({'message': 'Error occurred', 'error': str(e)}), 500

@app.route('/users', methods=['POST'])
def create_user():
    try:
        user_data = request.json
        if not user_data:
            return jsonify({'message': 'Invalid request body'}), 400

        existing_user = users_collection.find_one({'id': user_data['id']})
        if existing_user:
            return jsonify({'message': 'User with the same id already exists'}), 409
    
        user_id = users_collection.insert_one(user_data).inserted_id

        return jsonify({'message': 'User created', 'user_id': str(user_id)}), 201
    except Exception as e:
        return jsonify({'message': 'Error occurred', 'error': str(e)}), 500


@app.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user_data = request.json
        result = users_collection.update_one({'_id': ObjectId(user_id)}, {'$set': user_data}) 
        if result.modified_count > 0:
            return jsonify({'message': 'User updated'}), 200
        return jsonify({'message': 'User not found'}), 404
    except InvalidId:
        return jsonify({'message': 'Invalid user ID'}), 400
    except Exception as e:
        return jsonify({'message': 'Error occurred', 'error': str(e)}), 500

@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        result = users_collection.delete_one({'_id': ObjectId(user_id)})
        if result.deleted_count > 0:
            return jsonify({'message': 'User deleted'}), 200
        return jsonify({'message': 'User not found'}), 404
    except InvalidId:
        return jsonify({'message': 'Invalid user ID'}), 400
    except Exception as e:
        return jsonify({'message': 'Error occurred', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run()






