from Models.User import User
from Models import db

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def add_user(user):
    db.session.add(user)
    db.session.commit()
