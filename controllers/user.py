from flask import *

from models.user import User

from utils.validations.validation import Validation
from errors.unauthorized_error import UnauthorizedError
from errors.bad_request_error import BadRequestError


def user_sign_up():
    req_body = request.form
    err_dict = {
        'firstName': Validation.username(field=)
    }

    if len(err_dict.values()) > 0:
        raise BadRequestError('Validation error.', payload_key='messages', payload=error_list)
    else:
        new_user = User(
            firstName=req_body['firstName'],
            lastName=req_body['lastName'],
            username=req_body['username'],
            email=req_body['email'],
            password=req_body['password']
        )
        new_user.save()
        print(new_user)
