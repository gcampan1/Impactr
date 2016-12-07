from flask import Blueprint, render_template

www = Blueprint("www", __name__, template_folder="templates")

@www.route("/")
def home():
    return render_template("homepage.html")

@www.route("/players")
def players():
    return render_template("players.html")

@www.route("/players/<username>")
def player_by_id(username):
    return render_template("player_data.html")

@www.route("/login")
def login():
    return render_template("login.html")

@www.route("/register")
def register():
    return render_template("register.html")

@www.route("/contact")
def contact():
    return render_template("contact.html")

@www.route("/d3")
def d3():
    return render_template("d3.html")

@www.route("/histogram")
def data():
    return render_template("newd3.html")

@www.route("/linegraph")
def linegraph():
	return render_template("linegraphtest.html")

