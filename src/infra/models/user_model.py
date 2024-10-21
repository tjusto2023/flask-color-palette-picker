from mongoengine import Document, StringField, ListField, EmbeddedDocumentField
from .picture_model import PictureModel

class UserModel(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    pictures = ListField(EmbeddedDocumentField(PictureModel))

    meta = { 'collection': 'users' }