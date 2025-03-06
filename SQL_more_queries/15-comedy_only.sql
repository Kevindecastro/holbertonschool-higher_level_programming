-- Sélectionne les titres des émissions de télévision
SELECT ts.title
FROM tv_shows ts

-- Jointure avec la table de liaison qui associe les émissions aux genres
JOIN tv_show_genres tsg ON ts.id = tsg.show_id

-- Jointure avec la table des genres pour filtrer sur "Comedy"
JOIN tv_genres tg ON tsg.genre_id = tg.id

-- Filtre uniquement les émissions appartenant au genre "Comedy"
WHERE tg.name = 'Comedy'

-- Trie les résultats par titre en ordre alphabétique
ORDER BY ts.title ASC;
