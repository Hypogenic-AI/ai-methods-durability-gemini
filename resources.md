## Resources Catalog

### Summary
This document catalogs all resources gathered for the research project, including papers, datasets, and code repositories.

### Papers
Total papers downloaded: 6

| Title | Authors | Year | File | Key Info |
|-------|---------|------|------|----------|
| Learning under Concept Drift: A Review | Jie Lu, et al. | 2020 | papers/2004.05785_learning_under_concept_drift.pdf | A comprehensive review of concept drift research. |
| The Curse of Recursion: Training on Generated Data Makes Models Forget | Ilia Shumailov, et al. | 2023 | papers/2305.17493_the_curse_of_recursion.pdf | Introduces the concept of "model collapse". |
| Unsupervised Concept Drift Detection with a Discriminative Classifier | Lorena Poenaru-Olaru, et al. | 2024 | papers/2401.14093_mcudi.pdf | Proposes the McUDI method for unsupervised drift detection. |
| One or Two Things We know about Concept Drift | Fabian Hinder, et al. | 2023 | papers/2310.15826_one_or_two_things_we_know_about_concept_drift.pdf | A survey on concept drift in unsupervised data streams. |
| Position: Model Collapse Does Not Mean What You Think | Rylan Schaeffer, et al. | 2025 | papers/2503.03150_model_collapse_does_not_mean_what_you_think.pdf | A position paper that critically examines the concept of model collapse. |
| A Tale of Tails: Model Collapse as a Change of Scaling Laws | Elvis Dohmatob, et al. | 2024 | papers/2402.07043_a_tale_of_tails.pdf | Provides a theoretical framework for understanding model collapse in terms of scaling laws. |

See papers/README.md for detailed descriptions.

### Datasets
Total datasets identified: 2

| Name | Source | Size | Task | Location | Notes |
|------|--------|------|------|----------|-------|
| Backblaze Hard Drive Stats | HuggingFace | ~7M (2015) | Failure Prediction | datasets/backblaze_drive_stats_2015/ | Download script failed. Manual download required. |
| Newsroom | HuggingFace | 1.3M | Summarization | datasets/newsroom/ | Download script failed. Manual download required. |

See datasets/README.md for detailed descriptions.

### Code Repositories
Total repositories cloned: 2

| Name | URL | Purpose | Location | Notes |
|------|-----|---------|----------|-------|
| McUDI Implementation | https://github.com/LorenaPoenaru/aiops_failure_prediction | Implementation of the McUDI paper. | code/mcudi_implementation/ | Contains the code for the McUDI paper. |
| River | https://github.com/online-ml/river | A Python library for online machine learning. | code/river/ | Contains implementations of concept drift detection algorithms. |

See code/README.md for detailed descriptions.

### Resource Gathering Notes

#### Search Strategy
The resource gathering process started with a broad search for the term "AI model durability" and then narrowed down to more specific terms like "concept drift", "model collapse", and "drift detection". I used Google Scholar and the arXiv search to find relevant papers. For datasets, I searched Hugging Face. For code, I searched for repositories linked in the papers and also for general-purpose libraries.

#### Selection Criteria
The papers were selected based on their relevance to the research topic, their recency, and their citation count. The datasets were selected based on their suitability for the research questions and their availability. The code repositories were selected based on their relevance to the papers and the availability of implementations of common algorithms.

#### Challenges Encountered
The main challenge was the automatic download of datasets. Both selected datasets failed to download automatically due to issues with the dataset format on Hugging Face. This was addressed by providing manual download instructions. Another challenge was the difficulty in finding code repositories for the "model collapse" papers.

#### Gaps and Workarounds
The main gap is the lack of a readily available implementation for the "model collapse" papers. This was worked around by cloning the `river` library, which contains implementations of many concept drift detection algorithms that can be used as baselines.

### Recommendations for Experiment Design

Based on the gathered resources, I recommend:

1.  **Primary dataset(s)**: **Backblaze Hard Drive Stats** for the failure prediction task and **Newsroom** for the text generation task.
2.  **Baseline methods**: A static model, periodic retraining, and standard drift detection algorithms (DDM, EDDM, ADWIN) from the `river` library. The McUDI implementation can also be used as a more advanced baseline.
3.  **Evaluation metrics**: **AUC-ROC** for the failure prediction task and **perplexity** for the text generation task.
4.  **Code to adapt/reuse**: The `river` library can be used for implementing the baselines. The `mcudi_implementation` can be used to replicate the results of the McUDI paper and as a baseline.