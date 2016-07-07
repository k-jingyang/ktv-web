from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from app import app, mysql

class LoginForm(Form):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Name', validators=[DataRequired()])

def processLogin(username, password):
	pass

