
import os
import pandas as pd
from tqdm import tqdm
import pyarrow as pa
import pyarrow.parquet as pq
from find_common_columns import find_common_columns

def get_schema(common_columns):
    """
    Defines a consistent schema for the data.
    """
    schema = {}
    for col in common_columns:
        if col in ['date']:
            schema[col] = 'str' # Read as string, convert to datetime later
        elif col in ['serial_number', 'model']:
            schema[col] = 'str'
        elif col == 'failure':
            schema[col] = 'int64'
        elif 'normalized' in col:
            schema[col] = 'float64'
        elif 'raw' in col:
            schema[col] = 'float64'
        else:
            schema[col] = 'str'
    
    # capacity_bytes can be read as float to be safe
    if 'capacity_bytes' in schema:
        schema['capacity_bytes'] = 'float64'
        
    return schema

def preprocess_and_save_with_schema(directory, common_columns, output_path, schema):
    """
    Reads CSVs with a defined schema, preprocesses them, and appends to a Parquet file.
    """
    if not common_columns:
        print("No common columns found.")
        return

    files = sorted([os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')])
    
    writer = None

    for file in tqdm(files, desc="Processing CSVs"):
        try:
            # Read with specified dtype
            df = pd.read_csv(file, usecols=common_columns, dtype=schema, low_memory=False)
            
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
            df = df.dropna(subset=['date'])

            # Convert to pyarrow table
            table = pa.Table.from_pandas(df, preserve_index=False)
            
            if writer is None:
                writer = pq.ParquetWriter(output_path, table.schema)
            
            # Ensure schema matches before writing
            if not table.schema.equals(writer.schema):
                print(f"Schema mismatch in {file}. Skipping.")
                # Here you could implement more sophisticated schema evolution if needed
                continue

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
        
        defined_schema = get_schema(common_cols)
        
        preprocess_and_save_with_schema(data_directory, common_cols, output_file, defined_schema)
        
        if os.path.exists(output_file):
            print("Sorting the Parquet file...")
            df = pd.read_parquet(output_file)
            df = df.sort_values(by=['date', 'serial_number']).reset_index(drop=True)
            df.to_parquet(output_file, index=False)
            print("Sorting complete.")
        else:
            print("Output file not created. Skipping sort.")

