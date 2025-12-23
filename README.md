# Measuring the "Durability" of AI Research Methods

This project aims to systematically measure the "durability" of AI research methods by comparing their performance against newer state-of-the-art models in the context of concept drift.

## Key Findings

- **Static models are not durable**: A model trained once and never updated shows a rapid decline in performance on a dataset with concept drift.
- **Adaptive models are more durable**: Models that are retrained, either periodically or based on drift detection, are more "durable" and maintain a higher level of performance over time.
- **Drift-based retraining is the most effective**: A model that is retrained only when a concept drift is detected achieves the best performance, demonstrating the value of adaptive methods.

## How to Reproduce

1.  **Set up the environment**:
    ```bash
    uv venv
    source .venv/bin/activate
    pip install -r requirements.txt 
    ```
2.  **Download the data**: The data is downloaded from Hugging Face. The preprocessing scripts handle this.
3.  **Preprocess the data**:
    ```bash
    python src/concatenate.py
    python src/preprocess_v3.py
    python src/sort_with_dask_v2.py
    ```
4.  **Run the experiment**:
    ```bash
    python src/run_experiment_v3.py
    ```
5.  **Analyze the results**:
    ```bash
    python src/analyze_results.py
    ```

## File Structure

- `planning.md`: The research plan.
- `src/`: Contains all the Python scripts.
- `datasets/`: Contains the raw and preprocessed data.
- `results/`: Contains the results of the experiment.
- `REPORT.md`: A detailed report of the research.

For more details, please see the `REPORT.md` file.
