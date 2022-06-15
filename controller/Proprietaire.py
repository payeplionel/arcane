from flask_restful import Resource
import logging as logger
from config.config import mysql
from flask import jsonify
from flask import request


class Proprietaire(Resource):
    """
    Classe pour la gestion des ressources liée aux proprietés
    """
    def get(self, id):
        """
        Connaitre un proprietaire grâce à son identifiant
        :param id: identifiant du proprietaire
        :return: un proprietaire d'un bien si trouvé
        """
        logger.debug("Inside get method")
        try:
            connection = mysql.connect()
            cursor = connection.cursor()
            sqlQuery = "SELECT * FROM proprietaire where  proprietaireID = %s"
            data = id
            cursor.execute(sqlQuery, data)
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
            if _nom and _prenom and _date and request.method == 'POST':
                connection = mysql.connect()
                cursor = connection.cursor()
                sqlQuery = "INSERT INTO Proprietaire (nom, prenom, date_naissance) VALUES(%s, %s, %s)"
                data = (_nom, _prenom, _date)
                cursor.execute(sqlQuery, data)
                connection.commit()
                response = jsonify('Profil crée')
                response.status_code = 200
                return response
            else:
                return jsonify('error')
        except Exception as e:
            print(e)

    def put(self, id):
        """
        verbe permettant de mettre à jour un proprietaire
        :param id: identifiant du proprietaire
        :return: Message de retour
        """
        logger.debug("Update d'un proprietaire")
        proprietaire = proprietaire_by_id(id)
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
                    sqlQuery = "Update Proprietaire Set nom  = %s, prenom = %s, date_naissance = %s"
                    data = (proprietaire['nom'], proprietaire['prenom'], proprietaire['date'])
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