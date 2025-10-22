-- Crée une base de données dans le serveur
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- Crée une table, avec un id généré automatiquement et une colonne name ne pouvant pas être nulle.
CREATE TABLE IF NOT EXISTS states (
  id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  name VARCHAR(256) NOT NULL
);

-- Crée une table cities avec un id généré automatiquement, une colonne name ne pouvant pas être nulle et une clé étrangère state_id référencant l'id de la table states.
CREATE TABLE IF NOT EXISTS cities (
  id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  FOREIGN KEY (state_id) REFERENCES states(id)
);
