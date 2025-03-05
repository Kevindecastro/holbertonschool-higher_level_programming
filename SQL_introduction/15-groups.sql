-- Sélectionne le score et le nombre d'enregistrements pour chaque score dans la table second_table
-- Trie les résultats par nombre d'enregistrements, du plus grand au plus petit
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
