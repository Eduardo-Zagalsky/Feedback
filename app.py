from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def root():
    return render_template("")


@app.route("/register", methods=["GET", "POST"])
def new_user():
    if user:
        return redirect("/secret")
    else:
        return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login_user():
    if user:
        return redirect("/secret")
    else:
        return redirect("/")


@app.route("/secret")
def secret_page():
    return render_template("")
