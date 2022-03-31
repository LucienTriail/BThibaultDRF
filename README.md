Installation:

Importer le dump.sql fourni avec le projet dans une base Postgresql 14.
Définir les identifiants de connexion dans settings.DATABASE.
Créer un environnement virtuel en lançant la commande `virtualenv venv` à la racine du projet.
Executer `pip install -r requirements.txt`.
Lancer ` python manage.py makemigrations` puis `python manage.py migrate`.
Remplir la table produits.
Ne surtout pas remplir la table transactions manuellement sinon Postgres aura un conflit de clefs primaires lors des bulk insertions.