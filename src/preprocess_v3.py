
import pandas as pd
from tqdm import tqdm
import os

def process_and_save_chunks_to_parquet(input_csv, output_dir):
    """
    Reads a large CSV in chunks, processes each chunk, and saves to a new parquet file.
    """
    print(f"Processing {input_csv} in chunks and saving to {output_dir}...")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    chunksize = 100000
    
    for i, chunk in enumerate(tqdm(pd.read_csv(input_csv, chunksize=chunksize, low_memory=False), desc="Processing chunks")):
        
        # Convert dtypes
        for col in chunk.columns:
            if col == 'date':
                chunk[col] = pd.to_datetime(chunk[col], errors='coerce')
            elif col in ['serial_number', 'model']:
                chunk[col] = chunk[col].astype(str)
            elif col == 'failure':
                chunk[col] = pd.to_numeric(chunk[col], errors='coerce').fillna(0).astype(int)
            else: # SMART values
                chunk[col] = pd.to_numeric(chunk[col], errors='coerce')
        
        # Drop rows with invalid dates
        chunk = chunk.dropna(subset=['date'])

        # Save chunk to parquet
        chunk.to_parquet(os.path.join(output_dir, f"chunk_{i}.parquet"), index=False)

    print(f"Saved processed chunks to {output_dir}")


if __name__ == "__main__":
    input_csv = "datasets/backblaze_2015_concatenated.csv"
    output_dir = "datasets/backblaze_2015_processed_chunks"

    process_and_save_chunks_to_parquet(input_csv, output_dir)
    
    print("Done.")
