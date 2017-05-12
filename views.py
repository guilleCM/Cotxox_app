from flask import render_template, redirect, flash, url_for, session
from forms import LoginForm, SignupForm
from datetime import timedelta
from flask_login import current_user, login_required, login_user, logout_user

from middleware.Utils import Utils

from app import app, db, login_manager
from models import Users

@app.route('/')
@app.route('/index')
@login_required
def index():
	device = Utils.getDevice()
	return render_template("/"+device+"/index.html",
							device=device)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	if form.validate_on_submit():
		firstName = form.firstName.data
		lastName = form.lastName.data
		email = form.email.data
		password = form.password.data
		repeatPassword = form.repeatPassword.data
		if Users.query.filter_by(email=email).first() is not None:
			flash('This email is already in use! Please try with another one', 'red')
			return redirect(url_for('signup'))
		if password != repeatPassword:
			flash('The password fields doesn\'t match!', 'red')
			return redirect(url_for('signup'))
		new_user = Users(email, password, firstName, lastName)
		db.session.add(new_user)
		db.session.commit()
		flash('Succesfully registered. Now you can log in', 'green')
		return redirect(url_for('login'))


	return render_template("signup.html",
							form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		email = form.email.data
		password = form.password.data
		user = Users.query.filter_by(email=email).first()
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
	return Users.query.get(int(id))

@app.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))

#custom flash incorrect login message
login_manager.login_message = "You need login to acces this page."
login_manager.login_message_category = "red"
