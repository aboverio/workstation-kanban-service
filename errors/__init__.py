from flask import Blueprint, jsonify

from .bad_request_error import BadRequestError
from .unauthorized_error import UnauthorizedError
from .not_found_error import NotFoundError

error_handlers = Blueprint('errors', __name__)


@error_handlers.app_errorhandler(BadRequestError)
def handle_bad_request(err):
    res = jsonify(err.to_dict())
    res.status_code = err.status_code
    return res


@error_handlers.app_errorhandler(UnauthorizedError)
def handle_unauthorized(err):
    res = jsonify(err.to_dict())
    res.status_code = err.status_code
    return res


@error_handlers.app_errorhandler(NotFoundError)
def handle_not_found(err):
    res = jsonify(err.to_dict())
    res.status_code = err.status_code
    return res
