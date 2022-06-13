from flask_restful import Api
from app import app
from controllers import *

restServer = Api(app)
