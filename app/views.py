from app import app
from .subscribe import SubscribeForm, processSubscriber
from .login import LoginForm
from .dashboard import loadSubscribers, deleteSubscribers
from flask import render_template, flash, redirect, url_for

@app.route('/')
def nav_index():
	return render_template('index.html')

@app.route('/subscribe',methods=['GET', 'POST'])
def nav_subscribe():
	form = SubscribeForm()
	if form.validate_on_submit():
		processSubscriber(form.name.data,form.email.data,form.phone_num.data)
	return render_template('subscribe.html', form=form)	

@app.route("/", subdomain="admin")
def nav_dashboard():
	subscribers = loadSubscribers()
	return render_template('dashboard.html', subs=subscribers)
	#form = LoginForm()
    	#return render_template('login.html', form=form)	

@app.route("/delete/<id>", subdomain="admin")
def delete(id):
	if deleteSubscribers(id)== True:
		flash("Subscriber deleted")
	else:
		flash("Unable to delete subscriber")
	return redirect(url_for('nav_dashboard'))

@app.route("/broadcast", subdomain="admin")
def nav_broadcast():
	return "hello world"

