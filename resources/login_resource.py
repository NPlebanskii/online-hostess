from flask_restful import Resource
from flask import request


class LoginResource(Resource):
    def post(self):
        from app.models import User
        from app import app_bcrypt
        status = 200
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
                status = 404
                result = {
                    'status': 'fail',
                    'message': 'User does not exist.'
                }
            else:
                if app_bcrypt.check_password_hash(
                    user.password, post_data.get('password')
                ):
                    auth_token = user.encode_auth_token(user.id)
                    result = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token.decode()
                    }
                else:
                    status = 403
                    result = {
                        'status': 'fail',
                        'message': 'Check your credentials.'
                    }
        finally:
            return result, status
