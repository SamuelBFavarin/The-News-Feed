from functools import wraps
from flask import request

import app.main.services.auth_service as Auth


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        auth_headers = request.headers.get('Authorization', '').split()

        try:
            token = auth_headers[0]
        except:
            response = {'status': 'fail', 'message': 'You must send a token'}
            return response, 400

        if Auth.is_valid_token(token) == False:
            response = {'status': 'fail', 'message': 'Invalid auth token'}
            return response, 401

        return f(*args, **kwargs)

    return decorated
