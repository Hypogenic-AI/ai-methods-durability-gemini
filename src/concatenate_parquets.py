
import pandas as pd
import os
from tqdm import tqdm

def concatenate_parquets(input_dir, output_file):
    """
    Concatenates all parquet files in a directory.
    """
    print(f"Concatenating parquet files from {input_dir}...")
    
    files = sorted([os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.parquet')])
    
    df_list = []
    for file in tqdm(files, desc="Reading parquet chunks"):
        df = pd.read_parquet(file)
        df_list.append(df)
        
    concatenated_df = pd.concat(df_list, ignore_index=True)
    
    print("Sorting dataframe...")
    concatenated_df['date'] = pd.to_datetime(concatenated_df['date'])
    concatenated_df = concatenated_df.sort_values(by=['date', 'serial_number']).reset_index(drop=True)
    
    print(f"Saving final dataframe to {output_file}...")
    concatenated_df.to_parquet(output_file, index=False)
    
    # Clean up intermediate files
    for file in files:
        os.remove(file)
    os.rmdir(input_dir)
    
    print("Done.")

if __name__ == "__main__":
    input_dir = "datasets/backblaze_2015_processed_chunks"
    output_file = "datasets/backblaze_2015_preprocessed.parquet"
    
    concatenate_parquets(input_dir, output_file)
