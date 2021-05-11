<<<<<<< HEAD
from src.models import User
=======
from src.models import User, Landmark, Note
>>>>>>> 27f80a3219ad8db5a640569273dea902084261b9
from src import db

db.drop_all()
db.create_all()
# Create some tests landmarks and reviews
db.session.add(User(username="Debug Admin", email="admin@ktlabpublishing.com", password="password", admin=True))
db.session.add(User(username="Debug Customer", email="customer@gmail.com", password="password", admin=False))
<<<<<<< HEAD

=======
db.session.add(Landmark(name="TEST Landmark", coverImage="default.bmp"))
db.session.add(Landmark(name="Landmark 1", coverImage="default.bmp"))
db.session.add(Landmark(name="Landmark 2", coverImage="default.bmp"))
db.session.add(Landmark(name="Landmark 3", coverImage="default.bmp"))
db.session.add(Landmark(name="Landmark 4", coverImage="default.bmp"))
db.session.add(Landmark(name="Landmark 5", coverImage="default.bmp"))
db.session.add(Landmark(name="Landmark 6", coverImage="default.bmp"))
db.session.add(Landmark(name="Landmark 7", coverImage="default.bmp"))
db.session.add(Landmark(name="Landmark 8", coverImage="default.bmp"))
db.session.add(Landmark(name="Landmark 9", coverImage="default.bmp"))
db.session.add(Note(reviewTitle="TEST Landmark", coverImage="default.bmp"))
db.session.add(Note(reviewTitle="Landmark 1", review="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", landmarkid="1"))
db.session.add(Note(reviewTitle="Landmark 2", review="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", landmarkid="2"))
db.session.add(Note(reviewTitle="Landmark 3", review="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", landmarkid="3"))
db.session.add(Note(reviewTitle="Landmark 4", review="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", landmarkid="4"))
db.session.add(Note(reviewTitle="Landmark 5", review="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", landmarkid="5"))
db.session.add(Note(reviewTitle="Landmark 6", review="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", landmarkid="6"))
db.session.add(Note(reviewTitle="Landmark 7", review="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", landmarkid="7"))
db.session.add(Note(reviewTitle="Landmark 8", review="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", landmarkid="8"))
db.session.add(Note(reviewTitle="Landmark 9", review="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", landmarkid="8"))
>>>>>>> 27f80a3219ad8db5a640569273dea902084261b9
db.session.commit()
