
import os
import pandas as pd
from tqdm import tqdm
from find_common_columns import find_common_columns

def concatenate_to_csv(directory, common_columns, output_file):
    """
    Concatenates all daily CSV files into a single CSV file.
    """
    if not common_columns:
        print("No common columns found.")
        return

    # Read all as strings to avoid dtype inference issues
    dtype_map = {col: str for col in common_columns}

    # Use an iterator to avoid loading all files into memory at once
    df_iterator = (pd.read_csv(os.path.join(directory, f), usecols=common_columns, dtype=dtype_map, low_memory=False) 
                   for f in sorted(os.listdir(directory)) if f.endswith('.csv'))

    # Use a chunked approach to write to the output CSV
    chunksize = 100000 
    header = True
    for df in tqdm(df_iterator, desc="Concatenating to CSV"):
        df.to_csv(output_file, mode='a', header=header, index=False)
        header = False


if __name__ == "__main__":
    data_directory = "datasets/backblaze_2015"
    output_file = "datasets/backblaze_2015_concatenated.csv"
    
    # Remove the output file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)

    print("Finding common columns...")
    common_cols = find_common_columns(data_directory)
    
    if common_cols:
        print(f"Found {len(common_cols)} common columns.")
        concatenate_to_csv(data_directory, common_cols, output_file)
        print("Done.")

