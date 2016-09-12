from flask import Blueprint

api = Blueprint("api", __name__)

@api.route("/players")
def players():
    return "players"

@api.route("/impact")
def impact():
    return "impact"
