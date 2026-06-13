"""A simple Flask application that returns "Hello World!" when accessed at the root URL."""

from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "author": "John Doe",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 20, 2024",},
        {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2024",
        }
]

@app.route("/")
@app.route("/home")
def home():
    """Return a simple greeting message."""
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    """Return information about the application."""
    return render_template("about.html", title="About")

if __name__ == "__main__":
    app.run(debug=True)
