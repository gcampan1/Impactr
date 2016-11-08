from flask import Blueprint, render_template

www = Blueprint("www", __name__, template_folder="templates")

@www.route("/")
def home():
    return render_template("homepage.html")

@www.route("/players")
def players():
    return render_template("players.html")

@www.route("/players/new")
def player_form():
    return render_template("playerform.html")

@www.route("/coaches")
def coaches():
    return render_template("coachform.html")

@www.route("/parents")
def parents():
    return render_template("parentform.html")

@www.route("/contact")
def contact():
    return render_template("contact.html")

@www.route("/data")
def data():
    return render_template("data.html")

@www.route("/histogram")
def histogram():
    return render_template("histogram.html")

@www.route("/linegraph")
def linegraph():
    return render_template("linegraph.html")
