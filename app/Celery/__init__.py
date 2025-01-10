
from celery import Celery, Task
from flask import Flask


def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return super().__call__(*args, **kwargs)
    celery_app = Celery(app.Name,task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"]) 
    celery_app.set_default()
    app.extensions["celery"]=celery_app 
    return celery_app
        
        