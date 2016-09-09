from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask("Impactr")
mongo = PyMongo(app)

@app.route("/api/players")
def players():
  return jsonify(list(mongo.db.players.find({}, {"_id":0})))

if __name__=="__main__":
  app.run(host="0.0.0.0", debug=True)
