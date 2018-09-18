from flask import request
from flask_restful import Resource

from parsers.user_parser import UserParser


class UserResource(Resource):
    def get(self):
        from app.models import User
        status = 200
        # get the auth token
        auth_header = request.headers.get('Authorization')
        # check if user already exists
        auth_token = ''
        if auth_header:
            auth_header_list = auth_header.split(" ")
            if len(auth_header_list) == 2 and auth_header_list[0] == 'Bearer':
                auth_token = auth_header_list[1]
        else:
            status = 403
            result = {
                'status': 'fail',
                'errorCode': 'authorization.header.missing',
                'message': ''
            }
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                result = {
                    'status': 'success',
                    'data': UserParser.parse_user(user)
                }
            else:
                status = 401
                result = {
                    'status': 'fail',
                    'message': resp
                }
        else:
            status = 401
            result = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
        return result, status
