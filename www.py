from flask import Blueprint

www = Blueprint("www", __name__, template_folder="templates")

@www.route("/")
def players():
    return "home"
