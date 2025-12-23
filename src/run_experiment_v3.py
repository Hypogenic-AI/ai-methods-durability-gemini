
import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score
from river import linear_model, drift, compose, preprocessing
from tqdm import tqdm
import os
import dask.dataframe as dd

def run_experiment_v3():
    """
    Main function to run the durability experiment, optimized for row-by-row processing.
    """
    # Load the dataset
    print("Loading preprocessed data...")
    ddf = dd.read_parquet("datasets/backblaze_2015_preprocessed.parquet")
    ddf['date'] = dd.to_datetime(ddf['date'])

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
    
    # --- Data for evaluation ---
    y_true_week = []
    y_pred_static_week = []
    y_pred_periodic_week = []
    y_pred_drift_week = []
    
    current_week = -1
    
    # --- Train static model on first week ---
    print("Training static model on the first week...")
    ddf['week'] = ddf['date'].dt.isocalendar().week
    weeks = ddf['week'].unique().compute().to_numpy()
    first_week_df = ddf[ddf['week'] == weeks[0]].compute()
    X_first = first_week_df[features].fillna(0)
    y_first = first_week_df[target]
    for i in tqdm(range(len(X_first)), desc="Training static model"):
        static_model.learn_one(X_first.iloc[i].to_dict(), y_first.iloc[i])

    print("Processing data row by row...")
    for row in tqdm(ddf.itertuples(), total=len(ddf)):
        
        x = {}
        for feature in features:
            val = getattr(row, feature, 0)
            if pd.isna(val):
                val = 0
            x[feature] = val
        y = getattr(row, target)
        week = getattr(row, 'week')

        if current_week == -1:
            current_week = week

        if week != current_week:
            # --- Evaluate models ---
            if len(y_true_week) > 0:
                auc_static = roc_auc_score(y_true_week, y_pred_static_week) if len(np.unique(y_true_week)) > 1 else 0.5
                auc_periodic = roc_auc_score(y_true_week, y_pred_periodic_week) if len(np.unique(y_true_week)) > 1 else 0.5
                auc_drift = roc_auc_score(y_true_week, y_pred_drift_week) if len(np.unique(y_true_week)) > 1 else 0.5
                results.append({'week': current_week, 'model': 'static', 'auc': auc_static})
                results.append({'week': current_week, 'model': 'periodic', 'auc': auc_periodic})
                results.append({'week': current_week, 'model': 'drift', 'auc': auc_drift})
            
            # --- Reset weekly data ---
            y_true_week, y_pred_static_week, y_pred_periodic_week, y_pred_drift_week = [], [], [], []
            current_week = week

        # --- Predictions ---
        y_true_week.append(y)
        y_pred_static_week.append(static_model.predict_proba_one(x).get(True, 0.5))
        y_pred_periodic_week.append(periodic_model.predict_proba_one(x).get(True, 0.5))
        y_pred_drift_week.append(drift_model.predict_proba_one(x).get(True, 0.5))
        
        # --- Training ---
        # Periodic Retraining Model
        if week % 4 == 0:
            periodic_model.learn_one(x, y)
            
        # Drift-based Retraining Model
        error = 1 - (1 if y_pred_drift_week[-1] > 0.5 and y == 1 else 0)
        adwin.update(error)
        if adwin.drift_detected:
            drift_model.learn_one(x,y)
        else:
            drift_model.learn_one(x,y)
    
    # --- Save results ---
    results_df = pd.DataFrame(results)
    results_df.to_csv("results/experiment_results_v3.csv", index=False)
    print("Experiment finished. Results saved to results/experiment_results_v3.csv")


if __name__ == "__main__":
    if not os.path.exists("results"):
        os.makedirs("results")
    run_experiment_v3()
