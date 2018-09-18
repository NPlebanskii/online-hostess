from flask_restful import Resource
# from flask-JWT
from parsers.establishment_parser import EstablishmentParser


class EstablishmentsResource(Resource):
    # @jwt_required()
    def get(self):
        from app.models import Establishment
        result = {}
        status = 200
        try:
            establishments = EstablishmentParser.parse_establishments(
                Establishment.get_all())
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
