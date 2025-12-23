
import zipfile
import os

def inspect_zip(zip_path):
    """
    Lists the files inside a zip archive.
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.printdir()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    inspect_zip("datasets/zip_csv/2015.zip")
