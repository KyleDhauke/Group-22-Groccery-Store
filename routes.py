from flask import Flask, redirect, render_template, url_for, flash, Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_folder="static")
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://c1919329:Runner1234@csmysql.cs.cf.ac.uk:3306/c1919329_Users'
app.config['SQLALCHEMY_BINDS'] = {'Items':'mysql+pymysql://c1919329:Runner1234@csmysql.cs.cf.ac.uk:3306/c1919329_Items'} #adds a secondary bind to allow queries on items
admin = Admin(app, name='Admin panel', template_mode='bootstrap3')

db = SQLAlchemy(app)
################################################### db model set up ##########################
class users(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    def __init__(self, username, name, email, password, is_admin):
        self.username = username
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute') #prevents anyone from reading passwords in plaintext in the database
    @password.setter
    def password(self, password): #creates a hash for the password for storing in the database
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password): #used for login
        return check_password_hash(self.password_hash, password)
class items(db.Model):
    _id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    image_dir = db.Column(db.String(100))
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)
    def __init__(self, name, description, image_dir, price, stock):
        self.name = name
        self.description = description
        self.image_dir = image_dir
        self.price = price
        self.stock = stock

admin.add_view(ModelView(users, db.session))
admin.add_view(ModelView(items, db.session))
########################################################### Routes determine individual web page behaviour ############################
@app.before_first_request
def before_first_request():
    session["basket"] = [] #clear basket when first page opens

@app.route('/')
@app.route("/home")
def home():
    dictlist = []
    items_in_database = items.query.all()
    if "basket" not in session:
        session["basket"] = []
    for item_val in items_in_database: #create a list of dictionaries containing details of the sale items
        item_details = {}
        item_details["name"] = item_val.name
        item_details["image_dir"] = item_val.image_dir
        item_details["price"] = item_val.price
        dictlist.append(item_details)
    return render_template('home.html', title = 'Home', dictlist = dictlist) #pass dictlist to be used in html

@app.route("/basket/<item_identifier>")
def basket(item_identifier):
    if "basket" not in session:
        session["basket"] = []
    if session["basket"] == [] and item_identifier == "None":
        flash("Basket empty")
        return redirect(url_for('home'))
    else:
        if item_identifier == "None":
            item_dict = {} #item_dict will contain the quantities of each item in the basket
            for item in session["basket"]: #work out quantities of items in basket
                if item in item_dict:
                    item_dict[item] += 1
                else:
                    item_dict[item] = 1
            total = 0
            for item in item_dict: #work out total cost of all items
                price_of_item = items.query.filter_by(name = item).first().price
                total = total + (price_of_item * item_dict[item])
            total = round(total, 2)
            return render_template('basket.html', title='Shopping Basket', basket = item_dict, total = total)
        else:
            val = session["basket"]
            val.append(item_identifier)
            session["basket"] = val
            item_dict = {}
            for item in session["basket"]:
                if item in item_dict:
                    item_dict[item] += 1
                else:
                    item_dict[item] = 1
            total = 0
            for item in item_dict: #work out total cost of all items
                price_of_item = items.query.filter_by(name = item).first().price
                total = total + (price_of_item * item_dict[item])
            total = round(total, 2)
            return  render_template('basket.html', title='Shopping Basket', basket = item_dict, total = total)

@app.route("/item/<item_identifier>") #stores the final url item as an item_identifier
def item(item_identifier):
    item_details = items.query.filter_by(name = item_identifier).first()
    return render_template('item.html', title = 'item', item_details = item_details) #pass 'item' object with all the data for the item in the next page
@app.route("/delete/<item_identifier>")
def delete(item_identifier):
    val = session["basket"]
    val.remove(item_identifier)
    session["basket"] = val
    return redirect("/basket/None")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST": #in the case that the user gets to the page through a redirect e.g by clicking 'my account'
        session.permanent = True
        username = request.form["UserName"]
        password = request.form["Password"]
        found_user = users.query.filter_by(username=username).first()
        if found_user:
            if found_user.verify_password(password):
                session["username"] = username
                session["name"] = found_user.name
                session["email"] = found_user.email
                session["is_admin"] = found_user.is_admin
                return render_template("user.html", is_admin = session["is_admin"])
            else:
                flash("UserName or password incorrect")
                return render_template("login.html")
        else:
            flash("Username or password incorrect")
            return render_template("login.html")
        return redirect(url_for("user"))
    else:
        if "username" in session: #in the case that the user gets to the page via url or they typed in the wrong details
            return render_template("user.html", is_admin = session["is_admin"])
        return render_template("login.html")

@app.route("/user", methods = ["POST", "GET"])
def user():
    if "username" in session:
        username = session["username"]
        if request.method=="POST":
            email = request.form["email"]
            if users.query.filter_by(email = email).first():
                flash("Email already in use")
            else:
                session["email"] = email
                users.query.filter_by(username = username).first().email = email
                db.session.commit()
                flash("Email changed")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email = email, username = username, is_admin = session["is_admin"])
    else:
        flash("Please log in to access your account")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "username" in session:
        username = session["username"]
        flash("You have successfully logged out", "info")
    session.pop("username", None)
    session.pop("name", None)
    session.pop("password", None)
    session.pop("email", None)
    session.pop("is_admin", None)
    return redirect(url_for("login"))

@app.route("/delete_account", methods = ["POST", "GET"])
def delete_account():
    if "username" in session:
        username = session["username"]
        users.query.filter_by(username=username).delete()
        db.session.commit()
    session.pop("username", None)
    session.pop("name", None)
    session.pop("password", None)
    session.pop("email", None)
    session.pop("is_admin", None)
    return redirect(url_for("login"))

@app.route("/create_account", methods = ["POST", "GET"])
def create_account():

    if request.method == "POST":
        username = request.form["UserName"]
        name = request.form["Name"]
        email = request.form["Email"]
        password = request.form["Password"]
        is_admin = False
        session["username"] = username
        session["name"] = name
        session["email"] = email
        session["password"] = password
        session["is_admin"] = False

        if users.query.filter_by(email=email).first():
            flash("Email already in use")
            return render_template("create account.html")
        elif users.query.filter_by(username=username).first():
            flash("UserName already in use")
            return render_template("create account.html")
        else:
            usr = users(username, name, email, password, is_admin)
            db.session.add(usr)
            db.session.commit()
        return render_template("user.html", email = email, username = username, is_admin = session["is_admin"])
    else:
        if "username" in session:
            return render_template("user.html", email = email, username = username, is_admin = session["is_admin"])
        return render_template("create account.html")

@app.route("/checkout", methods = ["POST", "GET"])
def checkout():
    return render_template('checkout.html', title='Checkout')

if __name__ == '__main__':
    db.create_all()
    db.create_all(bind  = ["Items"])
    app.run()
