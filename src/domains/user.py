import bcrypt
from .picture import Picture

class User:
    def __init__(self, username: str, email:str, password: str, pictures = None):
        self.username = username
        self.email = email
        self.password = self._hash_password(password)

        if pictures is None:
            self.pictures = []

    def add_picture(self, picture: Picture):
        self.pictures.append(picture)

    @staticmethod
    def _hash_password(password: str) -> bytes:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed

    @staticmethod
    def check_password(password: str, hashed_password: bytes) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)