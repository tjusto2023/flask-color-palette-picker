from flask import Flask
from .di import DependencyInjection
from .database import initialize_db
from .config import Config
from application.interfaces.repositories.user_repository import IUserRepository
from infra.repositories.user_repository import UserRepository

def injectProviders():
    DependencyInjection.addSingleton(Config, Config)
    DependencyInjection.addScoped(IUserRepository, UserRepository)

def bootstrap():
    injectProviders()
    initialize_db()

    app = Flask(__name__)
    return app

if __name__ == "__main__":
    app = bootstrap()
    app.run(debug=True)