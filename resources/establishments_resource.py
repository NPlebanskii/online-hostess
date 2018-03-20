from data_base_processor import *
from table_types import TableType
from flask_restful import Resource

class EstablishmentsResource(Resource):
	__dbp = DataBaseProcessor()
	def get(self):
		result = {}
		status = 200
		try:
			rows = self.__dbp.read_all_rows_from_table(TableType.ESTABLISHMENT)
		except Exception as e:
			status = 500
			result['error'] = str(e)
		else:
			if not (rows is None):
				result['establishments'] = rows
			else:
				status = 404
				result['error'] = "Establishments not found."
		finally:
			return result, status
