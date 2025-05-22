import os
import logging
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

# Setup logging
log_path = "logs/pipeline_download.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    handlers=[
        logging.FileHandler(log_path, mode='w'),
        logging.StreamHandler()
    ]
)

try:
    download_path = os.path.join("data", "raw")
    os.makedirs(download_path, exist_ok=True)

    api = KaggleApi()
    api.authenticate()

    logging.info("Starting download...")
    api.dataset_download_files("grouplens/movielens-20m-dataset", path=download_path)

    logging.info("zip file has been downloaded.")
    logging.info("Extracting the files...")

    zip_file = os.path.join(download_path, "movielens-20m-dataset.zip")
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(download_path)

    logging.info("Cleaning up the folder...")
    os.remove(zip_file)
    logging.info("Dataset downloaded and extracted successfully.")

except Exception as e:
    logging.error(f"Error during download: {e}")
