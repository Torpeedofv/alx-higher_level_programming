-- lists all records with a score or higher in the table of the database in mysql
SELECT name, score FROM second_table WHERE score >= 10 ORDER BY score DESC;
