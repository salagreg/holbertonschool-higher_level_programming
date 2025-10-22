-- Crée une table dans la base de données avec uniquement 1 par défaut pour la colonne id.
CREATE TABLE IF NOT EXISTS unique_id (
  id INT UNIQUE DEFAULT 1,
  name VARCHAR(256)
);
