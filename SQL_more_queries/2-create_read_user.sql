-- Crée une base de données dans le serveur
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Crée un utilisateur avec uniquement le privilège SELECT sur la base de données hbtn_0d_2.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
