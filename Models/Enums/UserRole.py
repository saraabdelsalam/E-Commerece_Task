from enum import Enum

class UserRole(Enum): 
    user = 1
    admin = 2

def get_user_role(user_data):
    role_str = user_data.get('role', 'user').lower() 
    try:
        role_enum = UserRole[role_str]
        return role_enum.value 
    except KeyError:
        raise ValueError("Invalid role provided")
