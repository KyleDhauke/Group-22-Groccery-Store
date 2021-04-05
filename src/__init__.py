from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_googlemaps import GoogleMaps
import os

APP_PATH = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

# Set up error handling functions
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="404 Not Found")

app.secret_key = '5f657845a13f155c09feb146033e700bd5e2b966531a8907'

app.config['GOOGLEMAPS_KEY'] = "8JZ7i18MjFuM35dJHq70n3Hx4"
GoogleMaps(app)
app.config['SECRET KEY'] = '5f657845a13f155c09feb146033e700bd5e2b966531a8907'
app.config['WTF_CSRF_SECRET_KEY'] = '5f657845a13f155c09feb146033e700bd5e2b966531a8907'

csrf = CSRFProtect(app)
csrf.init_app(app)

# Configure database access
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c1914891:Ihatemysql1@csmysql.cs.cf.ac.uk:3306/c1914891_onlineShop'
app.register_error_handler(404, page_not_found)

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)

# Setup product image upload folder
app.config['UPLOAD_FOLDER'] = "static/Media/ProductImages"

from src import routes
