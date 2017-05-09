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
	form = LoginForm()
	if form.validate_on_submit():
		email = form.email.data
		password = form.password.data
		user = User.query.filter_by(email=email).first()
		if user is not None and user.get_password() == password:
			# numId = user.get_id()
			login_user(user)
			return redirect(url_for('index'))
		else:
			flash('Incorrect login', 'red')
			return redirect(url_for('login'))
	return render_template("login.html",
							form=form,
							)

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))

#custom flash incorrect login message
login_manager.login_message = "You need login to acces this page."
login_manager.login_message_category = "red"
