"""A simple Flask application that returns "Hello World!" when accessed at the root URL."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    """Return a simple greeting message."""
    return render_template("home.html")


@app.route("/about")
def about():
    """Return information about the application."""
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
