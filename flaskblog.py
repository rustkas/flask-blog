"""A simple Flask application that returns "Hello World!" when accessed at the root URL."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    """Return a simple greeting message."""
    return "<h1>Home Page</h1>"


@app.route("/about")
def about():
    """Return information about the application."""
    return "<h1>About Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)
