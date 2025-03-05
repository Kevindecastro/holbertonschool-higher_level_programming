-- Créer une base de données si elle n'existe pas
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Créer un utilisateur s'il n'existe pas
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Accorder uniquement le privilège Select
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- Appliquer les changements
FLUSH PRIVILEGES;
