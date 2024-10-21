from mongoengine import connect
from kink import di
from .config import Config

def initialize_db() -> None:
    try:
        config = di[Config]
        connect(db=config.MONGO_DB_NAME, host=config.MONGO_URI)
    except Exception as e:
        print(e)