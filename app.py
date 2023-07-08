from flask import Flask
from flask_restful import Api, Resource, reqparse
from pymongo import MongoClient
from config import connectionStringURL
from bson import ObjectId

app = Flask(__name__)
api = Api(app)
client = MongoClient(connectionStringURL)
db = client['mydatabase']
users_collection = db['users']


class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

    @staticmethod
    def from_dict(user_dict):
        return User(
            id=user_dict['id'],
            name=user_dict['name'],
            email=user_dict['email'],
            password=user_dict['password']
        )

class UserListResource(Resource):
    def get(self):
        users = [User.from_dict(user_data).to_dict() for user_data in users_collection.find()]
        return users
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='Name field is required.')
        parser.add_argument('name', type=str, required=True, help='Name field is required.')
        parser.add_argument('email', type=str, required=True, help='Email field is required.')
        parser.add_argument('password', type=str, required=True, help='Password field is required.')
        args = parser.parse_args()
        new_user = User( args['id'],args['name'], args['email'], args['password'])
        print(new_user)
        existing_user = users_collection.find_one({'id': str(new_user.id)})
        if existing_user:
            return {'message': 'User with the same id already exists'}, 409
        user_id = users_collection.insert_one(new_user.to_dict())
        print(new_user.name)
        print(user_id)
        return new_user.to_dict(), 201  


class UserResource(Resource):
    def get(self, user_id):
        user_data = users_collection.find_one({'id': str(user_id)})
        if user_data:
            return User.from_dict(user_data).to_dict()
        else:
            return {'error': 'User not found'}, 404



    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()

        update_fields = {field: value for field, value in args.items() if value is not None}

        result = users_collection.update_one({'id': str(user_id)}, {'$set': update_fields})
        if result.matched_count == 1:
            return {'message': 'User updated successfully'}
        else:
            return {'error': 'User not found'}, 404

    def delete(self, user_id):
        result = users_collection.delete_one({'id': str(user_id)})
        if result.deleted_count == 1:
            return {'message': 'User deleted successfully'}
        else:
            return {'error': 'User not found'}, 404


class ConnectionCheckResource(Resource):
    def get(self):
        connected = client.admin.command('ping')['ok']
        if connected:
            return {'message': 'Connected to MongoDB'}
        else:
            return {'message': 'Unable to connect to MongoDB'}


api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<string:user_id>')
api.add_resource(ConnectionCheckResource, '/connection-check')

if __name__ == '__main__':
    app.run(debug=True)
