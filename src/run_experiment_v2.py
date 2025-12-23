
import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score
from river import linear_model, drift, compose, preprocessing
from tqdm import tqdm
import os
import dask.dataframe as dd

def run_experiment_v2():
    """
    Main function to run the durability experiment, optimized for speed.
    """
    # Load the dataset
    print("Loading preprocessed data...")
    ddf = dd.read_parquet("datasets/backblaze_2015_preprocessed.parquet")

    # Define features and target
    features = [col for col in ddf.columns if 'smart' in col]
    target = 'failure'

    # --- Initialize models ---
    static_model = compose.Pipeline(preprocessing.StandardScaler(), linear_model.LogisticRegression())
    periodic_model = compose.Pipeline(preprocessing.StandardScaler(), linear_model.LogisticRegression())
    drift_model = compose.Pipeline(preprocessing.StandardScaler(), linear_model.LogisticRegression())
    adwin = drift.ADWIN()
    
    # --- Store results ---
    results = []
    
    # Get the weeks
    ddf['week'] = ddf['date'].dt.isocalendar().week
    weeks = ddf['week'].unique().compute().to_numpy()

    # --- Train static model on first week ---
    print("Training static model on the first week...")
    first_week_df = ddf[ddf['week'] == weeks[0]].compute()
    X_first = first_week_df[features].fillna(0)
    y_first = first_week_df[target]
    for i in tqdm(range(len(X_first)), desc="Training static model"):
        static_model.learn_one(X_first.iloc[i].to_dict(), y_first.iloc[i])

    # --- Main experiment loop ---
    for week in tqdm(weeks, desc="Processing weeks"):
        chunk = ddf[ddf['week'] == week].compute()
        X = chunk[features].fillna(0)
        y = chunk[target]

        # --- Static Model ---
        y_pred_static = [static_model.predict_proba_one(X.iloc[i].to_dict()).get(True, 0.5) for i in range(len(X))]
        auc_static = roc_auc_score(y, y_pred_static) if len(np.unique(y)) > 1 else 0.5
        results.append({'week': week, 'model': 'static', 'auc': auc_static, 'retrained': False})

        # --- Periodic Retraining Model ---
        retrained_periodic = (week % 4 == 0)
        if retrained_periodic:
            for i in range(len(X)):
                periodic_model.learn_one(X.iloc[i].to_dict(), y.iloc[i])
        
        y_pred_periodic = [periodic_model.predict_proba_one(X.iloc[i].to_dict()).get(True, 0.5) for i in range(len(X))]
        auc_periodic = roc_auc_score(y, y_pred_periodic) if len(np.unique(y)) > 1 else 0.5
        results.append({'week': week, 'model': 'periodic', 'auc': auc_periodic, 'retrained': retrained_periodic})

        # --- Drift-based Retraining Model ---
        retrained_drift = False
        for i in range(len(X)):
            y_pred_drift_one = drift_model.predict_proba_one(X.iloc[i].to_dict()).get(True, 0.5)
            error = 1 - (1 if y_pred_drift_one > 0.5 and y.iloc[i] == 1 else 0)
            adwin.update(error)
            if adwin.drift_detected:
                retrained_drift = True
            
            # Always learn
            drift_model.learn_one(X.iloc[i].to_dict(), y.iloc[i])

        y_pred_drift = [drift_model.predict_proba_one(X.iloc[i].to_dict()).get(True, 0.5) for i in range(len(X))]
        auc_drift = roc_auc_score(y, y_pred_drift) if len(np.unique(y)) > 1 else 0.5
        results.append({'week': week, 'model': 'drift', 'auc': auc_drift, 'retrained': retrained_drift})

    # --- Save results ---
    results_df = pd.DataFrame(results)
    results_df.to_csv("results/experiment_results.csv", index=False)
    print("Experiment finished. Results saved to results/experiment_results.csv")


if __name__ == "__main__":
    if not os.path.exists("results"):
        os.makedirs("results")
    run_experiment_v2()

