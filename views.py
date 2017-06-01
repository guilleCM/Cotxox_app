from flask import render_template, redirect, flash, url_for, session, request
from forms import LoginForm, SignupForm, RideForm
from datetime import timedelta
from flask_login import current_user, login_required, login_user, logout_user
import ast
from middleware.Utils import Utils
from controllers.services import ProviderAPI

from app import app, db, login_manager
from models import Users, Drivers

@app.route('/')
@app.route('/setpickup', methods=['GET', 'POST'])
@login_required
def setpickup():
	form = RideForm()
	device = Utils.getDevice()
	if request.method == 'POST':
		ride_data = form.ride_data.data
		return redirect(url_for('payment', ride_data=ride_data))
	return render_template("/"+device+"/setpickup.html",
							device=device,
							form=form)

@app.route('/payment/<ride_data>', methods=['GET', 'POST'])
@login_required
def payment(ride_data):
	form = RideForm()
	ride_dict = ast.literal_eval(ride_data)
	driver = Drivers.query.filter_by(id=ride_dict['driver']).first()
	driverPhoto = driver.profilePhoto
	device = Utils.getDevice()
	if request.method == 'POST':
		ride_data = form.ride_data.data
		return redirect(url_for('rate', ride_data=ride_data))
	return render_template("/"+device+"/payment.html",
							device=device,
							ride_dict=ride_dict,
							ride_data=ride_data,
							driverPhoto=driverPhoto,
							form=form)

@app.route('/rate/<ride_data>')
@login_required
def rate(ride_data):
	device = Utils.getDevice()
	return render_template("/"+device+"/rate.html",
							device=device,
							ride_data=ride_data)

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
		new_user = Users(email=email, password=password, firstName=firstName, lastName=lastName)
		db.session.add(new_user)
		db.session.commit()
		flash('Succesfully registered. Now you can log in', 'green')
		return redirect(url_for('login'))


	return render_template("signup.html",
							form=form)

@app.route('/getParameters/<startPoint>-<endPoint>')
def getParameters(startPoint, endPoint):
	parameters = ProviderAPI.getRidePreview(startPoint, endPoint)
	return parameters

@app.route('/getDriver')
@login_required
def getDriver():
	driver = ProviderAPI.getDriver();
	return driver

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		email = form.email.data
		password = form.password.data
		user = Users.query.filter_by(email=email).first()
		if user is not None and user.get_password() == password:
			login_user(user)
			return redirect(url_for('setpickup'))
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
