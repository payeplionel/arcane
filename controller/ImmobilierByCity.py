from flask_restful import Resource
import logging as logger
from config.config import mysql
from flask import jsonify


class ImmobilierByCity(Resource):
    """
    Classe pour la gestion des biens immobiliers
    """
    def get(self, ville):
        """
        Liste les biens immobiliers d'une ville passée en paramètre
        :param ville: le nom de la ville recherchée
        :return: la liste des biens immobiliers de la ville
        """
        logger.debug("Recherche ...")
        try:
            connection = mysql.connect()
            cursor = connection.cursor()
            sqlQuery = "SELECT * FROM immobilier i where i.ville = %s"
            data = ville
            cursor.execute(sqlQuery, data)
            rows = cursor.fetchall()
            print(rows)
            response = jsonify(rows)
            response.status_code = 200
            if len(rows) > 0:
                return response
            else:
                return {"message": "Aucune ville trouvée"}
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            connection.close()
