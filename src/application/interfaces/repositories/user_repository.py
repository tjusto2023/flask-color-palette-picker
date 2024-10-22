from abc import ABC, abstractmethod
from typing import List, Union
from infra.models.user_model import UserModel
from domains.user import User
from src.domains.picture import Picture

class IUserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> Union[UserModel]:
        raise NotImplementedError("This method needs to be implemented in the subclass.")
    
    @abstractmethod
    def get_all(self) -> List[Union[UserModel]]:
        raise NotImplementedError("This method needs to be implemented in the subclass.")

    @abstractmethod
    def get_by_id(self, user_id: str) -> Union[UserModel]:
        raise NotImplementedError("This method needs to be implemented in the subclass.")
    
    @abstractmethod
    def add_pictures(self, user_id: str, picture: Picture) -> Union[UserModel]:
        raise NotImplementedError("This method needs to be implemented in the subclass.")
    
    @abstractmethod
    def get_picture_by_user_id(self, user_id: str, picture_id: str) -> Union[UserModel]:
        raise NotImplementedError("This method needs to be implemented in the subclass.")