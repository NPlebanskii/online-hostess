from flask import Flask
from flask_restful import Api

from resources.establishment_resource import EstablishmentResource
from resources.establishments_resource import EstablishmentsResource
from resources.session_resource import SessionResource
from resources.table_resource import TableResource
from resources.tables_resource import TablesResource


app = Flask(__name__)
api = Api(app)

api.add_resource(SessionResource, '/api/v0/session')
api.add_resource(TableResource, '/api/v0/tables/<table_id>')
api.add_resource(TablesResource, '/api/v0/tables')
api.add_resource(EstablishmentsResource, '/api/v0/establishments')
api.add_resource(EstablishmentResource, '/api/v0/establishments/<id>')

if __name__ == '__main__':
	app.run(debug=True)