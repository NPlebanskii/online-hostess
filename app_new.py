from flask import Flask, render_template, Markup
from flask_restful import Resource, Api, reqparse
from data_base_processor import *
import uuid, pdb
import sqlite3 as sql
from table_types import TableType

app = Flask(__name__)
api = Api(app)

class SessionResource(Resource):
	__parser = None
	def __init__(self):
		self.__parser = reqparse.RequestParser()
		self.__parser.add_argument('user_type', required = True, help = 'user_type can not be converted', location='args')

	def get(self):
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
				result['token'] = str(uuid.uuid4())
			else:
				status = 400
				result['error'] = 'Unknown user_type'
		finally:
			return result, status

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

class TablesResource(Resource):
	__dbp = DataBaseProcessor()
	def get(self):
		result = {}
		status = 200
		try:
			rows = self.__dbp.read_all_rows_from_table(TableType.TABLE)
		except Exception as e:
			status = 500
			result['error'] = str(e)
		else:
			if not (rows is None):
				result['tables'] = rows
			else:
				status = 404
				result['error'] = "Tables not found"
		finally:
			return result, status

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

class EstablishmentResource(Resource):
	__dbp = DataBaseProcessor()
	__parser = None
	def __init__(self):
		self.__parser = reqparse.RequestParser()
		self.__parser.add_argument('recipient_name', required = True, help = 'recipient_name can not be converted', location='args')
		self.__parser.add_argument('recipient-surname', location='args')
		self.__parser.add_argument('email', required = True, help = 'email can not be converted', location='args')
		self.__parser.add_argument('comment', location='args')
		self.__parser.add_argument('table-id', required = True, help = 'table-id can not be converted', location='args')

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

	def put(self, id):
		result = {}
		table = None
		status = 200
		order = self.__parser.parse_args()
		try:
			self.__dbp.update_table_status(order['table-id'], 'reserved', order['email'])
			table = self.__dbp.read_row_from_table_by_id(TableType.TABLE, order['table-id'])
		except Exception as e:
			status = 500
			result['error'] = str(e)
		else:
			if table is None:
				status = 404
				result['error'] = 'Table was not found.'
			else:
				result['table'] = table
		finally:
			return result, status

api.add_resource(SessionResource, '/api/v0/session')
api.add_resource(TableResource, '/api/v0/tables/<table_id>')
api.add_resource(TablesResource, '/api/v0/tables')
api.add_resource(EstablishmentsResource, '/api/v0/establishments')
api.add_resource(EstablishmentResource, '/api/v0/establishments/<id>')

if __name__ == '__main__':
	app.run(debug=True)