﻿# Arcane
## Préparation de l'environnement de travail
### Environnement
<ol> 
  <li> Création du dossier pour le projet : mkdir  <i> nom du dossier </i> </li>
  <li> Accéder au dossier : cd  <i> nom du dossier </i> </li>
</ol>

### Installation des paquets 
<ul> 
  <li> Installation du framework Flask : <b> pip install flask </b> </li> </br>
  
  ![plot](./images/a1.png)
  
   <li> Installation de l'environnement virtuel pour encloisoner les dépendances du projet  : <b> pip install virtualenv </b> -> <b> virtualenv venv </b> </li> </br>
  
  ![plot](./images/a1.png)
  
   <li> Activation de l'environnement : <b> venv/Scripts/activate </b> </li> </br>
  
  ![plot](./images/a1.png)
  
  <li> Installation de MySQL pour la gestion de la base de données : <b> pip install flask-mysql </b> </li> </br>
  
   ![plot](./images/a2.png)
   
    <li> Installation de fask restful : qui permet la création rapide des services rest <b> pip install flask-restful </b> </li> </br>
  
   ![plot](./images/a2.png)
  
  <li> Installation CORS pour le partage des ressources entre les domaines : <b> pip install cors </b> </li>
  
   ![plot](./images/a3.png)
  
</ul>

### Conception 
<b> Modèle Conceptuel de données </b>

![plot](./images/mcd.png)

<section> 
  <ul><b> Notes :  </b>
    <li> Un proprietaire peut posséder 1 ou plusieurs biens immobiliers </li>
    <li> Un bien immobilier peut appartenir à aucun, un ou plusieurs proprétaires </li>
  </ul>
</section>

<b> Modèle Logique de données </b>

![plot](./images/mld.png)

<b> Diagramme de classe </b>
*****

### Architecture du projet 
*******

### Base de données :
<ol> 
  <li> Table immobilier </li>
  *****
  <li> Table proprietaire </li>
  *****
   <li> Table appartenir </li>
  *****
</ol>  

>>>>>>> 2ba5dfc (Update README.md)
