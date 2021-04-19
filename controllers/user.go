from flask import *
import bcrypt
import json

from models.user import User

from utils.validations.validation import Validation
from errors.unauthorized_error import UnauthorizedError
from errors.bad_request_error import BadRequestError


def user_sign_up():
    req_body = request.form

    found_users = User.objects(username=req_body['username'])

    if len(found_users):
        raise BadRequestError(message=f"User with username {req_body['username']} is already registered.")

    validation_dict = {
        'firstName': Validation.first_name(req_body['firstName']),
        'email': Validation.email(req_body['email']),
        'username': Validation.username(req_body['username']),
        'password': Validation.password(req_body['password'])
    }
    err_list = []

    for validation_key in validation_dict:
        if validation_dict[validation_key] is not None:
            err_list.append({
                validation_key: validation_dict[validation_key]
            })

    if len(err_list) > 0:
        raise BadRequestError('Validation Error', payload_key='messages', payload=err_list)
    else:
        new_user = User(
            firstName=req_body['firstName'],
            lastName=req_body['lastName'],
            username=req_body['username'],
            email=req_body['email'],
            password=bcrypt.hashpw(req_body['password'].encode('utf8'), bcrypt.gensalt())
        )
        new_user.save()
        new_user = json.loads(new_user.to_json())
        del new_user['password']
        new_user['_id'] = new_user['_id']['$oid']
        response_json = jsonify({
            'user': new_user,
            'message': 'Successfully signed up!'
        })
        return response_json, 201
