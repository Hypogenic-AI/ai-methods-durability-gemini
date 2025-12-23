import os
from datasets import load_dataset, get_dataset_config_names

def download_backblaze_2015():
    """
    Downloads and saves the Backblaze Drive Stats dataset for the year 2015.
    """
    print("Downloading Backblaze Drive Stats dataset for 2015...")
    try:
        # First, try to get the list of available configurations
        configs = get_dataset_config_names("backblaze/Drive_Stats")
        print(f"Available configurations: {configs}")

        # Try to load the data for 2015
        dataset = load_dataset("backblaze/Drive_Stats", "2015")
        
        output_path = "datasets/backblaze_drive_stats_2015"
        print(f"Saving dataset to {output_path}...")
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        dataset.save_to_disk(output_path)
        print("Dataset saved successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check the available configurations and modify the script accordingly.")

if __name__ == "__main__":
    download_backblaze_2015()