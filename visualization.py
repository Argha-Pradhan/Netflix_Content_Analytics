import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt


# MySQL connection

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="arghaSQL",
    database="projects"
)


# Color palette

teal = "#2A9D8F"
blue = "#457B9D"
navy = "#264653"
purple = "#6D597A"
orange = "#F4A261"
coral = "#E76F51"


# 1. Language Frequency

query = """
SELECT
    language,
    COUNT(*) AS language_count
FROM netflix
GROUP BY language
ORDER BY language_count DESC
LIMIT 8;
"""

df = pd.read_sql(query, conn)

total_movies = pd.read_sql(
    "SELECT COUNT(*) AS total FROM netflix;",
    conn
)["total"].iloc[0]

other_count = total_movies - df["language_count"].sum()

if other_count > 0:
    df.loc[len(df)] = ["Other", other_count]

language_colors = [
    navy,
    teal,
    blue,
    orange,
    coral,
    purple,
    "#8D99AE",
    "#A8DADC",
    "#ADB5BD"
]

plt.figure(figsize=(8, 8))

plt.pie(
    df["language_count"],
    labels=df["language"],
    autopct="%1.1f%%",
    startangle=90,
    colors=language_colors[:len(df)],
    wedgeprops={"width": 0.45, "edgecolor": "white"}
)

plt.title("Language Distribution of Movies")
plt.tight_layout()

plt.savefig(
    "E:\\Project_1\\Netflix_Content_Analytics\\visuals\\Language_Distribution_of_Movies.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# 2. Genre Frequency

query = """
SELECT
    genre,
    COUNT(*) AS movie_count
FROM show_genres
GROUP BY genre
ORDER BY movie_count DESC
LIMIT 8;
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(8, 8))

plt.pie(
    df["movie_count"],
    labels=df["genre"],
    autopct="%1.1f%%",
    startangle=90,
    colors=[
        teal,
        blue,
        orange,
        coral,
        purple,
        navy,
        "#8D99AE",
        "#A8DADC"
    ],
    wedgeprops={"width": 0.45, "edgecolor": "white"}
)

plt.title("Top 8 Genres by Movie Count")
plt.tight_layout()

plt.savefig(
    "E:\\Project_1\\Netflix_Content_Analytics\\visuals\\Top_8_Genres_by_Movie.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# 3. Average Rating by Genre

query = """
SELECT
    sg.genre,
    ROUND(AVG(n.vote_average), 2) AS average_rating
FROM show_genres sg
JOIN netflix n
    ON sg.show_id = n.show_id
GROUP BY sg.genre
ORDER BY average_rating DESC
LIMIT 8;
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(8, 8))

plt.pie(
    df["average_rating"],
    labels=df["genre"],
    autopct="%1.1f",
    startangle=90,
    colors=[
        blue,
        teal,
        purple,
        orange,
        coral,
        navy,
        "#8D99AE",
        "#A8DADC"
    ],
    wedgeprops={"width": 0.45, "edgecolor": "white"}
)

plt.title("Average Rating by Genre")
plt.tight_layout()

plt.savefig(
    "E:\\Project_1\\Netflix_Content_Analytics\\visuals\\Average_Rating_by_Genre.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# 4. Average Popularity by Genre

query = """
SELECT
    sg.genre,
    ROUND(AVG(n.popularity), 2) AS average_popularity
FROM show_genres sg
JOIN netflix n
    ON sg.show_id = n.show_id
GROUP BY sg.genre
ORDER BY average_popularity DESC
LIMIT 15;
"""

df = pd.read_sql(query, conn)

df = df.sort_values("average_popularity")

plt.figure(figsize=(10, 6))

plt.hlines(
    y=df["genre"],
    xmin=0,
    xmax=df["average_popularity"],
    color="#A8DADC",
    linewidth=2
)

plt.scatter(
    df["average_popularity"],
    df["genre"],
    color=coral,
    s=70,
    zorder=2
)

plt.title("Top 15 Genres by Average Popularity")
plt.xlabel("Average Popularity")
plt.ylabel("Genre")

plt.grid(axis="x", alpha=0.2)
plt.tight_layout()

plt.savefig(
    "E:\\Project_1\\Netflix_Content_Analytics\\visuals\\Top_15_Genres_by_Average_Popularity.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# 5. Highest-Budget Movies

query = """
SELECT
    title,
    budget
FROM netflix
WHERE budget > 0
ORDER BY budget DESC
LIMIT 15;
"""

df = pd.read_sql(query, conn)

df = df.sort_values("budget")

plt.figure(figsize=(10, 6))

plt.barh(
    df["title"],
    df["budget"],
    color=purple
)

plt.title("Top 15 Movies by Budget")
plt.xlabel("Budget")
plt.ylabel("Movie")

plt.grid(axis="x", alpha=0.2)
plt.tight_layout()

plt.savefig(
    "E:\\Project_1\\Netflix_Content_Analytics\\visuals\\Top_15_Movies_by_Budget.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# 6. Highest-Revenue Movies

query = """
SELECT
    title,
    revenue
FROM netflix
WHERE revenue > 0
ORDER BY revenue DESC
LIMIT 15;
"""

df = pd.read_sql(query, conn)

df = df.sort_values("revenue")

plt.figure(figsize=(10, 6))

plt.barh(
    df["title"],
    df["revenue"],
    color=teal
)

plt.title("Top 15 Movies by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Movie")

plt.grid(axis="x", alpha=0.2)
plt.tight_layout()

plt.savefig(
    "E:\\Project_1\\Netflix_Content_Analytics\\visuals\\Top_15_Movies_by_Revenue.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# 7. Highest Return Relative to Budget

query = """
SELECT
    title,
    budget,
    revenue,
    ROUND((revenue - budget) / budget * 100, 2) AS return_percentage
FROM netflix
WHERE budget >= 100000
  AND revenue > 0
ORDER BY return_percentage DESC
LIMIT 15;
"""

df = pd.read_sql(query, conn)

df = df.sort_values("return_percentage")

plt.figure(figsize=(11, 6))

plt.bar(
    df["title"],
    df["return_percentage"],
    color=orange
)

plt.title("Top 15 Movies by Return Relative to Budget")
plt.xlabel("Movie")
plt.ylabel("Return (%)")

plt.xticks(rotation=60, ha="right")
plt.grid(axis="y", alpha=0.2)

plt.tight_layout()

plt.savefig(
    "E:\\Project_1\\Netflix_Content_Analytics\\visuals\\Top_15_Movies_by_Return_Relative_to_Budget.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# 8. Highly Rated Movies with at Least 10,000 Votes

query = """
SELECT
    title,
    vote_count,
    vote_average
FROM netflix
WHERE vote_count >= 10000
  AND vote_average >= 8
ORDER BY vote_average DESC, vote_count DESC;
"""

df = pd.read_sql(query, conn)

df = df.sort_values(
    ["vote_average", "vote_count"],
    ascending=[True, True]
)

plt.figure(figsize=(10, 6))

plt.barh(
    df["title"],
    df["vote_average"],
    color=blue
)

plt.title("Highly Rated Movies with at Least 10,000 Votes")
plt.xlabel("Average Rating")
plt.ylabel("Movie")

plt.xlim(7.5, df["vote_average"].max() + 0.2)
plt.grid(axis="x", alpha=0.2)

plt.tight_layout()

plt.savefig(
    "E:\\Project_1\\Netflix_Content_Analytics\\visuals\\Highly_Rated_Movies.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# Close database connection

conn.close()