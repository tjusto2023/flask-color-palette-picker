from flask import Flask
from .di import DependencyInjection
from .database import initialize_db
from .config import Config
from application.interfaces.repositories.user_repository import IUserRepository
from infra.repositories.user_repository import UserRepository
app = Flask(__name__)

@app.before_request
def startRequest():
    DependencyInjection.startRequest()

@app.teardown_request
def endRequest():
    DependencyInjection.endRequest()

def injectProviders():
    DependencyInjection.addSingleton(Config, Config)
    DependencyInjection.addScoped(IUserRepository, UserRepository)

def bootstrap():
    injectProviders()
    initialize_db()
    
    return app

if __name__ == "__main__":
    app = bootstrap()
    app.run(debug=True)