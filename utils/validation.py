from mongoengine import  *


def not_empty(val, attribute_name):
    if not val:
        raise ValidationError(f'{attribute_name} cannot be empty!')
