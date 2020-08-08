from flask import *


def user_sign_in():
    return request.form['username']
