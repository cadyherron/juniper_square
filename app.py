import json
from flask import Flask, jsonify, json, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

from util import execute_query, validate_fields_from_json, fetch_rows
from queries import INSERT_NEW_PROJECT, SELECT_PROJECT_BY_ID, SELECT_ALL_PROJECTS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.route("/")
def hello_world():
    return {"hi": "there"}


@app.route("/projects", methods=["POST", "GET"])
def projects():
    if request.method == "POST":
        validate_fields_from_json(request.json, ["name"])
        last_row_id = execute_query(INSERT_NEW_PROJECT.format(**request.json))
        new_project = fetch_rows(SELECT_PROJECT_BY_ID.format(last_row_id=last_row_id))
        return json.dumps([{**d} for d in new_project])
    else:
        data = fetch_rows(SELECT_ALL_PROJECTS)
        return json.dumps([{**d} for d in data])


@app.route("/projects/<pid>", methods=["PUT"])
def update_project(pid):
    name = request.json.get("name")
    execute_query(f"UPDATE projects SET name = '{name}' WHERE id = {pid}")
    updated_project = fetch_rows(f"SELECT * FROM projects WHERE id = {pid}")
    # TODO: should return updated object
    return json.dumps([{**d} for d in updated_project])


@app.route("/projects/<pid>", methods=["DELETE"])
def delete_project(pid):
    execute_query(f"DELETE FROM projects WHERE id = {pid}")
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


@app.route("/tags", methods=["POST", "GET"])
def tags():
    return "ok"
    # if request.method == "POST":
    #     text = request.json.get("text")
    #     last_row_id = execute_query(f"INSERT INTO tags (text) VALUES ('{text}');")
    #     new_tag = fetch_rows(f"SELECT * FROM tags WHERE id = {last_row_id}")
    #     return json.dumps([{**t} for t in new_tag])
    # else:
    #     data = fetch_rows("SELECT * FROM tags;")
    #     return json.dumps([{**d} for d in data])
