from flask_restful import Resource
from flask import request


class RegisterResource(Resource):
    def post(self):
        from app.models import User
        status = 201
        try:
            # get the post data
            post_data = request.get_json(force=True)
            # check if user already exists
            user = User.query.filter_by(email=post_data.get('email')).first()
        except Exception as e:
            result = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            status = 500
        else:
            if not user:
                user = User(
                    email=post_data.get('email'),
                    password=post_data.get('password'),
                    first_name=post_data.get('first_name'),
                    last_name=post_data.get('last_name', ''),
                    admin=post_data.get('admin', False)
                )
                user.save()
                # generate the auth token
                auth_token = user.encode_auth_token(user.id)
                result = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                    'auth_token': auth_token.decode()
                }
            else:
                result = {
                    'status': 'fail',
                    'message': 'User already exists. Please Log in.',
                }
                status = 202
        finally:
            return result, status
