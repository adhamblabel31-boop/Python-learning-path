# ----------------------------------------------
#! ------ create & extends HTML templates ------
# ----------------------------------------------

from flask import Flask, render_template

Adham_app = Flask(__name__)


@Adham_app.route("/")
def homepage():
    return render_template("homepage.html", pagetitle="Home Page")


@Adham_app.route("/about")
def about():
    return render_template("about.html", pagetitle="About Page")


if __name__ == "__main__":
    Adham_app.run(debug=True, port=9999)
