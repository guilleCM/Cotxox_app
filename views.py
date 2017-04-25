from flask import render_template, redirect
#from forms import LoginForm

from app import app, db
from models import User


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
	demo = User.query.filter_by(username='demo').first()
	return render_template("login.html",
						   demo=demo)