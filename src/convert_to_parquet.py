
import pandas as pd
import os

def convert_to_parquet(input_csv, output_parquet):
    """
    Reads a CSV and converts it to Parquet format.
    """
    print(f"Reading {input_csv}...")
    df = pd.read_csv(input_csv, low_memory=False)
    
    print("Sorting dataframe...")
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by=['date', 'serial_number']).reset_index(drop=True)

    print(f"Saving final dataframe to {output_parquet}...")
    df.to_parquet(output_parquet, index=False)
    print("Done.")

if __name__ == "__main__":
    input_csv = "datasets/backblaze_2015_processed.csv"
    output_parquet = "datasets/backblaze_2015_preprocessed.parquet"
    
    convert_to_parquet(input_csv, output_parquet)
    
    # Clean up intermediate file
    os.remove(input_csv)
