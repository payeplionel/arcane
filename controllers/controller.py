import pymysql
from app import app
from config.config import mysql
from flask import jsonify
from flask import flash, request
import logging as logger
logger.basicConfig(level="DEBUG")

@app.route('/create', methods=['POST'])
def create_immobilier():
    try:
        _json = request.json
        _nom = _json['nom']
        _description = _json['description']
        _type = _json['type']
        _piece = _json['piece']
        _carac = _json['caracteristique']
        _proprietes = _json['proprietes']
        if _nom and _description and _type and _piece and _carac and _proprietes and request.method == 'POST':
            connection = mysql.connect()
            cursor = connection.cursor(pymysql.cursors.DistCursor)
            sqlQuery = "INSERT INTO immobilier(nom, descriptionImo, typeImo, pieces, caracteristique, proprietaire) VALUES(%s, %s, %s, %s, %s, %s)"
            data = (_nom, _description, _type, _piece, _carac, _proprietes)
            cursor.execute(sqlQuery,data)
            connection.commit()
            response = jsonify('added')
            response.status_code = 200
            return response
        else:
            return jsonify('error')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

@app.route('/list')
def list_immo():
    try:
        connection = mysql.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM immobilier")
        print(cursor)
        immoRows = cursor.fetchall()
        response = jsonify(immoRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
