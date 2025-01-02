from flask import Blueprint, jsonify, request
from controller.validator.user_validator import UserValidator
from services.user_service import UserService

user = Blueprint('user', __name__)
user_service = UserService()

@user.route('', methods=['GET'])
def get_user():
    users = user_service.get_all_users()
    print (users)
    return jsonify([user for user in user_service.get_all_users()])

@user.route('/<string:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    try:
        user = user_service.get_user(user_id)
        return jsonify(user)
    except ValueError as e:
        return jsonify({'message': str(e)}), 404

@user.route('', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    rank = data.get('rank')
    try:
        UserValidator.validate_create_user_data(name, email, password, rank)
        user = user_service.create_user(name, email, password, rank)
        return jsonify({'message': 'User created successfully', 'user': user}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@user.route('/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    rank = data.get('rank')
    try:
        UserValidator.validate_update_user_data(name, email, password, rank)
        user = user_service.update_user(user_id, name, email, password, rank)
        return jsonify({'message': 'User updated successfully', 'user': user})
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@user.route('/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user_service.delete_user(user_id)
        return jsonify({'message': f'User with ID {user_id} deleted successfully'})
    except ValueError as e:
        return jsonify({'message': str(e)}), 404
