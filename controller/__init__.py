from flask_restful import Api
from app import app
from controller.Immobilier import *
from controller.Appartenir import *
from controller.Proprietaire import *
from controller.ProprietaireByID import *
from controller.ImmobilierByCity import *

"""
Configuration des ressources misent à la disposition du client
"""

# Création d'une application rest sur notre application
restServer = Api(app)

# Mise à la disposition des ressources à travers les end points
restServer.add_resource(ImmobilierByCity, '/immobilier/<string:ville>')
restServer.add_resource(Immobilier, '/immobilier/<int:id_proprietaire>')
restServer.add_resource(Proprietaire, '/proprietaire')
restServer.add_resource(ProprietaireByID, '/proprietaire/<int:id_proprietaire>')
restServer.add_resource(Appartenir, '/appartenir/<proprietaireid>/<immobilierid>')

