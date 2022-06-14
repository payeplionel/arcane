from app import app
from flaskext.mysql import MySQL
"""
Configuration de la liaison à la base de données
"""
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'lionel'
app.config['MYSQL_DATABASE_DB'] = 'arcane'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
