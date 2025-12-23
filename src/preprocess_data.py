
import os
import pandas as pd
from tqdm import tqdm
from find_common_columns import find_common_columns

def concatenate_daily_csvs(directory, common_columns):
    """
    Concatenates all daily CSV files into a single DataFrame.
    """
    if not common_columns:
        print("No common columns found.")
        return None

    df_list = []
    files = sorted([os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')])
    
    for file in tqdm(files, desc="Concatenating CSVs"):
        try:
            df = pd.read_csv(file, usecols=common_columns)
            df_list.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")
            continue
            
    if not df_list:
        print("No dataframes to concatenate.")
        return None
        
    concatenated_df = pd.concat(df_list, ignore_index=True)
    return concatenated_df

if __name__ == "__main__":
    data_directory = "datasets/backblaze_2015"
    
    print("Finding common columns...")
    common_cols = find_common_columns(data_directory)
    
    if common_cols:
        print(f"Found {len(common_cols)} common columns.")
        
        # The 'failure' column from the notebook is mapped to 'label'.
        # I'll check if 'failure' is in the common columns and rename it.
        if 'failure' in common_cols:
            # The notebook expects 'label'
            pass # we will rename it later
        
        # The notebook uses `day_of_year` for the date. I will do the same.
        
        df = concatenate_daily_csvs(data_directory, common_cols)
        
        if df is not None:
            print("Sorting dataframe...")
            df = df.sort_values(by=['date', 'serial_number']).reset_index(drop=True)
            
            output_path = "datasets/backblaze_2015_concatenated.parquet"
            print(f"Saving concatenated dataframe to {output_path}...")
            df.to_parquet(output_path)
            print("Done.")
