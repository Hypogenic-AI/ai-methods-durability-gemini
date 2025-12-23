
import pandas as pd
from tqdm import tqdm

def preprocess_concatenated_csv(input_file, output_file):
    """
    Reads the concatenated CSV, converts dtypes, sorts, and saves as Parquet.
    """
    print(f"Reading {input_file}...")
    df = pd.read_csv(input_file, low_memory=False)

    print("Converting data types...")
    for col in tqdm(df.columns, desc="Converting dtypes"):
        if col == 'date':
            df[col] = pd.to_datetime(df[col], errors='coerce')
        elif col in ['serial_number', 'model']:
            df[col] = df[col].astype(str)
        elif col == 'failure':
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)
        else: # SMART values
            df[col] = pd.to_numeric(df[col], errors='coerce')
            
    print("Dropping rows with invalid dates...")
    df = df.dropna(subset=['date'])

    print("Sorting dataframe...")
    df = df.sort_values(by=['date', 'serial_number']).reset_index(drop=True)

    print(f"Saving preprocessed dataframe to {output_file}...")
    df.to_parquet(output_file, index=False)
    print("Done.")


if __name__ == "__main__":
    input_csv = "datasets/backblaze_2015_concatenated.csv"
    output_parquet = "datasets/backblaze_2015_preprocessed.parquet"
    
    preprocess_concatenated_csv(input_csv, output_parquet)

