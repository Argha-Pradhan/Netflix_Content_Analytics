-- Dataset & Content Overview	
select type,count(*) as counts from netflix group by type;
select release_year, count(*) as movie_per_year from netflix group by release_year;
select language,count(*) as Language_frequency from netflix group by language;

-- Content Trends Over Time
select release_year,count(*) as Count_of_movies from netflix group by release_year;
select release_year, avg(vote_average) as Average_Rating from netflix group by release_year order by release_year asc;
select genres, avg(vote_average) as Average_Rating from netflix group by genres order by Average_Rating desc limit 15;

-- Genre Analysis
SELECT show_id, TRIM(j.genre) AS genre
FROM netflix
JOIN JSON_TABLE(
    CONCAT('["', REPLACE(genres, ', ', '","'), '"]'),
    '$[*]' COLUMNS (
        genre VARCHAR(100) PATH '$'
    )
) AS j;

-- created table to avoid redundancy 
CREATE TABLE show_genres (
    show_id INT,
    genre VARCHAR(100)
);
INSERT INTO show_genres (show_id, genre)
SELECT show_id, TRIM(j.genre)
FROM movies
JOIN JSON_TABLE(
    CONCAT('["', REPLACE(genres, ', ', '","'), '"]'),
    '$[*]' COLUMNS (
        genre VARCHAR(100) PATH '$'
    )
) AS j;

SELECT genre, COUNT(*) AS total
FROM show_genres
GROUP BY genre
ORDER BY total DESC;
--
SELECT sg.genre, round(AVG(n.vote_average),2) AS avg_rating
FROM show_genres sg
JOIN netflix n ON sg.show_id = n.show_id
GROUP BY sg.genre
ORDER BY avg_rating DESC;
--
SELECT sg.genre, round((n.popularity),2) AS avg_popularity
FROM show_genres sg
JOIN netflix n ON sg.show_id = n.show_id
GROUP BY sg.genre
ORDER BY avg_popularity DESC;
--
SELECT sg.genre, SUM(n.revenue) AS total_revenue
FROM show_genres sg
JOIN netflix n ON sg.show_id = n.show_id
GROUP BY sg.genre
ORDER BY total_revenue DESC;

-- 




