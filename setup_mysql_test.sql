-- Create the database to do the tests
-- Create the user with privileges

CREATE DATABASE IF NOT exists hbnb_test_db;

USE hbnb_test_db;

CREATE USER IF NOT exists hbnb_test@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
