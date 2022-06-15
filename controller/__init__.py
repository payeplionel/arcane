from flask_restful import Api
from app import app
from controller.Immobilier import *
from controller.Appartenir import *
from controller.Proprietaire import *

"""
Configuration des ressources misent à la disposition du client
"""

restServer = Api(app)
restServer.add_resource(Immobilier, '/immobilier/<string:ville>')
restServer.add_resource(Proprietaire, '/proprietaire/<int:id>')
restServer.add_resource(Appartenir, '/appartenir/<proprietaireid>/<immobilierid>')

