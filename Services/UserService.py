from werkzeug.security import generate_password_hash
from Repository.UserRepository import add_user, get_user_by_email
from Models import User
from Models.Enums import UserRole
import re

def validate_user_data(user_data):
  
    if 'email' not in user_data or not is_valid_email(user_data['email']):
        raise ValueError("Invalid email format. Email should contain '@' and a valid domain.")
    
    if 'phone_number' not in user_data or len(user_data['phone_number']) != 11 or not user_data['phone_number'].isdigit():
        raise ValueError("Invalid phone number. It should be a 11 digits and contain only numbers.")
    
    if 'first_name' not in user_data or len(user_data['first_name']) < 3:
        raise ValueError("First name must be at least 2 characters long.")
    
    if 'last_name' not in user_data or len(user_data['last_name']) < 3:
        raise ValueError("Last name must be at least 2 characters long.")
    
    if 'password' not in user_data or len(user_data['password']) < 6 and len(user_data['password']) > 12:
        raise ValueError("Password length must be at between 6 to 12 characters long.")

def is_valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

def register_user(user_data):
    if get_user_by_email(user_data['email']):
        raise Exception("User already exists")

    userRole = UserRole.get_user_role(user_data)
    
    user_data['password'] = generate_password_hash(user_data['password'])
    
    new_user = User(
        first_name=user_data['first_name'],
        last_name=user_data['last_name'],
        email=user_data['email'],
        phone_number=user_data['phone_number'],
        password=user_data['password'],
        role=userRole
    )
    
    add_user(new_user)
    return new_user
