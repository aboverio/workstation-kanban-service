from flask import *
import json

user_router = Blueprint('user_router', __name__)


@user_router.route('/')
def index():
    return 'This is user router'


@user_router.route('/signin', methods=['POST'])
def sign_in():
    return request.form
