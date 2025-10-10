### Documentation API - Requests

# La différence entre HTTP et HTTPS :

HTTP est un protocole de communication utilisé pour transférer des données entre un client et un serveur.
HTTP utilise le port 80.

HTTPS est tout simplement la version sécurisée de HTTP, qui ajoute une couche de chiffrement aux échanges.
Essentiel pour les sites manipulant des données sensibles : identifiants, cartes bancaires, données personnelles.
HTTPS utilise le port 443.

# Quatres méthodes HTTP :
- GET pour récupérer une ressource --> Charger une page ou des données.
- POST pour envoyer des données au serveur --> Soumettre un formulaire.
- PUT pour remplacer complétement une ressource --> Mettre à jour un profil.
- DELETE pour supprimer une ressource --> Supprimer un compte.

# Codes d'état HTTP courants :
- 200 qui signifie un Succès lorsque qu'une requête GET est réussie.
- 400 qui signifie Mauvaise requête lorsqu'il y a des données mal formées envoyées au serveur.
- 404 qui signifie qu'une ressource n'a pas été trouvée car l'URL est inexistante.
- 403 qui signifie Accès refusé lorsqu'un utilisateur n'a pas les droits.
- 500 qui signifie Erreur du serveur lorsque qu'il y a un problème du serveur.


