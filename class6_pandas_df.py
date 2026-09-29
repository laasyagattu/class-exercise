from pathlib import Path

import pandas as pd

data_path = Path("data") / "messy_netflix_titles.csv"
df = pd.read_csv(data_path)

# first look checklist
print(df.shape) 
print(df.head())
print(df.columns) 
print(df.dtypes) 
df.info() 
print(df.describe())

# check whether column is numeric
print(df.dtypes)

is_numeric = pd.api.types.is_numeric_dtype(df["viewer_score"])
print(is_numeric)
is_numeric = pd.api.types.is_numeric_dtype(df["title"])
print(is_numeric)


# selecting data
# one column
titles = df["title"]

print(titles.head())
print(type(titles))

# multiple columns
selected = df[["title", "type"]]
print(selected.head())
print(type(selected))

# rows with boolean condition
is_movie = df["type"] == "Movie"
print(is_movie.head())

# matching rows
movies = df[df["type"] == "Movie"]
print(movies.head())
print(movies.shape)

# numeric conditions
recent = df[df["release_year"] >= 2020]

# combining conditions
recent_movies = df[(df["type"] == "Movie") & (df["release_year"] >= 2020)]
movies_or_recent = df[(df["type"] == "Movie") | (df["release_year"] >= 2020) ]

# selecting rows and columns together
result = df.loc[df["release_year"] >= 2020,["title", "type"]]
print(result.head())


# duplicate rows
# detecting duplicates
print(df[df.duplicated()])

# removing duplicates
before = len(df)
df = df.drop_duplicates() # only if all column values match
print(f"Removed {before - len(df)} duplicate row(s)")


# missing values
# detecting
print(df.isna().sum())

# Drop rows containing one or more missing values
rows_dropped = df.dropna()

# Drop columns containing one or more missing values
columns_dropped = df.dropna(axis=1)
