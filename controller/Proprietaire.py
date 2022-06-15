from flask_restful import Resource
import logging as logger
from config.config import mysql
from flask import jsonify
from flask import request


class Proprietaire(Resource):

    def post(self):
        """
        verbe pour la création d'un nouveau proprietaire d'un bien
        :return: une notification
        """
        logger.debug("Creation d'un proprietaire")
        try:
            _json = request.json
            _nom = _json['nom']
            _prenom = _json['prenom']
            _date = _json['date']
            if len(_nom) > 0 and len(_prenom) > 0 and len(_date) > 0 and request.method == 'POST':
                connection = mysql.connect()
                cursor = connection.cursor()
                sqlQuery = 'INSERT INTO Proprietaire (nom, prenom, date_naissance) VALUES(%s, %s, %s)'
                data = (_nom, _prenom, _date)
                cursor.execute(sqlQuery, data)
                connection.commit()
                response = jsonify('Profil crée')
                response.status_code = 201
                return response
            else:
                response = jsonify('error')
                response.status_code = 403
                return response
        except Exception as e:
            print(e)
