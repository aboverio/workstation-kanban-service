from mongoengine import *
from utils.validation import not_empty
import bcrypt


class User(Document):
    firstName = StringField(validation=not_empty)
    lastName = StringField()
    username = StringField(validation=not_empty)
    email = StringField(validation=not_empty)
    password = StringField(validation=not_empty)

    def save(self, *args, **kwargs):
        self.password = bcrypt.hashpw(self.password, bcrypt.gensalt())
        super(User, self).save(*args, **kwargs)
