from flask import Blueprint, request, jsonify
from Services.UserService import register_user, validate_user_data
from Services.AuthService import login_user
from flask_jwt_extended import jwt_required, get_jwt_identity, get_current_user

bp = Blueprint('api', __name__)

@bp.route('/register', methods=['POST'])
def register():
    try:
        user_data = request.json
        validate_user_data(user_data)
        register_user(user_data)
        return jsonify({"message": "User registered successfully."}), 201
    except ValueError as e:  # Catch validation errors
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500  # Internal server error for other exceptions


@bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    
    try:
        token = login_user(email, password)
        return jsonify(access_token=token), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 401

@bp.route('/systemAdmin', methods=['GET'])
@jwt_required()
def admin_only_page():
    current_user = get_jwt_identity()
    if current_user['role'] != 2: 
        return jsonify({"message": "Access forbidden: Admins only."}), 403
    return jsonify({"message": f"Hello {current_user['userName']}, welcome to the admin page!"})

@bp.route('/users', methods=['GET'])
@jwt_required()
def users_page():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Hello {current_user['userName']}, welcome to our website!"})


@bp.route('/visitors', methods=['GET'])
def visitors_page():
    return jsonify({"message": "Hello Visitor, welcome to our website!"})