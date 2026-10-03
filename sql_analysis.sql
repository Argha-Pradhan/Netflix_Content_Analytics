
-- Netflix Content Analytics
-- SQL Analysis


-- Dataset & Content Overview

SELECT * FROM netflix;

SELECT type, COUNT(*) AS counts
FROM netflix
GROUP BY type;

SELECT release_year, COUNT(*) AS movie_per_year
FROM netflix
GROUP BY release_year;

SELECT language, COUNT(*) AS Language_frequency
FROM netflix
GROUP BY language;


-- Content Trends Over Time

SELECT release_year, COUNT(*) AS Count_of_movies
FROM netflix
GROUP BY release_year;

SELECT release_year, AVG(vote_average) AS Average_Rating
FROM netflix
GROUP BY release_year
ORDER BY release_year ASC;

SELECT genres, AVG(vote_average) AS Average_Rating
FROM netflix
GROUP BY genres
ORDER BY Average_Rating DESC
LIMIT 15;


-- Genre Analysis

-- Split multi-valued genre data into individual genre records

SELECT show_id, TRIM(j.genre) AS genre
FROM netflix
JOIN JSON_TABLE(
    CONCAT('["', REPLACE(genres, ', ', '","'), '"]'),
    '$[*]' COLUMNS (
        genre VARCHAR(100) PATH '$'
    )
) AS j;


-- Create a separate genre table to avoid repeating the transformation

CREATE TABLE show_genres (
    show_id INT,
    genre VARCHAR(100)
);

INSERT INTO show_genres (show_id, genre)
SELECT show_id, TRIM(j.genre)
FROM netflix
JOIN JSON_TABLE(
    CONCAT('["', REPLACE(genres, ', ', '","'), '"]'),
    '$[*]' COLUMNS (
        genre VARCHAR(100) PATH '$'
    )
) AS j;


-- Genre frequency

SELECT genre, COUNT(*) AS total
FROM show_genres
GROUP BY genre
ORDER BY total DESC;


-- Average rating by genre

SELECT sg.genre, ROUND(AVG(n.vote_average), 2) AS avg_rating
FROM show_genres sg
JOIN netflix n ON sg.show_id = n.show_id
GROUP BY sg.genre
ORDER BY avg_rating DESC;


-- Average popularity by genre

SELECT sg.genre, ROUND(AVG(n.popularity), 2) AS avg_popularity
FROM show_genres sg
JOIN netflix n ON sg.show_id = n.show_id
GROUP BY sg.genre
ORDER BY avg_popularity DESC;


-- Total revenue associated with each genre

SELECT sg.genre, SUM(n.revenue) AS total_revenue
FROM show_genres sg
JOIN netflix n ON sg.show_id = n.show_id
GROUP BY sg.genre
ORDER BY total_revenue DESC;


-- Rating & Audience Analysis

-- Average audience vote count

SELECT AVG(vote_count)
FROM netflix;


-- Average movie rating

SELECT AVG(vote_average)
FROM netflix;


-- Movies with above-average votes and ratings

SELECT title, vote_count, vote_average
FROM netflix
WHERE vote_count > (SELECT AVG(vote_count) FROM netflix)
  AND vote_average > (SELECT AVG(vote_average) FROM netflix)
ORDER BY vote_count DESC;


-- Highly rated movies with at least 10,000 votes

SELECT title, vote_count, vote_average
FROM netflix
WHERE vote_count >= 10000
  AND vote_average >= 8
ORDER BY vote_average DESC, vote_count DESC;


-- Financial Analysis

-- Movies with available budget and revenue data

SELECT title, budget, revenue
FROM netflix
WHERE budget > 0
  AND revenue > 0
ORDER BY budget DESC;


-- Highest return relative to budget

SELECT
    title,
    budget,
    revenue,
    ROUND((revenue - budget) / budget * 100, 2) AS return_percentage
FROM netflix
WHERE budget >= 100000
  AND revenue > 0
ORDER BY return_percentage DESC
LIMIT 20;


-- Popularity Analysis

-- Movies ranked by audience vote count

SELECT
    title,
    vote_count,
    popularity
FROM netflix
WHERE vote_count > 0
ORDER BY vote_count DESC;

