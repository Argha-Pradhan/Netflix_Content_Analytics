import pandas as pd
df=pd.read_csv("E:\\DATA\\kaggle_datas\\netflix_movies_detailed_up_to_2025.csv")
# print(df.shape)
print("Columns:",df.columns.to_list())
# print(df.info())
# print("\nMissing values:")
# print(df.isnull().sum())
# print("Duplicated rows:",df.duplicated().sum())
df.columns= (df.columns.str.strip().str.lower().str.replace(' ','_'))

df = df.drop_duplicates()


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
print(df[["release_year",
    "popularity",
    "vote_count",
    "vote_average",
    "budget",
    "revenue"]])