from flask_restful import Resource
from parsers.table_parser import TableParser


class TableResource(Resource):
    def get(self, table_id):
        from app.models import Table
        result = {}
        status = 200
        try:
            table = Table.query.filter_by(id=table_id).first()
        except Exception as e:
            status = 500
            result['error'] = str(e)
        else:
            if table is not None:
                result['table'] = TableParser.parse_table(table)
            else:
                status = 404
                result['error'] = 'Not found'
        finally:
            return result, status
