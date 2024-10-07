from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement =True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)  # Hashed password
    role = db.Column(db.Integer, nullable=False)  # 0: visitor, 1: user, 2: admin

    orders = db.relationship('Order', backref='user', lazy=True)
