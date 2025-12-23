
import dask.dataframe as dd
import os

def sort_with_dask(input_dir, output_file):
    """
    Uses Dask to concatenate and sort parquet files.
    """
    print(f"Reading parquet files from {input_dir} with Dask...")
    ddf = dd.read_parquet(os.path.join(input_dir, '*.parquet'))
    
    print("Sorting dataframe with Dask...")
    ddf = ddf.set_index('date').persist() # Persist to keep in memory
    
    print(f"Saving final dataframe to {output_file}...")
    ddf.to_parquet(output_file, write_index=True)
    
    # Clean up intermediate files
    # for file in os.listdir(input_dir):
    #     os.remove(os.path.join(input_dir, file))
    # os.rmdir(input_dir)
    
    print("Done.")

if __name__ == "__main__":
    input_dir = "datasets/backblaze_2015_processed_chunks"
    output_file = "datasets/backblaze_2015_preprocessed.parquet"
    
    sort_with_dask(input_dir, output_file)
