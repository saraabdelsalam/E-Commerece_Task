from werkzeug.security import generate_password_hash
from Repository.UserRepository import add_user, get_user_by_email
from Models import User
from Models.Enums import UserRole

def register_user(user_data):
    if get_user_by_email(user_data['email']):
        raise Exception("User already exists")

    # Get the role from the request, default to 'user' if not provided
    userRole = UserRole.get_user_role(user_data)
    

    # Hash the password
    user_data['password'] = generate_password_hash(user_data['password'])
    
    # Create the new User with the integer value of the role enum
    new_user = User(
        first_name=user_data['first_name'],
        last_name=user_data['last_name'],
        email=user_data['email'],
        phone_number=user_data['phone_number'],
        password=user_data['password'],
        role=userRole # Store the integer value of the Enum in the database
    )
    
    add_user(new_user)
    return new_user
