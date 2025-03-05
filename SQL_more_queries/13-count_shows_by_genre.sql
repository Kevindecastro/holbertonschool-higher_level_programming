-- Sélectionne le nom du genre et le nombre d'émissions liées à ce genre
SELECT g.name AS genre, COUNT(s.id) AS number_of_shows
FROM tv_genres g

-- Jointure avec la table de liaison `tv_show_genres` pour associer chaque genre à ses émissions
JOIN tv_show_genres tsg ON g.id = tsg.genre_id

-- Jointure avec la table `tv_show` pour s'assurer qu'on compte bien les émissions existantes
JOIN tv_show s ON tsg.tv_show_id = s.id

-- Regroupe les résultats par genre pour compter combien d'émissions sont associées à chaque genre
GROUP BY g.name

-- Exclut les genres qui n'ont pas d'émissions associées
HAVING COUNT(s.id) > 0

-- Trie les résultats par ordre décroissant du nombre d'émissions par genre
ORDER BY number_of_shows DESC;
