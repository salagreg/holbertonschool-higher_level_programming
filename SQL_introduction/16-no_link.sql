-- Liste tous les enregsitrements d'une table avec un nom non NULL dans une base de données
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
