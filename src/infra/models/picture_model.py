from mongoengine import ObjectIdField, ListField, StringField, EmbeddedDocument
from bson import ObjectId

class PictureModel(EmbeddedDocument):
    id = ObjectIdField(default=ObjectId)
    name_file = StringField()
    name = StringField()
    color_palette = ListField(StringField())