-- Sélectionne le score et le nom des enregistrements dans la table second_table
-- Ne garde que les enregistrements où la colonne name n'est pas vide (c'est-à-dire où elle contient une valeur)
-- Trie les résultats par score décroissant (du plus grand au plus petit)
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
