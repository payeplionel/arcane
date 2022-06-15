from flask_restful import Resource
import logging as logger
from config.config import mysql
from flask import jsonify
from flask import request


class ProprietaireByID(Resource):
    """
    Classe pour la gestion des ressources liée aux proprietés
    """

    def get(self, id_proprietaire):
        """
        Connaitre un proprietaire grâce à son identifiant
        :param id_proprietaire: identifiant du proprietaire
        :return: un proprietaire d'un bien si trouvé
        """
        logger.debug("get method")
        try:
            connection = mysql.connect()
            cursor = connection.cursor()
            sqlQuery = 'SELECT * FROM proprietaire where  proprietaireID = %s'
            data = id_proprietaire
            cursor.execute(sqlQuery, data)
            rows = cursor.fetchall()
            if len(rows) > 0:
                response = jsonify(rows)
            else:
                response = jsonify('Aucun utilisateur')
            response.status_code = 200
            return response
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            connection.close()

    def put(self, id_proprietaire):
        """
        verbe permettant de mettre à jour un proprietaire
        :param id_proprietaire: identifiant du proprietaire
        :return: Message de retour
        """
        logger.debug("Update d'un proprietaire")
        proprietaire = proprietaire_by_id(id_proprietaire)
        if not len(proprietaire) > 0:
            return jsonify('not exist')
        else:
            try:
                _json = request.json
                if _json.get('nom') is not None:
                    proprietaire['nom'] = _json.get('nom')
                if _json.get('prenom') is not None:
                    proprietaire['prenom'] = _json.get('prenom')
                if _json.get('date') is not None:
                    proprietaire['date'] = _json.get('date')
                if request.method == 'PUT':
                    connection = mysql.connect()
                    cursor = connection.cursor()
                    sqlQuery = 'Update Proprietaire Set nom  = %s, prenom = %s, date_naissance = %s ' \
                               'where proprietaireID = %s'
                    data = (proprietaire['nom'], proprietaire['prenom'], proprietaire['date'], id_proprietaire)
                    cursor.execute(sqlQuery, data)
                    connection.commit()
                    response = jsonify('Profil modifié')
                    response.status_code = 200
                    return response
                else:
                    return jsonify('error')
            except Exception as e:
                print(e)


def proprietaire_by_id(identifiant):
    """
    Avoir les informations sur un proprietaire
    :param identifiant: identifiant du proprietaire
    :return: un dictionnaire avec les informations du proprietaire
    """
    try:
        connection = mysql.connect()
        cursor = connection.cursor()
        sqlQuery = 'SELECT * FROM proprietaire p where p.proprietaireID = %s'
        data = identifiant
        cursor.execute(sqlQuery, data)
        rows = cursor.fetchone()
        if rows is not None:
            return {"nom": rows.__getitem__(1), "prenom": rows.__getitem__(2), "date": rows.__getitem__(3)}
        else:
            return {}
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
