# --------------------------------------------
#! ----- advanced Css task using Jinja -------
# --------------------------------------------

from flask import Flask, render_template

Adham_app = Flask(__name__)


@Adham_app.route("/")
def homepage():
    return render_template("homepage.html", title="Home Page", custom_css="home")


@Adham_app.route("/add")
def add():
    return render_template("add.html", title="Add Assistant", custom_css="add")


@Adham_app.route("/about")
def about():
    return render_template("about.html", title="About Page")


if __name__ == "__main__":
    Adham_app.run(debug=True, port=9999)
