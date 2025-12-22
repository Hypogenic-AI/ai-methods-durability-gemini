## Research Question
Can we systematically measure the "durability" of an AI research method by comparing its performance over time and using newer methods to detect degradation?

## Background and Motivation
The rapid pace of AI research leads to a constant stream of new models and methods. This makes it difficult to know which published methods are still relevant and which have been effectively superseded. This research aims to develop a systematic way to measure the "shelf-life" or "durability" of an AI method. This will help researchers and practitioners focus on methods that provide lasting value.

## Hypothesis Decomposition
To test the main research question, I will focus on a specific, testable hypothesis:

*   **Hypothesis:** The performance of a predictive model trained on time-series data will degrade over time as the data distribution shifts (concept drift). This degradation can be detected by an unsupervised degradation indicator, thus providing a measure of the model's "durability".

## Proposed Methodology

### Approach
I will simulate the aging of an AI model by training it on an early portion of a time-series dataset and then evaluating it on later portions. I will use the Backblaze Hard Drive Stats dataset, as it contains daily snapshots of hard drive health metrics, which is ideal for studying concept drift.

I will implement a simple "older" model (Logistic Regression) and a "newer" method for detecting data degradation based on the McUDI paper. By comparing the model's actual performance degradation with the degradation predicted by the McUDI-inspired method, I can test if this is a valid way to measure durability.

### Experimental Steps
1.  **Data Acquisition and Preprocessing:**
    *   Download the Backblaze Drive Stats dataset for the year 2015 using the HuggingFace `datasets` library.
    *   Preprocess the data:
        *   Handle missing values.
        *   Select a subset of features for the model.
        *   Encode categorical features.
        *   Split the data chronologically into monthly batches.

2.  **"Older" Model Implementation:**
    *   Implement a Logistic Regression model using `scikit-learn`. This will serve as our "older" method.

3.  **Initial Model Training:**
    *   Train the Logistic Regression model on the first month of data (January 2015). This will be our initial "durable" model.

4.  **"Newer" Method Implementation (McUDI-inspired):**
    *   Implement the core logic of the McUDI degradation indicator. Based on the paper, this involves:
        *   Ranking features by importance (e.g., using the coefficients from the trained Logistic Regression model).
        *   For the most important features, perform a Kolmogorov-Smirnov (KS) test to compare the distribution of the feature in the training data (January 2015) with its distribution in a subsequent month's data.
        *   If the KS statistic is above a certain threshold for any of the key features, flag the model as potentially "degraded" for that month.

5.  **Evaluation Over Time:**
    *   For each subsequent month (February to December 2015):
        *   Evaluate the performance of the single, initially-trained Logistic Regression model on that month's data. Use metrics like AUC-ROC and F1-score.
        *   Run the McUDI-inspired degradation check to see if it flags that month's data as drifted.

6.  **Analysis:**
    *   Plot the model's performance (AUC-ROC) over the 12 months.
    *   On the same plot, indicate which months were flagged as "degraded" by the McUDI indicator.
    *   Analyze the correlation: Does the McUDI flag precede or coincide with a significant drop in model performance?

### Baselines
*   **Static Model:** The Logistic Regression model trained only on January 2015 data serves as our primary subject of study. Its changing performance over time is what we are trying to measure.
*   **Degradation Indicator:** The primary baseline for the degradation indicator is its own ability to predict a performance drop. Success is defined as the indicator's flags correlating with actual, measured performance drops.

### Evaluation Metrics
*   **Model Performance:**
    *   **AUC-ROC:** Area Under the Receiver Operating Characteristic Curve. This is a good metric for imbalanced classification tasks like failure prediction.
    *   **F1-Score:** The harmonic mean of precision and recall.
*   **Degradation Detection:**
    *   **Correlation:** We will look for a correlation between the McUDI degradation flags and the actual drop in the model's AUC-ROC.
    *   **Timeliness:** Does the degradation flag appear before the performance drops, giving a timely warning?

### Statistical Analysis Plan
*   I will use a rolling window to calculate the performance metrics to smooth out noise.
*   The KS-test p-value will be used to determine if a feature's distribution has significantly drifted. A significance level of p < 0.05 will be used.
*   I will visually inspect the plots for correlation and report on the observed relationship.

## Expected Outcomes
*   **Supporting the hypothesis:** I expect to see the logistic regression model's performance decrease over the months. I also expect the McUDI-based indicator to flag the months where the data distribution has shifted significantly, and that these flags will align with the periods of performance decline.
*   **Refuting the hypothesis:** The model's performance might not degrade significantly, or the McUDI indicator might fail to flag the months where performance does drop. This would suggest that this method of measuring durability is not effective for this use case.

## Timeline and Milestones
*   **Phase 2: Environment & Data Setup (1-2 hours):**
    *   Install dependencies.
    *   Download and preprocess the dataset.
*   **Phase 3: Implementation (2-3 hours):**
    *   Implement the Logistic Regression model.
    *   Implement the McUDI-inspired degradation indicator.
*   **Phase 4: Experimentation (1-2 hours):**
    *   Train the initial model.
    *   Run the evaluation loop for all months.
*   **Phase 5 & 6: Analysis & Documentation (1-2 hours):**
    *   Analyze the results.
    *   Create plots.
    *   Write the final `REPORT.md`.

## Potential Challenges
*   **Data Size:** The dataset might be large, requiring efficient data processing.
*   **Data Quality:** The data might have inconsistencies or require significant cleaning. The `datasets/README.md` already mentioned potential schema inconsistencies.
*   **McUDI Implementation:** Implementing McUDI from the paper might be challenging without a reference implementation. I will have to make some implementation choices based on my interpretation of the paper.
*   **Hyperparameter Tuning:** The KS-test threshold for flagging drift will need to be chosen carefully.

## Success Criteria
The research will be considered successful if I can demonstrate a clear correlation between the output of the McUDI-inspired degradation indicator and the measured performance of the "older" logistic regression model on the time-series dataset. This would provide evidence that this is a viable approach for systematically measuring the "durability" of an AI method.
