
# 🎬 MovieLens dbt Data Mart Project

This project builds an end-to-end ELT pipeline using the [MovieLens 20M dataset](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset), transforming raw movie ratings and metadata into a structured analytics-ready data mart using **SQLite** and **dbt**.

---

## 📁 Project Structure

```
movielens-dbt-data-mart/
├── data/raw/                  # Raw CSVs from MovieLens
├── dbt_movielens/             # dbt project
│   ├── models/
│   ├── macros/
|   ├── tests/
│   ├── movielens.db           # SQLite database file
|   ├── dbt_project.yml
├── scripts/                   # Python scripts (download, load, visuals)
├── logs/                      # Pipeline logs
├── visuals/                   # Visuals based on the data model
└── README.md
```

---

## ✅ Setup Instructions

### 1. 🔐 Authenticate with Kaggle

Place your `kaggle.json` API key in:

- Windows: `C:\Users\<your_username>\.kaggle\kaggle.json`
- Mac/Linux: `~/.kaggle/kaggle.json`

---

### 2. 🛠 Install requirements.txt
```bash
pip install -r requirements.txt
```

### 3. 📥 Download and extract dataset

```bash
python scripts/download_data.py
```

This will extract all MovieLens CSVs into `data/raw/`.

---

### 4. 📥 Load data into SQLite

```bash
python scripts/load_to_sqlite.py
```

This will create `movielens.db` inside `dbt_movielens/`.

---

### 5. ⚙️ Configure dbt profile

Edit your global profile at `~/.dbt/profiles.yml`:

```yaml
dbt_movielens:
  target: dev
  outputs:
    dev:
      type: sqlite
      threads: 1
      database: C:/path/to/movielens-dbt-data-mart/dbt_movielens/movielens.db
      schema: main
      schema_directory: C:/path/to/movielens-dbt-data-mart/dbt_movielens
```

> ✅ Use **absolute paths** and forward slashes (`/`).

---

### 6. 🚀 Run the dbt pipeline

```bash
cd dbt_movielens
dbt clean
dbt run
dbt test
```

---

## 🧠 Models Overview

### 🏗 Staging Models

| Model               | Description                            |
|---------------------|----------------------------------------|
| `stg_movies`        | Movie metadata with extracted year     |
| `stg_ratings`       | Ratings with timestamp formatting      |
| `stg_links`         | External IMDb and TMDb IDs             |
| `stg_user_tags`     | User-submitted tags                    |
| `stg_genome_tags`   | Genome tag definitions                 |
| `stg_genome_scores` | Movie-tag relevance scores             |

### 🧱 Marts / Core Models

| Model                    | Description                            |
|--------------------------|----------------------------------------|
| `dim_movie`              | Main movie dimension with links        |
| `dim_genre`              | Unique genre lookup                    |
| `bridge_movie_genre`     | Mapping table for movies ↔ genres      |
| `fact_ratings`           | Star schema fact table for ratings     |
| `dim_genome_tag`         | Tags used in genome scores             |

---

## 🛠 Tech Stack

- Python 3.10+
- dbt-core 1.9+
- dbt-sqlite
- SQLite
- Pandas
- Kaggle API

---

