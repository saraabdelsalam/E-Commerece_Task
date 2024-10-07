from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .User import User
from .Product import Product
from .Order import Order
from .OrderItem import OrderItem
