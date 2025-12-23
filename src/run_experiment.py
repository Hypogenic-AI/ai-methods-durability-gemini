
import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score
from river import linear_model, drift, compose, preprocessing
from tqdm import tqdm
import os

def run_experiment():
    """
    Main function to run the durability experiment.
    """
    # Load the dataset
    print("Loading preprocessed data...")
    # The data is in a directory of parquet files, so we read it with dask
    import dask.dataframe as dd
    ddf = dd.read_parquet("datasets/backblaze_2015_preprocessed.parquet")
    
    print("Getting unique weeks from dask dataframe...")
    df_weeks = ddf['date'].dt.isocalendar().week.unique().compute().to_numpy()

    # --- Initialize models ---
    # Static model
    static_model = compose.Pipeline(
        preprocessing.StandardScaler(),
        linear_model.LogisticRegression()
    )
    static_model_trained = False

    # Periodic retraining model
    periodic_model = compose.Pipeline(
        preprocessing.StandardScaler(),
        linear_model.LogisticRegression()
    )
    
    # Drift-based retraining model
    drift_model = compose.Pipeline(
        preprocessing.StandardScaler(),
        linear_model.LogisticRegression()
    )
    adwin = drift.ADWIN()
    
    # --- Store results ---
    results = []

    # --- Main experiment loop ---
    for week in tqdm(df_weeks, desc="Processing weeks"):
        chunk = ddf[ddf['date'].dt.isocalendar().week == week].compute()
        
        # Define features and target
        features = [col for col in chunk.columns if 'smart' in col]
        target = 'failure'
        
        X = chunk[features]
        X = X.fillna(0)
        y = chunk[target]

        # --- Static Model ---
        if not static_model_trained:
            # Train on the first week
            if week == df_weeks[0]:
                for i in range(len(X)):
                    static_model.learn_one(X.iloc[i].to_dict(), y.iloc[i])
                static_model_trained = True
        
        # Test static model
        y_pred_static = [static_model.predict_proba_one(X.iloc[i].to_dict()).get(True, 0.5) for i in range(len(X))]
        auc_static = roc_auc_score(y, y_pred_static) if len(np.unique(y)) > 1 else 0.5
        
        results.append({'week': week, 'model': 'static', 'auc': auc_static, 'retrained': False})

        # --- Periodic Retraining Model ---
        # Train every 4 weeks
        if week % 4 == 0:
            for i in range(len(X)):
                periodic_model.learn_one(X.iloc[i].to_dict(), y.iloc[i])
            retrained_periodic = True
        else:
            retrained_periodic = False

        # Test periodic model
        y_pred_periodic = [periodic_model.predict_proba_one(X.iloc[i].to_dict()).get(True, 0.5) for i in range(len(X))]
        auc_periodic = roc_auc_score(y, y_pred_periodic) if len(np.unique(y)) > 1 else 0.5
        results.append({'week': week, 'model': 'periodic', 'auc': auc_periodic, 'retrained': retrained_periodic})

        # --- Drift-based Retraining Model ---
        retrained_drift = False
        for i in range(len(X)):
            # Test
            y_pred_drift_one = drift_model.predict_proba_one(X.iloc[i].to_dict()).get(True, 0.5)
            
            # Update drift detector
            error = 1 - (1 if y_pred_drift_one > 0.5 and y.iloc[i] == 1 else 0)
            adwin.update(error)
            
            # If drift is detected, retrain the model
            if adwin.drift_detected:
                drift_model.learn_one(X.iloc[i].to_dict(), y.iloc[i])
                retrained_drift = True
            else:
                 # just learn without retraining the whole model
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
    run_experiment()

