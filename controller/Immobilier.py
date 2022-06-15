from flask_restful import Resource
import logging as logger
from config.config import mysql
from flask import jsonify
from flask import request
from controller.Appartenir import appartenance


class Immobilier(Resource):
    """
    Classe pour la gestion des biens immobiliers
    """

    def post(self, id_proprietaire):
        logger.debug("post method")
        """
               verbe pour la création d'un nouveau proprietaire d'un bien
               :return: une notification
               """
        logger.debug("Creation d'un proprietaire")
        try:
            _json = request.json
            _nom = _json['nom']
            _ville = _json['ville']
            _description = _json['description']
            _type = _json['type']
            _pieces = _json['pieces']
            _caracteristique = _json['caracteristique']
            if len(_nom) > 0 and len(_caracteristique) > 0 and len(_ville) > 0\
                    and len(_description) > 0 and len(_type) > 0 and len(_pieces) > 0 and request.method == 'POST':
                connection = mysql.connect()
                cursor = connection.cursor()
                sqlQuery = 'INSERT INTO Immobilier (nom, ville, descriptionImo, typeImo, pieces, caracteristique) ' \
                           'VALUES(%s, %s, %s, %s, %s, %s)'
                data = (_nom, _ville, _description, _type, _pieces, _caracteristique)
                cursor.execute(sqlQuery, data)
                connection.commit()
                sqlQuery = 'SELECT LAST_INSERT_ID();'
                cursor.execute(sqlQuery)
                rows = cursor.fetchone()
                appartenance(rows.__getitem__(0), id_proprietaire)
                response = jsonify('Bien crée')
                response.status_code = 201
                return response
            else:
                response = jsonify('error')
                response.status_code = 403
                return response
        except Exception as e:
            print(e)
