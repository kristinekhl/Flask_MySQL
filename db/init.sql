create database geography;
use geography;
CREATE TABLE countries (
nation VARCHAR(50),
capital VARCHAR(50),
population VARCHAR(50),
area VARCHAR(50)
);
INSERT INTO countries
(nation, capital, population, area)
VALUES
('Germany', 'Berlin', '3,769,495', '891,8 km²'),
('France', 'Paris', '2,165,423', '105,4 km²');