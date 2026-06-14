"""Routes"""
from flask import Blueprint, render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm

bp = Blueprint("blog", __name__)

posts = [
    {
        "author": "Corey Schafer",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 20, 2018",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2018",
    },
]


@bp.route("/")
@bp.route("/home")
def home():
    """Return a simple greeting message."""
    return render_template("home.html", posts=posts)


@bp.route("/about")
def about():
    """Return information about the application."""
    return render_template("about.html", title="About")


@bp.route("/register", methods=["GET", "POST"])
def register():
    """Register form"""
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("blog.home"))
    return render_template("register.html", title="Register", form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    """Register form"""
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("blog.home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)
