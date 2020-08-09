from flask import *

from controllers.user import *

user_router = Blueprint('user_router', __name__)


@user_router.route('/')
def index():
    return 'This is user router'


@user_router.route('/signin', methods=['POST'])
def sign_in():
    return 'this is sign in'


@user_router.route('/signup', methods=['POST'])
def sign_up():
    return user_sign_up()


@user_router.route('/<user_id>', methods=['PUT', 'PATCH', 'DELETE'])
def user_requests(user_id):
    if request.method == 'PUT':
        return 'this is update user'
    elif request.method == 'PATCH':
        return 'this is update user password'
    elif request.method == 'DELETE':
        return 'this is delete user'
