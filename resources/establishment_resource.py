from flask_restful import Resource
from parsers.establishment_parser import EstablishmentParser


class EstablishmentResource(Resource):
    def get(self, id):
        from app.models import Establishment
        result = {}
        status = 200
        try:
            establishment = Establishment.query.filter_by(id=id).first()
        except Exception as e:
            status = 500
            result['error'] = str(e)
        else:
            if establishment is not None:
                result = EstablishmentParser.parseEstablishment(establishment)
            else:
                status = 404
                result['error'] = 'Establishment not found'
        finally:
            return result, status
