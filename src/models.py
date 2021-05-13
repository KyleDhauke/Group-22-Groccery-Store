from datetime import datetime
from src import login_manager,app,db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

from src import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.Text, nullable=False)
    passwordHash = db.Column(db.String(128))
    password = db.Column(db.String(60), nullable=False)
    confirmed = db.Column(db.Boolean, default=False)

    def get_id(self):
        return self.id

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id}).decode('utf-8')

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = 1
        db.session.add(self)
        return True

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


class Landmark(db.Model):
     # Unique identifier of this landmark.
     landmarkid = db.Column(db.Integer, primary_key=True, nullable=False)
     # Name of the landmark.
     name = db.Column(db.String(120), nullable=False)
     # Description for this landmark.
     description = db.Column(db.String(128), nullable=False)
     # Tags for this landmark.
     tags = db.Column(db.String(255))
     lat = db.Column(db.Integer())
     lng = db.Column(db.Integer())
     userid = db.Column(db.Integer())


     def get_id(self):
         return self.landmarkid

     def __repr__(self):
         return f"Landmark('{self.name}', '{self.description}')"

class List(db.Model):
    # Unique identifier of this list.
    listid = db.Column('listid',db.Integer, primary_key=True)
    # Name of the list.
    name = db.Column(db.String(120), nullable=False)
    userid = db.Column(db.Integer,nullable=False)

# lists_landmarks = db.Table('lists_landmarks',
#                            db.Column('listid',db.Integer,db.ForeignKey('lists.listid'),primary_key=True),
#                            db.Column('landmarkid',db.Integer, db.ForeignKey('landmarks.landmarkid'),primary_key=True)
#                            )

class lists_landmarks(db.Model):
    listid = db.Column('listid',db.Integer,db.ForeignKey('lists.listid'),primary_key=True)
    landmarkid = db.Column('landmarkid',db.Integer, db.ForeignKey('landmarks.landmarkid'),primary_key=True)

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    userid = db.Column(db.Integer, nullable=False)
    reviewTitle = db.Column(db.String(120), nullable=False)
    review = db.Column(db.String(1024), nullable=False)
    landmarkid = db.Column(db.Integer,  nullable=False)
    def to_dict(self):
         return {
             'noteid'           : self.orderid,
             'userid'           : self.userid,
             'review'           : str(self.review),
         }

    def __repr__(self):
         return f"Note('{self.noteid}', '{self.userid}')"
