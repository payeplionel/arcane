from flask_restful import Resource
import logging as logger
from config.config import mysql
from flask import jsonify

class immobilier(Resource):
    def get(self):
        logger.debug("Inside get method")
        try:
            connection = mysql.connect()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM immobilier")
            print(cursor)
            rows = cursor.fetchall()
            response = jsonify(rows)
            response.status_code = 200
            return response
        except Exception as e:
            print(e)

    def post(self):
        logger.debug("Inside post method")
        return {"message" : "inside post method"}, 200

    def put(self):
        logger.debug("Inside put method")
        return {"message" : "inside put method"}, 200

    def delete(self):
        logger.debug("Inside delete method")
        return {"message" : "inside delete method"}, 200

class proprietaire(Resource):
    def get(self):
        global cursor, connection
        logger.debug("Inside get method")
        try:
            connection = mysql.connect()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM proprietaire")
            print(cursor)
            rows = cursor.fetchall()
            response = jsonify(rows)
            response.status_code = 200
            return response
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            connection.close()

    def post(self):
        logger.debug("Inside post method")
        return {"message" : "inside post method"}, 200

    def put(self):
        logger.debug("Inside put method")
        return {"message" : "inside put method"}, 200

    def delete(self):
        logger.debug("Inside delete method")
        return {"message" : "inside delete method"}, 200
