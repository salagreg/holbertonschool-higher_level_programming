-- Crée une base de données dans le serveur
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- Crée une table avec un id unique, généré automatiquement et une colonne name ne pouvant pas être nulle.
CREATE TABLE IF NOT EXISTS states (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(256) NOT NULL
);
