from flask import jsonify, request
from flask_smorest import abort, Blueprint

# Create Blueprint for items-related routes
items_blp = Blueprint("Items", "items", url_prefix="/api", description="Items description")


@items_blp.route("/welcome", methods=["GET"])
def welcome():
    return jsonify("Welcome to the application")


@items_blp.route("/items/welcome/<string:name>", methods=["GET"])
def welcome_by_name(name):
    return jsonify({"message": f"Hello : {name}"})


@items_blp.route("/items", methods=["POST"])
def create_item():
    payload = request.get_json()
    return jsonify(payload), 201


@items_blp.route("/items", methods=["GET"])
def get_one_item():
    data = request.args.get('include_regions', default=1, type=int)
    if data is None or data == 0:
        abort(404, message="No regions found")
    return jsonify({"got value": data})
