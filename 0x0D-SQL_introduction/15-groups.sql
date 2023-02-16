-- list the number of records with the same score in the table in mysql
SELECT score, COUNT(*) FROM second_table GROUP BY score;
