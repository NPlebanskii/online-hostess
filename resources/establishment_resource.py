from flask_restful import Resource
from parsers.establishment_parser import EstablishmentParser


class EstablishmentResource(Resource):
    def get(self, id):
        from app.models import Establishment
        result = {}
        tables = {}
        status = 200
        try:
            result = EstablishmentParser.parseEstablishment(
                Establishment.query.filter_by(id=id).first())
            tables = {}
        except Exception as e:
            status = 500
            result['error'] = str(e)
        else:
            # if tables is None:
                # status = 404
                # result['error'] = 'Tables not found'
            # else:
                result['tables'] = tables
        finally:
            return result, status
