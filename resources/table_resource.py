from data_base_processor import *
from table_types import TableType
from flask_restful import Resource

class TableResource(Resource):
	__dbp = DataBaseProcessor()
	def get(self, table_id):
		result = {}
		status = 200
		try:
			row = self.__dbp.read_row_from_table_by_id(TableType.TABLE, table_id)
		except Exception as e:
			status = 500
			result['error'] = str(e)
		else:
			if not row is None:
				result['table'] = row
			else:
				status = 404
				result['error'] = "Not found table with id " + table_id
		finally:
			return result, status
