from flask_restful import Resource, reqparse
import uuid


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
        userTypeMap = {
            'user': True,
            'admin': True,
            '__secret__': True
        }
        result = {}
        status = 200
        args = self.__parser.parse_args()

        try:
            userType = args['user_type']
        except Exception as e:
            print(e)
            result['error'] = str(e)
            status = 500
        else:
            if not (userTypeMap.get(userType) is None):
                sessionUuid = str(uuid.uuid4())
                session = Session(uuid=sessionUuid, user_type=userType)
                session.save()
                result['token'] = sessionUuid
            else:
                status = 400
                result['error'] = 'Unknown user_type'
        finally:
            return result, status
