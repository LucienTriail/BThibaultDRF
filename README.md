Installation:

Créer un fichier `.env` dans BinhDRF sur le modèle de `.env-example`.
Créer un environnement virtuel en lançant la commande `virtualenv venv` à la racine du projet.
Executer `pip install -r requirements.txt`.
Lancer ` python manage.py makemigrations` puis `python manage.py migrate`.
Remplir la table produits.
Ne surtout pas remplir la table transactions manuellement sinon Postgres aura un conflit de clefs primaires lors des bulk insertions.