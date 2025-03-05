-- Liste toutes les villes et leurs états respectifs dans la base de données `hbtn_0d_usa`.
SELECT cities.id, cities.name, states.name 
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
