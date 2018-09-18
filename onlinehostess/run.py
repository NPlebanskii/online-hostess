from flask_restful import Api

from application import app
from application.resources import EstablishmentResource, UserResource, \
    EstablishmentsResource, LoginResource, RegisterResource, TableResource

api = Api(app)
api.add_resource(TableResource, '/api/v1/tables/<id>')
api.add_resource(EstablishmentsResource, '/api/v1/establishments')
api.add_resource(EstablishmentResource, '/api/v1/establishments/<id>')
api.add_resource(RegisterResource, '/api/v1/register')
api.add_resource(LoginResource, '/api/v1/login')
api.add_resource(UserResource, '/api/v1/user')


if __name__ == '__main__':
    app.run()
