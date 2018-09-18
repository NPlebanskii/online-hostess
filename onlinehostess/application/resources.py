from flask import request
from flask_jwt_extended import jwt_required, create_access_token, \
    get_jwt_identity
from flask_restful import Resource

from application import app_bcrypt
from application.core import get_user, get_establishment, get_establishments, \
    get_table
from parsers.establishment_parser import EstablishmentParser
from parsers.table_parser import TableParser
from parsers.user_parser import UserParser


class EstablishmentResource(Resource):
    @jwt_required
    def get(self, id):
        establishment = get_establishment(id=id)
        if establishment is not None:
            status = 200
            result = EstablishmentParser.parse_establishment(establishment)
        else:
            status = 404
            result = {
                'error': f"Establishment with id {id} not found."
            }
        return result, status


class EstablishmentsResource(Resource):
    @jwt_required
    def get(self):
        result = {}
        status = 200
        try:
            establishments = EstablishmentParser.parse_establishments(
                get_establishments())
        except Exception as e:
            status = 500
            result['error'] = str(e)
        else:
            if establishments is not None:
                result['establishments'] = establishments
            else:
                status = 404
                result['error'] = "Establishments not found."
        finally:
            return result, status


class LoginResource(Resource):
    def post(self):
        status = 200
        # get the post data
        post_data = request.get_json(force=True)
        # check if user already exists
        email = post_data.get('email')
        user = get_user(email=email)
        if not user:
            status = 404
            result = {
                'status': 'fail',
                'message': f"User with email {email} does not exist."
            }
        else:
            if app_bcrypt.check_password_hash(
                user.password, post_data.get('password')
            ):
                result = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'auth_token': create_access_token(identity=email)
                }
            else:
                status = 403
                result = {
                    'status': 'fail',
                    'message': 'Check your credentials.'
                }
        return result, status


class RegisterResource(Resource):
    def post(self):
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


class TableResource(Resource):
    @jwt_required
    def get(self, id):
        table = get_table(id=id)
        if table is not None:
            status = 200
            result = {
                'table': TableParser.parse_table(table)
            }
        else:
            status = 404
            result = {
                'error': f"Table with id {id} was not found."
            }
        return result, status


class UserResource(Resource):
    @jwt_required
    def get(self):
        email = get_jwt_identity()
        user = get_user(email=email)
        status = 200
        result = {
            'status': 'success',
            'data': UserParser.parse_user(user)
        }
        return result, status
