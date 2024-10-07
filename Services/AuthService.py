from flask_jwt_extended import create_access_token
from Repository.UserRepository import get_user_by_email
from werkzeug.security import check_password_hash

def login_user(email, password):
    user = get_user_by_email(email)
    if user and check_password_hash(user.password, password):
        return create_access_token(identity={"email": user.email, "role": user.role})
    raise Exception("Invalid credentials")
