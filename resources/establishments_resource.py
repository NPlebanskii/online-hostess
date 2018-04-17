from flask_restful import Resource
from parsers.establishment_parser import EstablishmentParser


class EstablishmentsResource(Resource):
    @jwt_required()
    def get(self):
        from app.models import Establishment
        result = {}
        status = 200
        try:
            establishments = EstablishmentParser.parseEstablishments(
                Establishment.get_all())
        except Exception as e:
            status = 500
            result['error'] = str(e)
        else:
            if not (establishments is None):
                result['establishments'] = establishments
            else:
                status = 404
                result['error'] = "Establishments not found."
        finally:
            return result, status
