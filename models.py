from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class ProjectModel(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())