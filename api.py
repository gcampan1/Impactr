from uuid import uuid4
from flask import Blueprint, request, abort, jsonify, Response
from schema import Schema

from mongo import mongo

api = Blueprint("api", __name__)

player_schema = Schema({
  "firstname": str,
  "age": int,
  "height": float,
  "weight": float
})

impact_schema = Schema({
  "player": str,
  "data": float,
  "dt": int
})

@api.route("/players", methods=["GET", "POST"])
def players():
  if request.method == "POST":
    # Validate data
    data = request.json
    try:
      player_schema.validate(data)
    except:
      abort(400)
    # Add a player
    data["player_id"] = str(uuid4())
    mongo.db.players.insert(data)
    return Response("OK", status=200)
  else:
    # Retrieve a player
    return jsonify(list(mongo.db.players.find({}, {"_id":0})))

@api.route("/impact")
def impact():
    return "impact"
