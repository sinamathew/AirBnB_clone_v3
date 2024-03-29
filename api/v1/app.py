#!/usr/bin/python3
""" Endpoint of API """
from flask import Flask, jsonify, make_response
from os import getenv
from models import storage
from api.v1.views import app_views

# get environment variables
host = getenv("HBNB_API_HOST", "0.0.0.0")
port = getenv("HBNB_API_PORT", 5000)

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """ Calls the close method """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ Return not found """
    return make_response(jsonify({"error": "Not found"}))


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host=host, port=port)
