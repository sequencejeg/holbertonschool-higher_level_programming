-- Script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name
FROM tv_show_genres
RIGHT JOIN tv_shows ON show_id = tv_shows.id
RIGHT JOIN tv_genres ON genre_id = tv_genres.id
WHERE title = "Dexter"
ORDER BY tv_genres.name ASC;