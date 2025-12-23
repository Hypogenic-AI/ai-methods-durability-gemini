
import dask.dataframe as dd
import os

def sort_with_dask_v2(input_dir, output_file):
    """
    Uses Dask to concatenate and save parquet files, then sorts.
    """
    print(f"Reading parquet files from {input_dir} with Dask...")
    ddf = dd.read_parquet(os.path.join(input_dir, '*.parquet'))
    
    # Don't sort in Dask, just save. We will sort with pandas later.
    print(f"Saving concatenated dataframe to {output_file}...")
    ddf.to_parquet(output_file, write_index=False)
    
    print("Done.")

if __name__ == "__main__":
    input_dir = "datasets/backblaze_2015_processed_chunks"
    output_file = "datasets/backblaze_2015_preprocessed.parquet"
    
    sort_with_dask_v2(input_dir, output_file)
