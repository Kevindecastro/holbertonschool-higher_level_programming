-- Afficher tous les genres associés à chaque émission avec leur titre et nom
SELECT ts.title, tg.name
FROM tv_shows ts
-- Jointure gauche pour inclure toutes les émissions même sans genre
LEFT JOIN tv_show_genres tsg ON ts.id = tsg.show_id
-- Jointure gauche pour récupérer le nom du genre correspondant
LEFT JOIN tv_genres tg ON tsg.genre_id = tg.id
-- Trier les résultats par titre d'émission puis par nom de genre en ordre croissant
ORDER BY ts.title ASC, tg.name ASC;