-- Crée une seconde table dans une base de données
CREATE TABLE IF NOT EXISTS second_table (
  id INT,
  name VARCHAR(256),
  score INT
);
-- Insère des valeurs dans une seconde table dans une base de données
INSERT INTO second_table (id, name, score)
VALUES
(1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);
