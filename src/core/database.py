from mongoengine import connect
from core.di import DependencyInjection 

def initialize_db() -> None:
    try:
        config = DependencyInjection.inject('Config')
        connect(
            db=config.MONGO_DB_NAME, 
            host=config.MONGO_URI
        )
    except Exception as e:
        print(e)