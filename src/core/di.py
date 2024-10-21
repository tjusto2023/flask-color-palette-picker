from kink import di as container
from .config import Config
from application.repositories.user_repository import IUserRepository
from infra.repositories.user_repository import UserRepository

def setup_dependency_container() -> None:
    container[Config] = Config
    container[IUserRepository] = UserRepository
