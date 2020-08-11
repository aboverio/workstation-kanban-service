from flask import jsonify


class BadRequestError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload_key=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

        if payload is not None and payload_key is not None:
            if type(payload) is list or type(payload) is dict:
                self.payload = {
                    payload_key: payload
                }
        else:
            self.payload = payload

    def to_dict(self):
        err = dict(self.payload or ())
        err['message'] = self.message
        return err
