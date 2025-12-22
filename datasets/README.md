# Downloaded Datasets

This directory contains datasets for the research project. Data files are NOT
committed to git due to size. Follow the download instructions below.

## Dataset 1: Backblaze Disk Stats

### Overview
- **Source**: [https://huggingface.co/datasets/backblaze/Drive_Stats](https://huggingface.co/datasets/backblaze/Drive_Stats)
- **Size**: ~7M samples for the year 2015
- **Format**: HuggingFace Dataset
- **Task**: Disk failure prediction (classification)
- **Splits**: train
- **License**: Not specified

### Download Instructions

**Using HuggingFace (recommended):**
```python
from datasets import load_dataset
dataset = load_dataset("backblaze/Drive_Stats")
dataset = dataset.filter(lambda x: x['date'].startswith('2015'))
dataset.save_to_disk("datasets/backblaze_drive_stats_2015")
```

**Note:** The automatic download might fail due to schema inconsistencies in the dataset. If it fails, you will need to download the data manually from the Backblaze website and preprocess it to have a consistent schema.

### Loading the Dataset

Once downloaded, load with:
```python
from datasets import load_from_disk
dataset = load_from_disk("datasets/backblaze_drive_stats_2015")
```

### Sample Data

Example records from this dataset:
```json
[
  {"date": "2015-01-01", "serial_number": "MJ0351YNG9Z0XA", "model": "Hitachi HDS5C3030ALA630", "capacity_bytes": 3000592982016, "failure": 0, ...},
  {"date": "2015-01-01", "serial_number": "Z3025K5Z", "model": "ST4000DM000", "capacity_bytes": 4000787030016, "failure": 0, ...}
]
```

## Dataset 2: Google Cluster Traces

### Overview
- **Source**: [https://github.com/google/cluster-data](https://github.com/google/cluster-data)
- **Size**: ~2.4TB
- **Format**: CSV
- **Task**: Job failure prediction (classification)
- **Splits**: Not applicable
- **License**: Not specified

### Download Instructions

The Google Cluster Traces dataset is not directly downloadable. You need to use Google BigQuery or Google Storage to access it. Please refer to the official GitHub repository for detailed instructions: [https://github.com/google/cluster-data](https://github.com/google/cluster-data)

### Loading the Dataset

Once you have downloaded the data, you can use a library like pandas to load the CSV files.

```python
import pandas as pd
df = pd.read_csv("path/to/your/downloaded/csv_file.csv")
```
