from flask import Flask, render_template, redirect, session, flash
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

        user = User.register(username, pwd, email, first_name, last_name)

        db.session.add(user)
        db.session.commit()
        session["username"] = user.username
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
            session["username"] = user.username
            return redirect("/secret")
        else:
            form.username.errors = ["Incorrect Username/Password"]
    return render_template("login.html", form=form)


@app.route("/secret")
def secret_page():
    user = session.get("username")
    if user:
        return redirect(f"/users/{user}")
    else:
        return redirect("/")


@app.route("/logout")
def logout():
    session.pop("username")
    return redirect("/")


@app.route("/users/<username>")
def user_info(username):
    check_user = session.get("username")
    if check_user == username:
        user = User.query.get_or_404(username)
        return render_template("user-info.html", user=user)
    else:
        flash("Must be logged in to view that page, please make an account or sign in")
        return redirect("/")
