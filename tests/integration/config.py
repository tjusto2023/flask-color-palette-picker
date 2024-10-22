import os
from dotenv import load_dotenv

class TestConfig:
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    MONGO_URI = os.getenv('MONGO_URI')
    MONGO_DB_NAME = 'testcolorpalettepicker'