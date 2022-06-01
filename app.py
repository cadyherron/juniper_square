import json
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from util import execute_query, fetch_rows

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/")
def hello_world():
    return {"hi": "there"}


@app.route("/projects", methods=["POST", "GET"])
def projects():
    if request.method == "POST":
        name = request.json.get("name")
        execute_query(f"INSERT INTO projects (name) VALUES ('{name}');")
        # TODO: should return new object
        resp = jsonify(success=True)
        resp.status_code = 200
        return resp
    else:
        data = fetch_rows("SELECT * FROM projects;")
        return json.dumps([{**d} for d in data])


@app.route("/projects/<pid>", methods=["PUT"])
def update_project(pid):
    name = request.json.get("name")
    execute_query(f"UPDATE projects SET name = '{name}' WHERE id = {pid}")
    # TODO: should return dated object
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


@app.route("/projects/<pid>", methods=["DELETE"])
def delete_project(pid):
    execute_query(f"DELETE FROM projects WHERE id = {pid}")
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp
