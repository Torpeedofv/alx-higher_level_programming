-- creates a table on mysql server
CREATE TABLE IF NOT EXISTS unique_id (id int DEFAULT 1, name VARCHAR(256), UNIQUE (id));
