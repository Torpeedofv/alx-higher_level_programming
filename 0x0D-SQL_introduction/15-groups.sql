-- list the number of records with the same score in the table in mysql
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score DESC;
