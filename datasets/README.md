# Downloaded Datasets

This directory contains datasets for the research project. Data files are NOT
committed to git due to size. Follow the download instructions below.

## Dataset 1: Backblaze Hard Drive Stats

### Overview
- **Source**: [https://huggingface.co/datasets/backblaze/Drive_Stats](https://huggingface.co/datasets/backblaze/Drive_Stats)
- **Size**: ~7M samples for 2015
- **Format**: HuggingFace Dataset / CSV
- **Task**: Failure prediction
- **Splits**: train
- **License**: Not specified

### Download Instructions

The automatic download script `src/download_data.py` might fail due to inconsistencies in the dataset schema on HuggingFace. If it fails, please follow these manual steps:

1.  Visit the dataset page on Hugging Face: [https://huggingface.co/datasets/backblaze/Drive_Stats](https://huggingface.co/datasets/backblaze/Drive_Stats)
2.  Follow the instructions on the dataset page to download the data for the year 2015.
3.  Alternatively, you can use the `hf://` protocol with `datasets` library to load a specific subset of data. Due to the inconsistencies, it is recommended to load data quarter by quarter for 2015 and handle the schema changes.

### Loading the Dataset

Once downloaded, you can load the dataset from disk.

## Dataset 2: Newsroom

### Overview
- **Source**: [https://huggingface.co/datasets/lil-lab/newsroom](https://huggingface.co/datasets/lil-lab/newsroom)
- **Size**: 1.3M articles
- **Format**: HuggingFace Dataset
- **Task**: Summarization, Text Generation
- **Splits**: train, validation, test
- **License**: Not specified

### Download Instructions

The automatic download script `src/download_data.py` might fail. If it fails, please follow these manual steps:

1.  Visit the dataset page on Hugging Face: [https://huggingface.co/datasets/lil-lab/newsroom](https://huggingface.co/datasets/lil-lab/newsroom)
2.  Follow the instructions on the dataset page to download the data.

### Loading the Dataset

Once downloaded, you can load the dataset from disk.