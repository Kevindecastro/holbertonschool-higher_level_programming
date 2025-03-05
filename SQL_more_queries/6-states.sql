-- Crée une base de données `hbtn_0d_usa` et une table `states`.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Passer à la base de données hbtn_0d_usa
USE hbtn_0d_usa;

-- Créer des états de table s'ils n'existent pas
-- Définir l'ID sur l'incrémentation automatique et la clé primaire
-- Définir le nom sur non nul
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
