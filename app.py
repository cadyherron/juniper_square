import json
import sqlite3 as sql
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/jsq"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/")
def hello_world():
    return {"hi": "there"}


@app.route("/projects")
def index():
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from projects")
    data = cur.fetchall()
    return json.dumps([{**d} for d in data])


@app.route("/create", methods=['POST', 'GET'])
def create_project():
    if request.method == 'POST':
        name = request.json.get("name")
        con = sql.connect("db_web.db")
        cur = con.cursor()
        cur.execute(f"insert into projects (name) values ('{name}');")
        con.commit()
        resp = jsonify(success=True)
        resp.status_code = 200
        return resp
#
#
# @app.route("/edit_user/<string:uid>", methods=['POST', 'GET'])
# def edit_user(uid):
#     if request.method == 'POST':
#         uname = request.form['uname']
#         contact = request.form['contact']
#         con = sql.connect("db_web.db")
#         cur = con.cursor()
#         cur.execute("update users set UNAME=?,CONTACT=? where UID=?", (uname, contact, uid))
#         con.commit()
#         flash('User Updated', 'success')
#         return redirect(url_for("index"))
#     con = sql.connect("db_web.db")
#     con.row_factory = sql.Row
#     cur = con.cursor()
#     cur.execute("select * from users where UID=?", (uid,))
#     data = cur.fetchone()
#     return render_template("edit_user.html", datas=data)
#
#
# @app.route("/delete_user/<string:uid>", methods=['GET'])
# def delete_user(uid):
#     con = sql.connect("db_web.db")
#     cur = con.cursor()
#     cur.execute("delete from users where UID=?", (uid,))
#     con.commit()
#     flash('User Deleted', 'warning')
#     return redirect(url_for("index"))
