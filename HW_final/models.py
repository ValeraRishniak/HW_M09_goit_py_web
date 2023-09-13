from mongoengine import Document, CASCADE
from mongoengine.fields import ReferenceField, ListField, StringField
from connect import connect



class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    bio = StringField()


class Qoute(Document):
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    qoute = StringField()
    tags = ListField(StringField())
    meta = {'allow_inheritance': True}