
from huggingface_hub import hf_hub_download
import os

def download_zip_file(repo_id, filename):
    """
    Downloads a single file from a Hugging Face repository.
    """
    try:
        if not os.path.exists("datasets"):
            os.makedirs("datasets")
        
        downloaded_file_path = hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            repo_type="dataset",
            local_dir="datasets"
        )
        print(f"File downloaded to: {downloaded_file_path}")
        return downloaded_file_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    download_zip_file("backblaze/Drive_Stats", "zip_csv/2015.zip")
