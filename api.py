from uuid import uuid4
from flask import Blueprint, request, abort, jsonify, Response
from schema import Schema, Optional

from mongo import mongo

api = Blueprint("api", __name__)


player_schema = Schema({
  "name": str,
  "age": int,
  "height": float,
  "weight": float,
  #"MAC_addr": str
})

impact_schema = Schema({
  Optional("player_id"): str,
  "date": str,
  "time": str,
  "a_x": float,
  "a_y": float,
  "a_z": float,
  "roll": float,
  "pitch": float,
  "yaw": float,
  "ug_x": float,
  "ug_y": float,
  "ug_z": float,
  "o2": int,
  "hyd": int,
  "bpm": int
})

@api.route("/register", methods=["POST"])
def register():
    # TODO
    pass

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



@api.route("/impact", methods=["GET", "POST"])
def impact():
  if request.method == "POST":
    #Validate data
    data = request.json
    try:
      impact_schema.validate(data)
    except:
      abort(400)
    #Add Impact data
    #data["impact_data"] = mongo.db.players.find_one({"_id":0})
    mongo.db.impact.insert(data) 
    return Response("OK", status=200)
  else:
    #Retrieve Impact Data
    return jsonify(list(mongo.db.impact.find({}, {"_id":0})))

@api.route("/players/<player_id>/impact", methods=["GET", "POST"])
def impact_for_player(player_id):
    if request.method == "POST":
        data = request.json
        try:
            impact_schema.validate(data)
        except:
            abort(400)
        data["player_id"] = player_id
        mongo.db.impact.insert(data)
        return Response("OK", status=200)

    # GET
    impact_data = mongo.db.impact.find({"player_id": player_id}, {"_id": 0})
    return jsonify(list(impact_data))
