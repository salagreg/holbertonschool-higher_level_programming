-- Liste le nombre d'enregistrements avec le même score dans une table d'une base de données
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
