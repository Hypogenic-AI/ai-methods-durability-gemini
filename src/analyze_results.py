
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_results(results_file):
    """
    Analyzes the experiment results and creates plots.
    """
    print(f"Loading results from {results_file}...")
    df = pd.read_csv(results_file)

    # --- Plot AUC over time ---
    print("Plotting AUC over time...")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='week', y='auc', hue='model')
    plt.title('Model Performance Over Time')
    plt.xlabel('Week')
    plt.ylabel('AUC Score')
    plt.grid(True)
    plt.savefig('results/auc_over_time.png')
    print("Saved plot to results/auc_over_time.png")

    # --- Print summary statistics ---
    print("\nSummary Statistics:")
    summary = df.groupby('model')['auc'].mean().reset_index()
    print(summary)
    
    summary.to_csv('results/summary_statistics.csv', index=False)
    print("\nSaved summary statistics to results/summary_statistics.csv")


if __name__ == "__main__":
    results_file = "results/experiment_results_v3.csv"
    analyze_results(results_file)

