
import os
import pandas as pd

def find_common_columns(directory):
    """
    Finds the common columns across all CSV files in a directory.
    """
    try:
        files = sorted([os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')])
        
        if not files:
            print("No CSV files found in the directory.")
            return None
        
        # Get columns from the first file
        common_columns = set(pd.read_csv(files[0], nrows=0).columns)
        
        for file in files[1:]:
            try:
                columns = set(pd.read_csv(file, nrows=0).columns)
                common_columns.intersection_update(columns)
            except Exception as e:
                print(f"Error reading {file}: {e}")
                continue
        
        return list(common_columns)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    common_cols = find_common_columns("datasets/backblaze_2015")
    if common_cols:
        print("Common columns found:")
        for col in sorted(common_cols):
            print(col)
