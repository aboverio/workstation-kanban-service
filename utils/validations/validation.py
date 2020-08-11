import re

class Validation:
    @staticmethod
    def not_empty(val, field):
        if len(val) <= 0 or val is None:
            return {
                field: f'{field} cannot be empty!'
            }

    @staticmethod
    def first_name(first_name):
        if len(first_name) <= 0 or first_name is None:
            return 'First name cannot be empty!'

    @staticmethod
    def email(email):
        email_regex = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

        if len(email) <= 0 or email is None:
            return 'Email cannot be empty!'
        elif re.search(email_regex, email) is None:
            return 'Invalid email address!'

    @staticmethod
    def username(username):
        if len(username) <= 0 or username is None:
            return 'Username cannot be empty!'
        elif 0 < len(username) < 6:
            return 'Username must be 6 characters in length!'

    @staticmethod
    def password(password):
        if len(password) <= 0 or password is None:
            return 'Password cannot be empty!'
        elif 0 < len(password) < 6:
            return 'Password must be 6 characters in length!'
