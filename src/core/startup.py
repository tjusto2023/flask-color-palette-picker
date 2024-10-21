from flask import Flask
from .di import setup_dependency_container
from .database import initialize_db

def bootstrap():
    setup_dependency_container()
    initialize_db()

    app = Flask(__name__)
    return app

if __name__ == "__main__":
    app = bootstrap()
    app.run(debug=True)