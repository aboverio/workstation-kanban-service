from mongoengine import *
from utils.validations.model_validation import ModelValidation
import bcrypt


class User(Document):
    firstName = StringField(validation=ModelValidation.not_empty)
    lastName = StringField()
    username = StringField(validation=ModelValidation.not_empty)
    email = StringField(validation=ModelValidation.not_empty)
    password = StringField(validation=ModelValidation.not_empty)

    def save(self, *args, **kwargs):
        self.password = bcrypt.hashpw(self.password, bcrypt.gensalt())
        super(User, self).save(*args, **kwargs)
