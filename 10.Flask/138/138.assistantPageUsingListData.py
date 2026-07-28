# ------------------------------------------
# ! ---- assistant page using list data ----
# ------------------------------------------

from flask import Flask, render_template

Adham_app = Flask(__name__)

my_assistant = [
    ("Adham", "python developer"),
    ("adham", "java developer"),
    ("el_dod", "C++ developer"),
]


@Adham_app.route("/")
def homepage():
    return render_template("homepage.html", title="Home Page", custom_css="home")


@Adham_app.route("/add")
def add():
    return render_template("add.html", title="Add Assistant", custom_css="add")


@Adham_app.route("/about")
def about():
    return render_template("about.html", title="About Page")


@Adham_app.route("/assistant")
def assistant():
    return render_template(
        "assistant.html",
        title="Assistant Page",
        page_head="Assistant Page",
        description="This is the assistant page which include my assistant",
        assistants=my_assistant,
    )


if __name__ == "__main__":
    Adham_app.run(debug=True, port=9999)
