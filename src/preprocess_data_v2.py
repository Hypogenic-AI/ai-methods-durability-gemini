
import os
import pandas as pd
from tqdm import tqdm
from find_common_columns import find_common_columns
import pyarrow as pa
import pyarrow.parquet as pq

def preprocess_and_save_in_chunks(directory, common_columns, output_path):
    """
    Reads CSVs in chunks, preprocesses them, and appends to a Parquet file.
    """
    if not common_columns:
        print("No common columns found.")
        return

    files = sorted([os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')])
    
    writer = None

    for file in tqdm(files, desc="Processing CSVs"):
        try:
            df = pd.read_csv(file, usecols=common_columns)
            
            # Simple preprocessing
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
            df = df.dropna(subset=['date'])

            table = pa.Table.from_pandas(df, preserve_index=False)
            
            if writer is None:
                writer = pq.ParquetWriter(output_path, table.schema)
            
            writer.write_table(table)

        except Exception as e:
            print(f"Error processing {file}: {e}")
            continue
    
    if writer:
        writer.close()
        print(f"Saved concatenated data to {output_path}")
    else:
        print("No data was written.")

if __name__ == "__main__":
    data_directory = "datasets/backblaze_2015"
    output_file = "datasets/backblaze_2015_concatenated.parquet"
    
    print("Finding common columns...")
    common_cols = find_common_columns(data_directory)
    
    if common_cols:
        print(f"Found {len(common_cols)} common columns.")
        preprocess_and_save_in_chunks(data_directory, common_cols, output_file)
        
        print("Sorting the Parquet file...")
        df = pd.read_parquet(output_file)
        df = df.sort_values(by=['date', 'serial_number']).reset_index(drop=True)
        df.to_parquet(output_file, index=False)
        print("Sorting complete.")

