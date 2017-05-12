from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, RadioField, BooleanField, SelectField, HiddenField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class SignupForm(FlaskForm):
	username = StringField('username')
	password = PasswordField('password')
	repeatPassword = PasswordField('repeatpassword')
	email = StringField('email')
	firstName = StringField('firstName')
	lastName = StringField('lastName')