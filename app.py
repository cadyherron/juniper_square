from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/jsq"


@app.route("/")
def hello_world():
    return {"hi": "there"}
