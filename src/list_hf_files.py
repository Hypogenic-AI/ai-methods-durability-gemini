
from huggingface_hub import HfApi

def list_repo_files(repo_id):
    """
    Lists all files in a Hugging Face repository.
    """
    try:
        api = HfApi()
        files = api.list_repo_files(repo_id=repo_id, repo_type="dataset")
        for file in files:
            print(file)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_repo_files("backblaze/Drive_Stats")
