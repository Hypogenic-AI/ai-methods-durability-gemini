
import pandas as pd
from tqdm import tqdm
import os

def preprocess_in_chunks(input_file, output_file):
    """
    Reads a large CSV in chunks, processes each chunk, and saves to a new CSV.
    """
    print(f"Processing {input_file} in chunks...")
    
    # Remove the output file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)

    chunksize = 100000
    header = True
    
    for chunk in tqdm(pd.read_csv(input_file, chunksize=chunksize, low_memory=False), desc="Processing chunks"):
        
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

        # Append processed chunk to new CSV
        chunk.to_csv(output_file, mode='a', header=header, index=False)
        header = False

    print(f"Saved processed data to {output_file}")


if __name__ == "__main__":
    input_csv = "datasets/backblaze_2015_concatenated.csv"
    processed_csv = "datasets/backblaze_2015_processed.csv"
    output_parquet = "datasets/backblaze_2015_preprocessed.parquet"

    # Process in chunks and save to a new CSV
    preprocess_in_chunks(input_csv, processed_csv)
    
    # Now read the processed CSV and save to Parquet
    print(f"Reading processed CSV {processed_csv}...")
    df = pd.read_csv(processed_csv, low_memory=False)
    
    print("Sorting dataframe...")
    df['date'] = pd.to_datetime(df['date']) # Ensure date is datetime object before sorting
    df = df.sort_values(by=['date', 'serial_number']).reset_index(drop=True)

    print(f"Saving final dataframe to {output_parquet}...")
    df.to_parquet(output_parquet, index=False)
    
    # Clean up intermediate file
    os.remove(processed_csv)
    
    print("Done.")
