-- Sélectionne le nom du genre et le nombre d'émissions liées à ce genre
SELECT g.name AS genre, COUNT(g.id) AS number_of_shows
FROM tv_genres g

-- Jointure avec la table de liaison `tv_show_genres` pour associer chaque genre à ses émissions
JOIN tv_show_genres tsg ON g.id = tsg.genre_id

-- Regroupe les résultats par genre pour compter combien d'émissions sont associées à chaque genre
GROUP BY g.id

-- Trie les résultats par ordre décroissant du nombre d'émissions par genre
ORDER BY number_of_shows DESC;
