from flask import render_template, redirect, flash, url_for, session, request
from forms import LoginForm
from datetime import timedelta
from flask_login import current_user, login_required, login_user, logout_user

from app import app, db, login_manager
from models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
	return render_template("index.html")

@app.route('/signup')
def signup():
	demo = User.query.filter_by(username='demo').first()
	return render_template("signup.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate_on_submit():
		email = form.email.data
		password = form.password.data
		session['logged_in'] = True
		user = User.query.filter_by(email=email).first()
		if(user != None):
			if(user.get_password() == password):
				return redirect(url_for('index'))
			else:
				flash('Incorrect password', 'red')
				redirect(url_for('login'))
		else:
			flash('Incorrect email', 'red')
			redirect(url_for('login'))
	
	return render_template("login.html",
							form=form,
							)


@app.before_request
def before_request():
	session.permanent = True
	app.permanent_session_lifetime = timedelta(minutes=5)

@login_manager.user_loader
def load_user(user_email):
	return User.query.filter_by(email=user_email).first()

@app.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))

#custom flash incorrect login message
login_manager.login_message = "You need login to acces this page."
login_manager.login_message_category = "red"
