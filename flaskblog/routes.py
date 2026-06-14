"""Routes"""
from flask import Blueprint, render_template, request, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog.forms import RegistrationForm, LoginForm
from .  import db,bcrypt
from .models import User

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
    if current_user.is_authenticated:
        return redirect(url_for('blog.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for("blog.home"))
    return render_template("register.html", title="Register", form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    """Register form"""
    if current_user.is_authenticated:
        return redirect(url_for('blog.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else  redirect(url_for("blog.home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)

@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('blog.home'))


@bp.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')