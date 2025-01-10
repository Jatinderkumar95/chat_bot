
import os


class Config:
    SQLALCHEMY_DATABASE_URI =  os.getenv("DATABASE_URL","sqlite:///data.db")
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    CELERY = {
        "broker_url": os.environ.get("REDIS_URI", False),
        "task_ignore_result": True,
        "broker_connection_retry_on_startup": False,
    }
