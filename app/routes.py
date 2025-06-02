from flask import Blueprint, request, jsonify
from .db import init_db, insert_entry, get_entries
from .crypto import generate_password

api_blueprint = Blueprint('api', __name__)
init_db()

@api_blueprint.route("/")
def home():
    return "Password Vault API"

@api_blueprint.route("/generate", methods=["GET"])
def generate():
    length = request.args.get('length', default=20, type=int)
    return jsonify({"password": generate_password(length)})

@api_blueprint.route("/db", methods=["GET"])
def list_vault():
    return jsonify(get_entries())

@api_blueprint.route("/db", methods=["POST"])
def add_to_vault():
    data = request.json
    site = data.get("site")
    username = data.get("username")
    password = data.get("password", generate_password())
    insert_entry(site, username, password)
    return jsonify({"status": "added"})