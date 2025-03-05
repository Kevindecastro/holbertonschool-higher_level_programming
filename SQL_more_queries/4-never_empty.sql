-- Crée une table `id_not_null` où la colonne `id` ne peut pas être NULL
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
