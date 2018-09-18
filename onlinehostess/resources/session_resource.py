import uuid

from flask_restful import Resource, reqparse


class SessionResource(Resource):
    __parser = None

    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('user_type',
                                   required=True,
                                   help='user_type can not be converted',
                                   location='args')

    def get(self):
        from app.models import Session
        user_type_map = {
            'user': True,
            'admin': True,
            '__secret__': True
        }
        result = {}
        status = 200
        args = self.__parser.parse_args()

        try:
            user_type = args['user_type']
        except Exception as e:
            print(e)
            result['error'] = str(e)
            status = 500
        else:
            if user_type_map.get(user_type) is not None:
                session_uuid = str(uuid.uuid4())
                session = Session(uuid=session_uuid, user_type=user_type)
                session.save()
                result['token'] = session_uuid
            else:
                status = 400
                result['error'] = 'Unknown user_type'
        finally:
            return result, status
