-- Sélectionne le nom des genres associés à la série "Dexter"
SELECT g.name
FROM tv_genres g

-- Jointure avec la table de liaison `tv_show_genres` pour associer les genres aux émissions
JOIN tv_show_genres tsg ON g.id = tsg.genre_id

-- Jointure avec la table `tv_shows` pour récupérer les informations des émissions
JOIN tv_shows s ON tsg.tv_show_id = s.id

-- Filtre pour ne récupérer que les genres de l'émission "Dexter"
WHERE s.title = "Dexter"

-- Trie les genres par ordre alphabétique (croissant)
ORDER BY g.name ASC;
