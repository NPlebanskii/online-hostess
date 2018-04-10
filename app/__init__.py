from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from resources.establishment_resource import EstablishmentResource
from resources.establishments_resource import EstablishmentsResource
from resources.session_resource import SessionResource
from resources.table_resource import TableResource
from resources.tables_resource import TablesResource
from instance.config import app_config

db = SQLAlchemy()


def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	api = Api(app)
	api.add_resource(SessionResource, '/api/v0/session')
	api.add_resource(TableResource, '/api/v0/tables/<table_id>')
	api.add_resource(TablesResource, '/api/v0/tables')
	api.add_resource(EstablishmentsResource, '/api/v0/establishments')
	api.add_resource(EstablishmentResource, '/api/v0/establishments/<id>')
	
	db.init_app(app)

	return app