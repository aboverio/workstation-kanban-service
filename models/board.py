from mongoengine import *
import datetime

class Board(Document):
    title = StringField()
