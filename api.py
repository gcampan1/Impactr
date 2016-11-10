import logging
from uuid import uuid4

from flask import Blueprint, request, abort, jsonify, Response
from schema import Schema, Optional, SchemaError

import store

logger = logging.getLogger(__name__)

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
  "bpm": int,
  Optional("other1"): object,
  Optional("other2"): object,
  Optional("other3"): object,
  Optional("other4"): object,
})

def check_auth(u, p):
    user = store.db.users.find_one({"username": u})
    if not user: return False
    return sha256(p.encode()).hexdigest() == user["password"]

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return jsonify(
                msg="Login First"
            ), 401, {"WWW-Authenticate": 'Basic realm="Login Required"'}
        return f(*args, **kwargs)
    return decorated

@api.errorhandler(ValueError)
def type_conversion_error(error):
    logger.exception(error)
    return jsonify(
        msg=str(error)
    ), 400

@api.errorhandler(SchemaError)
def schema_error(error):
    logger.exception(error)
    return jsonify(
        msg=str(error)
    ), 400

@api.route("/register", methods=["POST"])
def register():
    # Validate
    data = request.json
    registration_schema.validate(data)

    height = float(data["height"])
    weight = float(data["weight"])

    pw = sha256(data["password"].encode()).hexdigest()

    data["height"] = height
    data["weight"] = weight
    data["password"] = pw
        
    # Check if email exists
    if store.db.users.find_one({"email": data["email"]}):
        return jsonify(
            msg="user exists"
        ), 409

    # Generate a username
    twoNumbers = lambda: str(random.randint(0, 9)) + str(random.randint(0, 9))
    username = lambda: data["firstName"][0].lower() + data["lastName"].lower() + twoNumbers()
    exists = lambda: store.db.users.find_one({"username": data["username"]})

    data["username"] = username()
    while exists():
        data["username"] = username()

    # Add two fields: devices and friends
    data["devices"] = []
    data["friends"] = [data["username"]]

    # Insert if it passes all the checks
    store.db.users.insert(data)
    return jsonify(
        username=data["username"]
    ), 201

@api.route("/users", methods=["GET", "POST"])
@requires_auth
def users():
    auth = request.authorization
    return jsonify(list(store.db.users.find({
        "friends": {"$in": [auth.username]}
    }, {"_id": 0, "password": 0})))

@api.route("/impact", methods=["GET", "POST"])
def impact():
  if request.method == "POST":
    #Validate data
    data = request.json
    impact_schema.validate(data)

    #Add Impact data
    #data["impact_data"] = store.db.players.find_one({"_id":0})
    store.db.impact.insert(data) 
    return Response("OK", status=200)
  else:
    # Retrieve Impact Data
    return jsonify(list(store.db.impact.find({}, {"_id":0})))

@api.route("/players/<player_id>/impact", methods=["GET", "POST"])
def impact_for_player(player_id):
    if request.method == "POST":
        data = request.json
        try:
            impact_schema.validate(data)
        except:
            abort(400)
        data["player_id"] = player_id
        store.db.impact.insert(data)
        return Response("OK", status=200)

    # GET
    impact_data = store.db.impact.find({"player_id": player_id}, {"_id": 0})
    return jsonify(list(impact_data))

