-- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE genre_id > 0
GROUP BY name
ORDER BY number_of_shows DESC;