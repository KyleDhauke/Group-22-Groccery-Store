from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_mail import Mail,Message
import os

#undoing bad commit
APP_PATH = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

# Set up error handling functions
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="404 Not Found")

app.secret_key = '5f657845a13f155c09feb146033e700bd5e2b966531a8907'

app.config['SECRET KEY'] = '5f657845a13f155c09feb146033e700bd5e2b966531a8907'
app.config['WTF_CSRF_SECRET_KEY'] = '5f657845a13f155c09feb146033e700bd5e2b966531a8907'

csrf = CSRFProtect(app)
csrf.init_app(app)

# Configure database access
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c1932063:Team22project@csmysql.cs.cf.ac.uk:3306/c1932063_Team22Year2'
app.register_error_handler(404, page_not_found)



login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)

#mail settings
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
# 注意这里启用的是TLS协议(transport layer security)，而不是SSL443协议所以用的是25号端口
app.config['MAIL_USERNAME'] = 'wyyrx0530@163.com'
app.config['MAIL_PASSWORD'] = 'LOGYRXSQBWUARANA'

app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[confirm]'
app.config['FLASKY_MAIL_SENDER'] = 'wyyrx0530@163.com'

mail = Mail(app)


# Setup product image upload folder
app.config['UPLOAD_FOLDER'] = "static/Media/ProductImages"

from src import routes
