import pandas as pd
df=pd.read_csv("E:\\Project_1\\Netflix_Content_Analytics\\netflix_movies_detailed_up_to_2025.csv")
print(df.shape)
print("Columns:",df.columns.to_list())
print(df.info())



df.columns= (df.columns.str.strip().str.lower().str.replace(' ','_'))

df = df.drop_duplicates()

#convert string columns to string type and strip whitespace

string_columns = [
    "type",
    "title",
    "director",
    "cast",
    "country",
    "rating",
    "duration",
    "genres",
    "language"
]

for col in string_columns:
    df[col] = df[col].astype("string").str.strip()

df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

#converting numeric columns to numeric
numeric_columns = [
    "release_year",
    "popularity",
    "vote_count",
    "vote_average",
    "budget",
    "revenue"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col],errors="coerce")




#print("Missing values in 'duration':", df["duration"].isna().sum())
#print("Non-missing values in 'duration':", df["duration"].notna().sum())
#No duration column is present in the dataset, so dropping it to avoid errors
df = df.drop(columns=["duration"])
print(df.columns.to_list())

print(df[["rating", "vote_average"]].head(10))

print(
    "Rating == Vote Average:",
    (pd.to_numeric(df["rating"], errors="coerce") == df["vote_average"]).mean()
)

print("\nTypes:")
print(df["type"].value_counts(dropna=False))

print("\nLanguages:")
print(df["language"].value_counts(dropna=False).head(20))

print("\nRatings:")
print(df["rating"].value_counts(dropna=False).head(20))

print("\nNumeric summary:")
print(df[
    [
        "release_year",
        "popularity",
        "vote_count",
        "vote_average",
        "budget",
        "revenue"
    ]
].describe())

numeric_check = [
    "popularity",
    "vote_count",
    "vote_average",
    "budget",
    "revenue"
]

for col in numeric_check:
    print(f"{col}: {(df[col] < 0).sum()} negative values")

print(
    df[
        (df["release_year"] < 1900) |
        (df["release_year"] > 2025)
    ][["title", "release_year"]]
)

print("Duplicate show IDs:", df["show_id"].duplicated().sum())
missing_summary = pd.DataFrame({
    "missing_count": df.isna().sum(),
    "missing_percentage": df.isna().mean() * 100
})

print(missing_summary.sort_values("missing_percentage", ascending=False))

df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

print(
    "Rating/Vote Average identical:",
    (df["rating"] == df["vote_average"]).all()
)

print(
    "Differences:",
    (df["rating"] != df["vote_average"]).sum()
)
#rating and vote_average columns are identical, so dropping the rating column to avoid redundancy
df = df.drop(columns=["rating"])

text_fill_columns = [
    "director",
    "cast",
    "country",
    "genres",
    "description"
]

for col in text_fill_columns:
    df[col] = df[col].fillna("Unknown")