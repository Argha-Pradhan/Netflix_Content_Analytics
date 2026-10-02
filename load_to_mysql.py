import pandas as pd
import mysql.connector

# Load cleaned data
df = pd.read_csv(r"E:\\Project_1\\Netflix_Content_Analytics\\netflix_cleaned.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="arghaSQL",
    database="projects"

)

cursor = conn.cursor()

# Insert data
query = """
INSERT INTO netflix (
    show_id,
    type,
    title,
    director,
    cast,
    country,
    date_added,
    release_year,
    genres,
    language,
    description,
    popularity,
    vote_count,
    vote_average,
    budget,
    revenue
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

data = [
    tuple(row)
    for row in df.itertuples(index=False, name=None)
]

cursor.executemany(query, data)

conn.commit()

print(f"Inserted {cursor.rowcount} rows.")

cursor.close()
conn.close()