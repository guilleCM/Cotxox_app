from flask import render_template, redirect
#from forms import LoginForm

from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
	return render_template("login.html")