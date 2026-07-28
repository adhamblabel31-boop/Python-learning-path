# ---------------------------------------------
# ! ------------- intro to Flask --------------
# ---------------------------------------------
# ? Flask is micro framework built with python
# ---------------------------------------------
# ? HTML
# ? CSS
# ? JavaScript
# ---------------------------------------------

from flask import Flask

Adham_app = Flask(__name__)


@Adham_app.route("/")
def homepage():
    return "Hello in Adham"


@Adham_app.route("/about")
def about():
    return "Adham is ENG"


if __name__ == "__main__":
    Adham_app.run(debug=True, port=9999)
