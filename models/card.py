from mongoengine import *
from utils.validation import not_empty


class Card(Document):
    title = StringField(validation=not_empty, required=True)
    userId = ObjectIdField(required=True)
    boardId = ObjectIdField(required=True)
