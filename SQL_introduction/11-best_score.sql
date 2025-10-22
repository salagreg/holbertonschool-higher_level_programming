-- Liste les enregistrements d'une table avec score >= 10 dans une base de données
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
