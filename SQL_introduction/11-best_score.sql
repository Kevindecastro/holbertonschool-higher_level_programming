-- Sélectionner les colonnes score et name de la table second_table
-- Ne garde que les enregistrements avec un score >= 10
-- Trient les résultats par score décroissant (du plus grand au plus petit)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
