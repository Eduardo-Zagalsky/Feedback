from flask import Flask, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from forms import AddUserForm, LoginForm

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
    return redirect("/register")


@app.route("/register", methods=["GET", "POST"])
def new_user():

    form = AddUserForm()

    if form.validate_on_submit():
        username = form.username.data
        pwd = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        new_user = User.register(username, pwd, email, first_name, last_name)

        db.session.add(new_user)
        db.session.commit()
        return redirect("/secret")
    else:
        return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login_user():

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        pwd = form.password.data
        user = User.authenticate(username, pwd)
        if user:
            session["user_id"] = user.id
            return redirect("/secret")
        else:
            form.username.errors = ["Incorrect Username/Password"]
    else:
        return render_template("login.html", form=form)


@app.route("/secret")
def secret_page():
    return render_template("")
