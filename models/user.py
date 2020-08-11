from mongoengine import *
from utils.validations.model_validation import ModelValidation


class User(Document):
    firstName = StringField(validation=ModelValidation.not_empty, required=True)
    lastName = StringField()
    username = StringField(validation=ModelValidation.not_empty, required=True)
    email = StringField(validation=ModelValidation.not_empty, required=True)
    password = StringField(validation=ModelValidation.not_empty, required=True)
