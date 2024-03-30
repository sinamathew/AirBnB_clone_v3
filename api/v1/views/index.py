#!/usr/bin/python3
""" Index app """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def status():
    """ Return status """
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def get_stat():
    """ Get number of count of each object """
    classes = {"amenities": "Amenity",
               "cities": "City",
               "places": "Place",
               "reviews": "Review",
               "states": "State",
               "users": "User"}
    stat_ = {}
    for key, value in classes.items():
        stat_[key] = storage.count(value)
    return jsonify(stat_)
