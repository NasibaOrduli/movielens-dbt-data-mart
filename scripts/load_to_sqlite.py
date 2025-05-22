import logging
import pandas as pd
import sqlite3
from pathlib import Path

# Setup logging
log_path = "logs/pipeline_load.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    handlers=[
        logging.FileHandler(log_path, mode='w'),
        logging.StreamHandler()
    ]
)

DB_PATH = Path("dbt_movielens/movielens.db")
RAW_PATH = Path("data/raw")

try:
    conn = sqlite3.connect(DB_PATH)

    files = {
        "movies": "movie.csv",
        "ratings": "rating.csv",
        "tags": "tag.csv",
        "links": "link.csv",
        "genome_scores": "genome_scores.csv",
        "genome_tags": "genome_tags.csv"
    }

    for table, file in files.items():
        df = pd.read_csv(RAW_PATH / file)
        df.to_sql(table, conn, if_exists='replace', index=False)
        logging.info(f"Loaded {table} into SQLite")

    conn.close()
    logging.info("All tables loaded successfully.")

except Exception as e:
    logging.error(f"Error loading data: {e}")

