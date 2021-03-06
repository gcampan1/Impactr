from flask import Flask, jsonify, request, abort, Response
from uuid import uuid4

from api import api
from www import www

app = Flask("Impactr")

# Register website
app.register_blueprint(www)

# Register app
app.register_blueprint(api, url_prefix="/api")

if __name__=="__main__":
  app.run(host="0.0.0.0", debug=True)
