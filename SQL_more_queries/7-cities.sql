-- Crée une table `cities` liée à la table `states` via une clé étrangère.
-- Crée une base de données `hbtn_0d_usa` et une table `states`.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Passer à la base de données hbtn_0d_usa
USE hbtn_0d_usa;

-- Create Table cities if it doesn't exist
-- Set id to auto increment and primary key
-- Set state_id to not null and foreign key
-- Set name to not null
CREATE TABLE IF NOT EXISTS cities (
  id INT AUTO_INCREMENT PRIMARY KEY,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  FOREIGN KEY (state_id) REFERENCES states(id)
);
