import os
from datasets import load_dataset

def download_backblaze_data():
    """
    Downloads and saves the Backblaze Drive Stats dataset for the year 2015.
    """
    print("Downloading Backblaze Drive Stats dataset for 2015...")
    try:
        dataset = load_dataset("backblaze/Drive_Stats")
        print("Filtering dataset for the year 2015...")
        dataset_2015 = dataset['train'].filter(lambda x: x['date'].startswith('2015'))
        
        output_path = "datasets/backblaze_drive_stats_2015"
        print(f"Saving dataset to {output_path}...")
        if not os.path.exists("datasets"):
            os.makedirs("datasets")
        dataset_2015.save_to_disk(output_path)
        print("Dataset saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please follow the manual download instructions in datasets/README.md")

def download_newsroom_data():
    """
    Downloads and saves the Newsroom dataset.
    """
    print("Downloading Newsroom dataset...")
    try:
        dataset = load_dataset("lil-lab/newsroom")
        output_path = "datasets/newsroom"
        print(f"Saving dataset to {output_path}...")
        if not os.path.exists("datasets"):
            os.makedirs("datasets")
        dataset.save_to_disk(output_path)
        print("Dataset saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please follow the manual download instructions in datasets/README.md")

if __name__ == "__main__":
    download_backblaze_data()
    download_newsroom_data()
