from data_base_processor import *
from table_types import TableType
from flask_restful import Resource

class EstablishmentResource(Resource):
	__dbp = DataBaseProcessor()

	def get(self, id):
		result = {}
		status = 200
		try:
			tables = self.__dbp.read_establishment_tables(id)
		except Exception as e:
			status = 500
			result['error'] = str(e)
		else:
			if tables is None:
				status = 404
				result['error'] = 'Tables not found'
			else:
				result['tables'] = tables
		finally:
			return result, status
