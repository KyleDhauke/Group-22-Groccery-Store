from src.models import User
from src import db

db.drop_all()
db.create_all()
# Create a couple of test accounts
db.session.add(User(username="Debug Admin", email="admin@ktlabpublishing.com", password="password", admin=True))
db.session.add(User(username="Debug Customer", email="customer@gmail.com", password="password", admin=False))

db.session.commit()
