from flask_restful import Api
from app import app
from api.models import *

restServer = Api(app)
restServer.add_resource(immobilier, '/immobilier')
restServer.add_resource(proprietaire, '/proprietaire')
