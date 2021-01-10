from flask import request
from flask_restplus import Resource
from ..util.dto import AuthDto
from ..services.auth_service import generate_token

api = AuthDto.api
_auth = AuthDto.auth


@api.route('/')
class Auth(Resource):

    @api.response(201, 'Token successfully created.')
    @api.marshal_list_with(_auth, envelope='data')
    @api.doc('create a token')
    @api.expect(_auth, validate=True)
    def post(self):
        """Creates a new News """
        data = request.json

        return generate_token(data=data)
