import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Paths
db_path = Path("dbt_movielens/movielens.db")
output_dir = Path("visuals")
output_dir.mkdir(exist_ok=True)

# Connect to database
conn = sqlite3.connect(db_path)

# Top 10 most rated movies
top_movies = pd.read_sql_query("""
    SELECT m.title, COUNT(r.rating) as rating_count
    FROM fact_ratings r
    JOIN dim_movie m ON r.movie_id = m.movie_id
    GROUP BY m.title
    ORDER BY rating_count DESC
    LIMIT 10
""", conn)

# Average rating by genre
avg_rating_by_genre = pd.read_sql_query("""
    SELECT g.genre, AVG(r.rating) as avg_rating
    FROM fact_ratings r
    JOIN dim_movie m ON r.movie_id = m.movie_id
    JOIN bridge_movie_genre bg ON m.movie_id = bg.movie_id
    JOIN dim_genre g ON bg.genre_id = g.genre_id
    GROUP BY g.genre
    ORDER BY avg_rating DESC
""", conn)

# Movies per year
movies_per_year = pd.read_sql_query("""
    SELECT release_year, COUNT(*) as movie_count
    FROM dim_movie
    WHERE release_year IS NOT NULL
    GROUP BY release_year
    ORDER BY release_year
""", conn)


# Average rating by year ---
avg_rating_by_year_query = """
SELECT strftime('%Y', rating_datetime) as year, AVG(rating) as avg_rating
FROM fact_ratings
WHERE rating_datetime IS NOT NULL
GROUP BY year
ORDER BY year
"""
avg_rating_by_year_df = pd.read_sql_query(avg_rating_by_year_query, conn)

# Highest rated movies with 100+ ratings ---
highest_rated_movies_query = """
SELECT m.title, COUNT(*) as rating_count, AVG(r.rating) as avg_rating
FROM fact_ratings r
JOIN dim_movie m ON r.movie_id = m.movie_id
GROUP BY m.title
HAVING COUNT(*) >= 100
ORDER BY avg_rating DESC
LIMIT 10
"""
highest_rated_movies_df = pd.read_sql_query(highest_rated_movies_query, conn)

conn.close()

# --- Plot 1 ---
plt.figure(figsize=(10, 5))
plt.barh(top_movies["title"], top_movies["rating_count"], color="skyblue")
plt.xlabel("Number of Ratings")
plt.title("Top 10 Most Rated Movies")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(output_dir / "top_10_most_rated_movies.png")
plt.close()

# --- Plot 2 ---
plt.figure(figsize=(12, 6))
plt.bar(avg_rating_by_genre["genre"], avg_rating_by_genre["avg_rating"], color="salmon")
plt.xticks(rotation=45, ha='right')
plt.ylabel("Average Rating")
plt.title("Average Rating by Genre")
plt.tight_layout()
plt.savefig(output_dir / "average_rating_by_genre.png")
plt.close()

# --- Plot 3 ---
plt.figure(figsize=(12, 6))
plt.plot(movies_per_year["release_year"], movies_per_year["movie_count"], marker='o')
plt.xlabel("Release Year")
plt.ylabel("Number of Movies")
plt.title("Number of Movies Released Per Year")
plt.grid(True)
plt.tight_layout()
plt.savefig(output_dir / "movies_per_year.png")
plt.close()

# --- Plot 4: Average rating by year ---
plt.figure(figsize=(12, 6))
plt.plot(avg_rating_by_year_df["year"], avg_rating_by_year_df["avg_rating"], marker='o', color='green')
plt.xlabel("Year")
plt.ylabel("Average Rating")
plt.title("Average Movie Rating by Year")
plt.grid(True)
plt.tight_layout()
plt.savefig(output_dir / "avg_rating_by_year.png")
plt.close()

# --- Plot 5: Highest rated movies (min 100 ratings) ---
plt.figure(figsize=(10, 6))
plt.barh(highest_rated_movies_df["title"], highest_rated_movies_df["avg_rating"], color="gold")
plt.xlabel("Average Rating")
plt.title("Top 10 Highest Rated Movies (100+ Ratings)")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(output_dir / "top_10_highest_rated_movies.png")
plt.close()


print(f"Visuals saved to: {output_dir.resolve()}")
