from flask_restful import Api
from app import app
from api.models import *

"""
Configuration des ressources misent à la disposition du client
"""

restServer = Api(app)
restServer.add_resource(Immobilier, '/immobilier/<string:ville>')
restServer.add_resource(Proprietaire, '/proprietaire/<int:id>')
restServer.add_resource(Appartenir, '/appartenir/<proprietaireid>/<immobilierid>')

