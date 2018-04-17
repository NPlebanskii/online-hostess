from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from resources.establishment_resource import EstablishmentResource
from resources.establishments_resource import EstablishmentsResource
from resources.session_resource import SessionResource
from resources.table_resource import TableResource
from resources.register_resource import RegisterResource
from resources.login_resource import LoginResource
from resources.user_resource import UserResource
from instance.config import app_config

db = SQLAlchemy()
app_bcrypt = None


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    api = Api(app)
    api.add_resource(SessionResource, '/api/v0/session')
    api.add_resource(TableResource, '/api/v0/tables/<table_id>')
    api.add_resource(EstablishmentsResource, '/api/v0/establishments')
    api.add_resource(EstablishmentResource, '/api/v0/establishments/<id>')
    api.add_resource(RegisterResource, '/api/v0/register')
    api.add_resource(LoginResource, '/api/v0/login')
    api.add_resource(UserResource, '/api/v0/user')

    db.init_app(app)
    global app_bcrypt
    app_bcrypt = Bcrypt(app)

    return app
