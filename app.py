from flask import Flask, jsonify, request, abort, Response
from flask_pymongo import PyMongo
from schema import Schema
from uuid import uuid4

app = Flask("Impactr")
mongo = PyMongo(app)

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

@app.route("/api/players", methods=["GET", "POST"])
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

@app.route("/api/impact")
def impact():
    return "impact"

if __name__=="__main__":
  app.run(host="0.0.0.0", debug=True)

#guychange



