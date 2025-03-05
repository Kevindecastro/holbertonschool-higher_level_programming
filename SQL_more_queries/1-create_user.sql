-- Vérifier si l'utilisateur 'user_0d_1' existe déjà et le créer si ce n'est pas le cas
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Accorder tous les privilèges sur toutes les bases de données à 'user_0d_1'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Appliquer les changements
FLUSH PRIVILEGES;
