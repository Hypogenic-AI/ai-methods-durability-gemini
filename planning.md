## Research Question
How can we systematically measure the "durability" of a disk failure prediction model in the presence of concept drift?

## Background and Motivation
The rapid pace of change in data distributions, a phenomenon known as "concept drift", is a major challenge in maintaining the performance of machine learning models in production. This is particularly true in AIOps, where models are used to monitor and predict the health of complex systems like hard disk fleets. A model that is accurate at the time of deployment may become obsolete as the characteristics of the data change over time. This project aims to develop a systematic way to measure the "durability" of different methods for handling concept drift in the context of disk failure prediction.

## Hypothesis Decomposition
*   **Hypothesis 1:** A simple model for disk failure prediction, trained once on historical data, will show a significant degradation in performance when evaluated on data from a later time period.
*   **Hypothesis 2:** Methods that explicitly handle concept drift, either by periodic retraining or by using drift detectors, will be more "durable" and maintain a higher level of performance over time.
*   **Hypothesis 3:** More advanced, state-of-the-art methods like McUDI will offer a better trade-off between performance and the cost of retraining compared to simpler methods.
*   **Definition of "Durability":** For this research, "durability" will be a qualitative measure based on the rate of performance decay over time and the computational cost (number of retrainings) required to maintain a certain level of performance.

## Proposed Methodology

### Approach
The experiment will simulate a real-world, online learning scenario where a model is used to predict disk failures based on the Backblaze Hard Drive Stats dataset from 2015. The dataset will be processed chronologically, and different methods for handling concept drift will be compared.

### Experimental Steps
1.  **Data Preparation:**
    *   Load the Backblaze Hard Drive Stats dataset for 2015.
    *   Perform necessary preprocessing and feature engineering. This will likely involve selecting relevant SMART features, handling missing values, and creating a binary failure label. The notebooks in the `code/mcudi_implementation` will be used as a guide.
    *   The data will be split into temporal chunks, for example, by week, to simulate the online arrival of data.

2.  **Baseline Model (Static):**
    *   Train a baseline model (e.g., `river.linear_model.LogisticRegression`) on the first chunk of data (e.g., the first month).
    *   Evaluate the model's performance (AUC-ROC) on all subsequent chunks of data without any retraining. This will serve as the baseline for performance degradation.

3.  **Periodic Retraining:**
    *   Train a model on the first chunk of data.
    *   Retrain the model at fixed intervals (e.g., every month) by adding the new data to the training set.
    *   Evaluate the model's performance over time.

4.  **Drift-based Retraining:**
    *   Train a model on the first chunk of data.
    *   Use a concept drift detector from the `river` library (e.g., `ADWIN`) to monitor the model's performance or the data distribution.
    *   Trigger retraining only when a drift is detected.
    *   Evaluate the model's performance and the number of retrainings over time.

5.  **State-of-the-Art Method (McUDI):**
    *   Adapt the McUDI implementation from the `code/mcudi_implementation` repository.
    *   Use McUDI to detect concept drift and trigger retraining.
    *   Evaluate the model's performance and the number of retrainings over time.

### Baselines
*   **Static Model:** A `river.linear_model.LogisticRegression` model trained once and never updated. This represents the lower bound of performance.
*   **Periodic Retraining:** A model that is retrained at regular intervals. This is a common industry practice.
*   **Drift-based Retraining:** A model that is retrained based on signals from a standard drift detection algorithm from the `river` library.
*   **McUDI:** The method proposed in the McUDI paper, used as a state-of-the-art baseline.

### Evaluation Metrics
*   **Predictive Performance:** The primary metric will be the **Area Under the Receiver Operating Characteristic Curve (AUC-ROC)**, which is suitable for imbalanced classification tasks like failure prediction.
*   **Cost of Maintenance:** The **number of retrainings** will be used as a proxy for the computational cost and operational complexity of maintaining the model.
*   **Drift Detection:** For methods that use drift detection, we will also track the **number of detected drifts**.

### Statistical Analysis Plan
The primary output will be a plot of the AUC-ROC score over time (e.g., per week) for each of the methods. This will provide a visual comparison of their durability. We will also present a table summarizing the total number of retrainings for each method, along with the average AUC-ROC over the entire period.

## Expected Outcomes
*   The static model's performance is expected to degrade significantly over time.
*   Periodic retraining should lead to better performance than the static model, but at a higher computational cost.
*   Drift-based retraining and McUDI are expected to provide a good balance between performance and cost, maintaining high AUC-ROC scores while requiring fewer retrainings than the periodic approach.
*   McUDI may outperform the standard drift detection methods from `river` in terms of finding a better trade-off between performance and cost.

## Timeline and Milestones
*   **Phase 1: Planning (0.5 hours):** Complete this document.
*   **Phase 2: Implementation (3 hours):**
    *   Set up the environment and install dependencies.
    *   Implement the data preparation pipeline.
    *   Implement the experimental loop for all four methods.
*   **Phase 3: Analysis (1.5 hours):**
    *   Run the experiments and collect the results.
    *   Generate plots and tables.
    *   Analyze the results and draw conclusions.
*   **Phase 4: Documentation (1 hour):**
    *   Write the final `REPORT.md` and `README.md`.

## Potential Challenges
*   **Data Preprocessing:** The Backblaze dataset is known to be noisy and requires careful preprocessing. The feature engineering part might be time-consuming.
*   **Adapting McUDI:** The code from the McUDI repository might need significant adaptation to fit into the experimental framework.
*   **Computational Cost:** The experiments might be computationally intensive, especially the retraining parts. The data size might need to be downsampled if the experiments take too long to run.

## Success Criteria
The research will be considered successful if it produces:
1.  A clear quantitative comparison of the performance of the different methods over time, presented in plots and tables.
2.  An analysis of the trade-offs between predictive performance and the cost of maintenance for each method.
3.  A well-documented and reproducible experimental pipeline for measuring the durability of models for disk failure prediction.