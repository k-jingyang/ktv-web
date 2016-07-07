from flask import Flask
from flaskext.mysql import MySQL
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
mysql = MySQL()
mysql.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
from app import views
