from flask import Flask, request, render_template, app
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from flask_login import LoginManager
from flask_babelex import Babel

app = Flask(__name__)
                                            #mysql+pymysql://root:root@localhost/myDbName
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:12345678@database-test3306.clcqijtl2xor.us-east-1.rds.amazonaws.com/ManageUser?charset=utf8mb4"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=120)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['SECRET_KEY'] = 'ZJn5lf/gtvXQ3+CqXPA2C4dDk9tvbh+1gFq4mMyn'

db = SQLAlchemy(app=app)

login_manager = LoginManager(app=app)
login_manager.login_view = "login_account"
login_manager.login_message_category = 'info'

from my_app import routes, admin
from my_app import admin

babel = Babel(app=app)

@babel.localeselector
def get_locale():
    return 'vi'