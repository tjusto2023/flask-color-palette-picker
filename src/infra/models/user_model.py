from mongoengine import Document, StringField, EmbeddedDocumentListField
from .picture_model import PictureModel

class UserModel(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    pictures = EmbeddedDocumentListField(PictureModel)

    meta = { 'collection': 'users' }

    