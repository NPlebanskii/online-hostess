from flask_restful import Resource
from flask import request
from parsers.user_parser import UserParser


class UserResource(Resource):
    def get(self):
        from app.models import User
        status = 200
        try:
            # get the auth token
            auth_header = request.headers.get('Authorization')
            # check if user already exists
            auth_token = ''
            if auth_header:
                authHeaderList = auth_header.split(" ")
                if len(authHeaderList) == 2 and authHeaderList[0] == 'Bearer':
                    auth_token = authHeaderList[1]
            if auth_token:
                resp = User.decode_auth_token(auth_token)
                if not isinstance(resp, str):
                    user = User.query.filter_by(id=resp).first()
                    result = {
                        'status': 'success',
                        'data': UserParser.parseUser(user)
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
        except Exception as e:
            result = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            status = 500
        finally:
            return result, status
