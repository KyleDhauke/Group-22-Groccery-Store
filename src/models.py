from datetime import datetime
from src import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from src import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.Text, nullable=False)
    passwordHash = db.Column(db.String(128))
    password = db.Column(db.String(60), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    transactionid = db.Column(db.Integer, nullable = False, default=0)

    def get_id(self):
        return self.id

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute.")

    @password.setter
    def password(self, password):
        self.passwordHash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.passwordHash, password)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

# class Product(db.Model):
#     # Unique identifier of this product.
#     id = db.Column(db.Integer, primary_key=True, nullable=False)
#     # Whether this product is viewable and purchasable by customers or not.
#     active = db.Column(db.Boolean(), nullable=False)
#     # Name and description of this product.
#     name = db.Column(db.String(120), nullable=False)
#     desc = db.Column(db.String(1000), nullable=False)
#     # Path to a cover image for this product.
#     coverImage = db.Column(db.String(128), nullable=False)
#     # How many instances of this product are in stock.
#     totalStock = db.Column(db.Integer, nullable=False)
#     # The base price for this product, not including VAT or discounts.
#     basePrice = db.Column(db.Float, nullable=False)
#
#     def get_id(self):
#         return self.id
#
#     def __repr__(self):
#         return f"Product('{self.name}', '{self.desc}')"

# class Order(db.Model):
#     orderid = db.Column(db.Integer, primary_key=True, nullable=False)
#     userid = db.Column(db.Integer, nullable=False)
#     transactionid = db.Column(db.Integer, nullable=False)
#     productid = db.Column(db.Integer, nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)
#
#     def to_dict(self):
#         return {
#             'orderid'           : self.orderid,
#             'userid'            : self.userid,
#             'transactionid'     : str(self.transactionid),
#             'productid'         : str(self.productid),
#             'quantity'          : str(self.quantity)
#         }
#
#     def __repr__(self):
#         return f"Order('{self.orderid}', '{self.id}')"