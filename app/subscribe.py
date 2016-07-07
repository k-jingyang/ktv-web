from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Email, Optional, DataRequired
from app import app, mysql

class SubscribeForm(Form):
	email = StringField('Email', validators=[Optional(), Email()])
	name = StringField('Name', validators=[DataRequired()])
	phone_num = StringField('Contact No.', validators=[Optional()])

def processSubscriber(name, email, phone_num):
	if phone_num.isdigit==False:
		return False
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO SUBSCRIBERS VALUES (%s, %s, %s, %s);", (0,name, email, int(phone_num)))
	cursor.close ()
   	conn.commit ()
  	conn.close ()
	print name, email, phone_num
	return True

