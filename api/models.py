from flask_restful import Resource
import logging as logger
from config.config import mysql
from flask import jsonify
from flask import request
import json


class Immobilier(Resource):
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

    def post(self):
        logger.debug("Inside post method")
        return {"message": "inside post method"}, 200


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