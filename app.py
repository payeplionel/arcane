from flask import Flask
#from flask_cors import CORS, cross_origin
import logging as logger
logger.basicConfig(level="DEBUG")

app = Flask(__name__)
#CORS(app)

if __name__ == '__main__':
    logger.debug("Starting the application")
    from api import *
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=True)