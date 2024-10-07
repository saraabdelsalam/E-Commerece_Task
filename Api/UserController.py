from flask import Blueprint, request, jsonify
from Services.UserService import register_user
from Services.AuthService import login_user
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('api', __name__)

@bp.route('/register', methods=['POST'])
def register():
    try:
        user_data = request.json
        # Pass user data (including role) to the registration service
        register_user(user_data)
        return jsonify({"message": "User registered successfully."}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400


# @bp.route('/login', methods=['POST'])
# def login():
#     email = request.json.get('email')
#     password = request.json.get('password')
    
#     try:
#         token = login_user(email, password)
#         return jsonify(access_token=token), 200
#     except Exception as e:
#         return jsonify({"message": str(e)}), 401

# @bp.route('/admin_only_page', methods=['GET'])
# @jwt_required()
# def admin_only_page():
#     current_user = get_jwt_identity()
#     if current_user['role'] != 2:  # Check if user is admin
#         return jsonify({"message": "Access forbidden: Admins only."}), 403
#     return jsonify({"message": f"Hello {current_user['email']}, welcome to the admin page!"})
