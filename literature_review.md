## Literature Review

### Research Area Overview
[Brief overview of the research area based on papers read]

### Key Papers

#### Paper 1: Learning under Concept Drift: A Review
- **Authors**: Jie Lu, Anjin Liu, Fan Dong, Feng Gu, João Gama, and Guangquan Zhang
- **Year**: 2020
- **Source**: arXiv:2004.05785
- **Key Contribution**: Establishes a framework for learning under concept drift, comprising three main components: concept drift detection, concept drift understanding, and concept drift adaptation.
- **Methodology**: This is a review paper, so it surveys existing methodologies.
- **Datasets Used**: The paper lists and discusses 10 popular synthetic datasets and 14 publicly available benchmark datasets for evaluating learning algorithms under concept drift.
- **Results**: The paper summarizes the state-of-the-art and provides a comprehensive overview of the field.
- **Code Available**: No.
- **Relevance to Our Research**: This paper provides a comprehensive background and a framework for the research. It is a foundational resource for understanding the problem of concept drift and the existing approaches to address it.

#### Paper 2: The Curse of Recursion: Training on Generated Data Makes Models Forget
- **Authors**: Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson
- **Year**: 2023
- **Source**: arXiv:2305.17493
- **Key Contribution**: Introduces the concept of "model collapse," a degenerative process where generative models forget the true underlying data distribution when trained on model-generated content.
- **Methodology**: The paper provides a theoretical analysis of model collapse and demonstrates it empirically on Variational Autoencoders (VAEs), Gaussian Mixture Models (GMMs), and Large Language Models (LLMs).
- **Datasets Used**: The paper uses synthetic data and standard datasets like MNIST and wikitext2.
- **Results**: The paper shows that model collapse is a real phenomenon and that access to genuine human-generated content is essential to avoid it.
- **Code Available**: No.
- **Relevance to Our Research**: This paper introduces the core concept of "model collapse", which is a key mechanism for the loss of model durability. It is a foundational paper for the research hypothesis.

#### Paper 3: Unsupervised Concept Drift Detection with a Discriminative Classifier
- **Authors**: Lorena Poenaru-Olaru, Luis Cruz, Jan Rellermeyer and Arie van Deursen
- **Year**: 2024
- **Source**: arXiv:2401.14093
- **Key Contribution**: Proposes McUDI, a model-centric unsupervised degradation indicator for AIOps solutions.
- **Methodology**: McUDI computes the feature importance ranking from a trained AIOps model, selects the most important features, and then applies the Kolmogorov-Smirnov (KS) statistical test on the data distribution of these features to identify drift.
- **Datasets Used**: Google Cluster Traces and Backblaze Disk Stats datasets.
- **Results**: McUDI can reduce the number of samples that require annotation for retraining while achieving similar performance to periodic retraining.
- **Code Available**: Yes, at https://github.com/LorenaPoenaru/aiops_failure_prediction
- **Relevance to Our Research**: This paper provides a concrete and recent method for unsupervised model degradation detection, which is directly applicable to the research hypothesis. It also provides a baseline for comparison.

#### Paper 4: One or Two Things We know about Concept Drift -- A Survey on Monitoring Evolving Environments
- **Authors**: Fabian Hinder, Valerie Vaquet, Barbara Hammer
- **Year**: 2023
- **Source**: arXiv:2310.15826
- **Key Contribution**: Provides a literature review focusing on concept drift in unsupervised data streams, which is a less-covered area. It also provides a taxonomy of existing work and precise mathematical definitions.
- **Methodology**: This is a review paper.
- **Datasets Used**: The paper contains standardized experiments on parametric artificial datasets to allow for a direct comparison of different strategies.
- **Results**: The paper provides a systematic analysis of different drift detection and localization schemes and provides guidelines for their usage.
- **Code Available**: No.
- **Relevance to Our Research**: This paper complements the broader review paper by focusing on the unsupervised setting, which is highly relevant to the research hypothesis. It provides a more in-depth look at the specific problem of detecting drift without labels.

#### Paper 5: Position: Model Collapse Does Not Mean What You Think
- **Authors**: Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo
- **Year**: 2025
- **Source**: arXiv:2503.03150
- **Key Contribution**: This position paper argues that the term "model collapse" is ill-defined and that the narrative around it is oversimplified. It identifies eight distinct definitions of model collapse in the literature.
- **Methodology**: The paper is a critical review and analysis of the existing literature on model collapse.
- **Datasets Used**: The paper does not use any new datasets, but it analyzes the datasets and methodologies used in the papers it reviews.
- **Results**: The paper concludes that many predicted claims of model collapse rely on unrealistic assumptions and that the focus should be on more specific and likely harms.
- **Code Available**: No.
- **Relevance to Our Research**: This paper provides a critical perspective on the core concept of the research. It is important for framing the research question and for being precise in the definition of "durability" and "degradation".

#### Paper 6: A Tale of Tails: Model Collapse as a Change of Scaling Laws
- **Authors**: Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, Julia Kempe
- **Year**: 2024
- **Source**: arXiv:2402.07043
- **Key Contribution**: Develops a theoretical framework of model collapse through the lens of scaling laws.
- **Methodology**: The paper provides a theoretical analysis of how scaling laws are affected by the introduction of synthetic data. It validates its theory with large-scale experiments using a transformer on an arithmetic task and text generation with Llama2.
- **Datasets Used**: Synthetic data and Wikitext-103.
- **Results**: The paper shows that even a small fraction of synthetic data can lead to model collapse and that larger training sets may not enhance performance in such scenarios.
- **Code Available**: No.
- **Relevance to Our Research**: This paper provides a theoretical framework for understanding and quantifying model collapse, which is a key aspect of measuring model durability. It provides a more formal way to reason about the degradation of models.

### Research Area Overview

The research area is concerned with the degradation of AI models over time. This phenomenon has been described as "concept drift" in the data stream mining community and, more recently, as "model collapse" in the context of large generative models. The core problem is that the statistical properties of the data change over time, which can lead to a decline in model performance. The goal of the research in this area is to develop methods to measure, understand, and mitigate this degradation to ensure the "durability" of AI models.



### Common Methodologies

*   **Concept Drift Detection:** This is the most common methodology. It involves using statistical tests to detect changes in the data distribution. Common algorithms include the Drift Detection Method (DDM), the Early Drift Detection Method (EDDM), and the ADaptive WINdowing (ADWIN). The Kolmogorov-Smirnov (KS) test is also used.

*   **Model-centric approaches:** These methods use the model's internal states or feature importances to detect degradation. An example is McUDI, which monitors the distribution of the most important features of a model.

*   **Scaling Laws:** This is a more recent approach that analyzes the performance of models as a function of data size, model size, and other parameters. It is used to understand and predict model collapse in large generative models.

*   **Ensemble methods:** Using multiple models is a common strategy to improve robustness and handle concept drift.



### Standard Baselines

*   **Periodic retraining:** Retraining the model at fixed intervals is the most common baseline.

*   **Static model:** A model that is never retrained is used as a lower bound on performance.

*   **Standard drift detection algorithms:** Algorithms like DDM, EDDM, and ADWIN are often used as baselines to compare new methods against.



### Evaluation Metrics

*   **Drift detection metrics:** For evaluating drift detection algorithms, the common metrics are True Positive Rate (the number of correctly detected drifts), False Positive Rate (the number of false alarms), and the delay of detection.

*   **Model performance metrics:** To evaluate the impact of drift on model performance, standard metrics like accuracy, AUC-ROC, and F1-score are used for classification tasks, and perplexity is used for language models.

*   **Labeling cost:** In real-world scenarios, the cost of acquiring labels is an important consideration. The number of labels required for retraining is often used as a metric.



### Datasets in the Literature

The literature uses a wide variety of datasets to evaluate concept drift algorithms.

*   **Synthetic datasets:** These are used for controlled experiments where the type and time of drift are known. Common synthetic datasets include STAGGER, SEA, Rotating Hyperplane, and Random RBF.

*   **Real-world datasets:** These are used to validate the practical relevance of the proposed methods. Common real-world datasets include Electricity, Airlines, NOAA Weather, Covertype, and KDDCup'99.

*   **AIOps datasets:** For the specific domain of AIOps, datasets like the Google Cluster Traces and the Backblaze Disk Stats dataset are used.

*   **Text datasets:** For studying model collapse in LLMs, text datasets like wikitext-103 are used.



### Gaps and Opportunities

*   **Lack of a unified definition of model degradation:** As pointed out in the position paper by Schaeffer et al., there is no single, agreed-upon definition of model collapse or durability. This makes it difficult to compare different methods and to reason about the problem in a precise way.

*   **Unsupervised methods:** Most of the research on concept drift has focused on supervised settings where labels are available. There is a need for more research on unsupervised methods that can detect drift without access to labels.

*   **Real-world validation:** Many proposed methods are only evaluated on synthetic datasets. There is a need for more extensive validation on real-world data to demonstrate their practical relevance.

- **Explainability:** Understanding *why* a model is degrading is still a major challenge. Most drift detection methods only signal *that* a drift has occurred, but they do not provide any explanation of the cause.



### Recommendations for Our Experiment

Based on the literature review, the following recommendations can be made for the experiment:

- **Recommended datasets**: The **Backblaze Hard Drive Stats** dataset is a good choice for the failure prediction task, as it is a real-world dataset known to exhibit concept drift. The **Newsroom** dataset is a good choice for the text generation task, as it is a large-scale real-world dataset with a temporal component.

- **Recommended baselines**: For comparison, the experiment should include a **static model** (no retraining), **periodic retraining**, and a standard drift detection algorithm like **DDM** or **ADWIN** from the `river` library.

- **Recommended metrics**: The performance of the models should be evaluated using **AUC-ROC** for the Backblaze dataset and **perplexity** for the Newsroom dataset. The cost of labeling should also be tracked.

- **Methodological considerations**: The experiment should use a clear and precise definition of "durability" and "degradation". Given the lack of a unified definition in the literature, it is important to be explicit about the definitions used in this research.