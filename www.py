from flask import Blueprint, render_template

www = Blueprint("www", __name__, template_folder="templates")

@www.route("/")
def home():
    return render_template("homepage.html")

@www.route("/players")
def players():
    return render_template("playerform.html")

@www.route("/coaches")
def coaches():
    return render_template("coachform.html")

@www.route("/parents")
def parents():
    return render_template("parentform.html")

