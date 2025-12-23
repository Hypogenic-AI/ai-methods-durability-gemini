
import os
import pandas as pd
from tqdm import tqdm
from find_common_columns import find_common_columns

def concatenate_with_string_dtype(directory, common_columns):
    """
    Concatenates all daily CSV files into a single DataFrame, reading all columns as strings first.
    """
    if not common_columns:
        print("No common columns found.")
        return None

    # Read all as strings to avoid dtype inference issues
    dtype_map = {col: str for col in common_columns}

    df_list = []
    files = sorted([os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')])
    
    for file in tqdm(files, desc="Reading CSVs as strings"):
        try:
            df = pd.read_csv(file, usecols=common_columns, dtype=dtype_map, low_memory=False)
            df_list.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")
            continue
            
    if not df_list:
        print("No dataframes to concatenate.")
        return None
        
    concatenated_df = pd.concat(df_list, ignore_index=True)
    return concatenated_df

def convert_dtypes(df):
    """
    Converts columns to appropriate dtypes after concatenation.
    """
    for col in tqdm(df.columns, desc="Converting dtypes"):
        if col == 'date':
            df[col] = pd.to_datetime(df[col], errors='coerce')
        elif col in ['serial_number', 'model']:
            continue # Already string
        elif col == 'failure':
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)
        else: # SMART values
            df[col] = pd.to_numeric(df[col], errors='coerce')
            
    return df


if __name__ == "__main__":
    data_directory = "datasets/backblaze_2015"
    output_file = "datasets/backblaze_2015_preprocessed.parquet"
    
    print("Finding common columns...")
    common_cols = find_common_columns(data_directory)
    
    if common_cols:
        print(f"Found {len(common_cols)} common columns.")
        
        df = concatenate_with_string_dtype(data_directory, common_cols)
        
        if df is not None:
            print("Converting data types...")
            df = convert_dtypes(df)
            
            print("Sorting dataframe...")
            df = df.sort_values(by=['date', 'serial_number']).reset_index(drop=True)

            print(f"Saving preprocessed dataframe to {output_file}...")
            df.to_parquet(output_file, index=False)
            print("Done.")

