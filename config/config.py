from app import app
from flaskext.mysql import MySQL

"""
Configuration de la liaison à la base de données
"""
mysql = MySQL()
# Nom d'utolisateur de la base de données
app.config['MYSQL_DATABASE_USER'] = 'root'
# Mot de passe de l'utilisateur
app.config['MYSQL_DATABASE_PASSWORD'] = 'lionel'
# Nom de la base de données
app.config['MYSQL_DATABASE_DB'] = 'arcane'
# Localisation
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# Chargement des paramètres dans l'application
mysql.init_app(app)
