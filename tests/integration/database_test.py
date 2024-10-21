import pytest
from mongoengine import disconnect
from src.core.di import setup_dependency_container
from src.core.database import initialize_db
from faker import Faker
faker = Faker()

from src.application.repositories.user_repository import IUserRepository
from src.infra.repositories.user_repository import UserRepository
from src.infra.models.user_model import UserModel
from src.infra.models.picture_model import PictureModel
from src.domains.picture import Picture
from src.domains.user import User
from bson import ObjectId
from mongoengine import ValidationError

@pytest.fixture(scope='module', autouse=True)
def setup_database():
    setup_dependency_container()
    initialize_db()

    yield

    # UserModel.drop_collection()
    disconnect()

@pytest.fixture
def user_repo() -> IUserRepository:
    # Given
    return UserRepository()

def create_user():
    return User(
        username = faker.user_name(),
        email = faker.email(),
        password = faker.password(),
    )

@pytest.fixture
def user_fixture() -> User:
    # Given
    return create_user()

@pytest.fixture
def picture_fixture() -> Picture:
    # Given
    return Picture(faker.image_url(), [faker.hex_color() for _ in range(5)])

class TestUserRepository:
    # def test_given_valid_inputs_when_user_created_then_instance_is_saved(
    #     self, user_repo: IUserRepository, user_fixture: User):

    #     # Act
    #     saved_user = user_repo.save(user_fixture)

    #     # Assert
    #     assert saved_user.username == user_fixture.username
    #     assert saved_user.email == user_fixture.email
    #     assert saved_user.password != user_fixture.password
    #     assert isinstance(saved_user.pictures, list) and len(saved_user.pictures) == 0
    #     assert saved_user.id is not None
    #     assert isinstance(saved_user.id, ObjectId)

    def test_given_picture_when_user_saves_picture_then_picture_is_saved(
        self, user_repo: IUserRepository, user_fixture: User, picture_fixture: Picture):

        # Act
        # saved_user = user_repo.save(user_fixture)
        # userModel = user_repo.get_by_id(saved_user.pk)

        user = UserModel(
            username="johndoe",
            email="johndoe@example.com",
            password="securepassword",
            pictures=[]  # Pass a list of PictureModel instances
        )

        saved_user = user_repo.save(user)

        # Criar uma nova instância de PictureModel
        picture = PictureModel(
            name_file='test_image.png',
            name='Test Image',
            # id=ObjectId()
            color_palette=['#FFFFFF', '#000000', '#FF5733']  # Exemplo de cores
        )

        saved_user.pictures.append(picture)

        saved_user.save()
        # userModel.save() # Salvar após adicionar a nova imagem

        # Act
        # saved_user = user_repo.save(user_fixture)
        # # userModel = user_repo.add_pictures(saved_user.pk, picture_fixture)
        # userModel = user_repo.get_by_id(saved_user.pk)
        
        # picture_model = PictureModel(
        #     name_file = picture_fixture.name_file,
        #     name = picture_fixture.name,
        #     color_palette = picture_fixture.color_palette
        # )

        # userModel.pictures.append(picture_model)
        # userModel.save()
        # # Assert
        # assert userModel.pictures[0].pk is not None
        # assert isinstance(saved_user.pictures, list) and len(saved_user.pictures) == 0
        # assert isinstance(userModel.pictures, list) and len(userModel.pictures) > 0
        # assert isinstance(userModel.pictures[0].id, ObjectId)

    # def test_given_users_created_when_get_all_then_return_all_users(
    #     self, user_repo: IUserRepository):

    #     UserModel.drop_collection()

    #     # Given
    #     user1 = create_user()
    #     user2 = create_user()

    #     # Act
    #     saved_user1 = user_repo.save(user1)
    #     saved_user2 = user_repo.save(user2)
    #     users = user_repo.get_all()
        
    #     # Assert
    #     assert isinstance(users, list) and len(users) == 2
    #     assert users[0].pk == saved_user1.pk
    #     assert users[1].pk == saved_user2.pk
