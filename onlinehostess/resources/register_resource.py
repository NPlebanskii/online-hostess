from flask import request
from flask_restful import Resource


class RegisterResource(Resource):
    def post(self):
        from app.models import User
        # get the post data
        post_data = request.get_json(force=True)
        # check if user already exists
        email = post_data.get('email')
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(
                email=email,
                password=post_data.get('password'),
                first_name=post_data.get('first_name'),
                last_name=post_data.get('last_name', ''),
                admin=post_data.get('admin', False)
            )
            user.save()
            result = {
                'status': 'success',
                'message': 'Successfully registered.'
            }
            status = 201
        else:
            result = {
                'status': 'fail',
                'errorCode': 'email.already.in.use',
                'message': (f"User with email {email} already exists. "
                            "Use different email.")
            }
            status = 400

        return result, status
