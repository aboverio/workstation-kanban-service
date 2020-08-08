from flask import *

from utils.validations.validation import Validation


def user_sign_in():
    req_body = request.form
    error_list = []
    for field in req_body:
        curr_validation = Validation.username(req_body[field], field)
        if curr_validation:
            error_list.append(curr_validation)

    if len(error_list) > 0:
        make_response()

    return request.form['username']
