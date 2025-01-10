import os
from flask import Flask

from app.Celery import celery_init_app
from app.web.config import Config
from app.web.db import db,init_db_command


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # app.config.from_mapping(
    #     CELERY=dict(
    #         broker_url="redis://localhost",
    #         result_backend="redis://localhost",
    #         task_ignore_result=True,
    #     )
    # )
    app.config.from_prefixed_env()
    register_extensions(app)
    if Config.CELERY["broker_url"]:
        celery_init_app(app)
    return app

def register_extensions(app):
    db.init_app(app)
    app.cli.add_command(init_db_command)