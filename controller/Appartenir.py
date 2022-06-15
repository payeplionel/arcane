from flask_restful import Resource
import logging as logger
from config.config import mysql
from flask import jsonify
from flask import request


class Appartenir(Resource):
    """
    Classe pour la gestion des appartenances à un bien
    """

    def put(self, proprietaireid, immobilierid):
        """
        Mise à jour des données d'un bien immobilier
        :param proprietaireid: identifiant du proprietaire
        :param immobilierid: identifiant du bien immobilier
        :return: Notification
        """
        logger.debug("Modification d'un bien")
        immobilier = proprietaire_by_bien(proprietaireid, immobilierid)
        if len(immobilier) > 0:
            try:
                _json = request.json
                if _json.get('nom') is not None:
                    immobilier['nom'] = _json.get('nom')
                if _json.get('ville') is not None:
                    immobilier['ville'] = _json.get('ville')
                if _json.get('description') is not None:
                    immobilier['description'] = _json.get('description')
                if _json.get('type') is not None:
                    immobilier['type'] = _json.get('type')
                if _json.get('pieces') is not None:
                    immobilier['pieces'] = _json.get('pieces')
                if _json.get('caracteristique') is not None:
                    immobilier['caracteristique'] = _json.get('caracteristique')

                if request.method == 'PUT':
                    connection = mysql.connect()
                    cursor = connection.cursor()
                    sqlQuery = "Update Immobilier Set nom  = %s, ville = %s, descriptionImo = %s, typeImo = %s, " \
                               "pieces = %s, caracteristique =  %s where immobilierID = %s"
                    data = (immobilier['nom'], immobilier['ville'], immobilier['description'], immobilier['type'],
                            immobilier['pieces'], immobilier['caracteristique'], immobilierid)
                    cursor.execute(sqlQuery, data)
                    connection.commit()
                    response = jsonify('Bien modifié')
                    response.status_code = 200
                    return response
                else:
                    return jsonify('error')
            except Exception as e:
                print(e)
        else:
            return jsonify('Vous n\'avez pas le droit de modifier ce bien')


def proprietaire_by_bien(idP, idM):
    """
    Vérification si un bien appartient à un proprietaire
    :param idP: identifiant du proprietaire
    :param idM: identifiant de l'immobilier
    :return: un dictionnaire avec les informations du bien
    """
    try:
        connection = mysql.connect()
        cursor = connection.cursor()
        sqlQuery = 'SELECT * FROM Appartenir a where a.immobilierID = %s and a.proprietaireID = %s'
        data = (idP, idM)
        cursor.execute(sqlQuery, data)
        rows = cursor.fetchone()
        if rows is not None:
            sqlQuery = 'SELECT * FROM Immobilier i where i.immobilierID = %s'
            data = idM
            cursor.execute(sqlQuery, data)
            rows = cursor.fetchone()
            return {"nom": rows.__getitem__(1), "ville": rows.__getitem__(2), "description": rows.__getitem__(3),
                    "type": rows.__getitem__(4), "pieces": rows.__getitem__(5), "caracteristique": rows.__getitem__(6)}
        else:
            return {}
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
