from mongoengine import *
from utils.validations import not_empty
from models.card import Card


class Board(Document):
    title = StringField(validation=not_empty, required=True)
    userId = ObjectIdField(required=True)
    cards = ListField(ReferenceField(Card))
