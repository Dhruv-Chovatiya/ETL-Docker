CREATE DATABASE etl_db;

USE etl_db;

CREATE TABLE people (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    city VARCHAR(100)
);