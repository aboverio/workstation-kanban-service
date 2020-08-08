from mongoengine import  *


def not_empty(val):
    if not val:
        raise ValidationError(f'Cannot be empty!')
