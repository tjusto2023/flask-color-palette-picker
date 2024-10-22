from typing import List
from application.interfaces.repositories.user_repository import IUserRepository
from infra.models.user_model import UserModel
from infra.models.picture_model import PictureModel
from domains.user import User
from domains.picture import Picture
from mongoengine import Q, DoesNotExist

class UserRepository(IUserRepository):
    def save(self, user: User) -> UserModel:
        userModel = UserModel(
                username=user.username, 
                email=user.email, 
                password=user.password,
                pictures=[]
            )
        
        userModel.save()
        return userModel
    
    def get_all(self) -> List[UserModel]:
        return list(UserModel.objects())
    
    def get_by_id(self, user_id: str) -> UserModel:
        user = UserModel.objects(id=user_id).first()

        if not user:
            raise DoesNotExist(f"Usuário com id {user_id} não encontrado.")
        
        return user
    
    def add_pictures(self, user_id: str, picture: Picture):
        userModel = self.get_by_id(user_id)

        if not userModel:
            raise DoesNotExist(f"Usuário com id {user_id} não encontrado.")
        
        picture_model = PictureModel(
            name_file = picture.name_file,
            name = picture.name,
            color_palette = picture.color_palette
        )

        userModel.pictures.append(picture_model)
        userModel.save()
        return userModel
           
    def get_picture_by_user_id(self, user_id: str, picture_id: str) -> UserModel:
        user = UserModel.objects(
            Q(id=user_id) & Q(pictures__match={"$elemMatch": {"id": picture_id}})
        ).only('username', 'id', 'pictures').first()

        if not user:
            raise DoesNotExist(f"Usuário com id {user_id} ou imagem com id {picture_id} não encontrada.")
        
        # user.color_palettes = [palette for palette in user.color_palettes if str(palette.id) == color_palette_id]

        return user