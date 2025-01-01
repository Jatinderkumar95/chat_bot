from flask import Flask 
import os
from web.db import db


def create_app(db_url = None):
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"]=db_url or os.getenv("DATABASE_URL","sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    db.__init__(app=app)

    @app.before_request
    def create_tables():
        db.create_all()
    return app