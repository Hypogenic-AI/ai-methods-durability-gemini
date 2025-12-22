## Resources Catalog

### Summary
This document catalogs all resources gathered for the research project, including papers, datasets, and code repositories.

### Papers
Total papers downloaded: 3

| Title | Authors | Year | File | Key Info |
|-------|---------|------|------|----------|
| The curse of recursion: Training on generated data makes models forget | Ilia Shumailov, et al. | 2023 | papers/2305.17493_the_curse_of_recursion.pdf | Introduces the concept of "model collapse." |
| Learning under Concept Drift: A Review | Jie Lu, et al. | 2018 | papers/2004.05785_learning_under_concept_drift.pdf | A comprehensive review of concept drift. |
| McUDI: A Model-Centric Unsupervised Degradation Indicator for AIOps Models | Lorena Poenaru-Olaru, et al. | 2024 | papers/2401.14093_mcudi.pdf | Proposes McUDI, an unsupervised model degradation indicator. |

See papers/README.md for detailed descriptions.

### Datasets
Total datasets downloaded: 0

| Name | Source | Size | Task | Location | Notes |
|------|--------|------|------|----------|-------|
| Backblaze Disk Stats | HuggingFace | ~7M (2015) | Classification | datasets/ | Download instructions are in datasets/README.md. The automatic download may fail. |
| Google Cluster Traces | GitHub | ~2.4TB | Classification | datasets/ | Download instructions are in datasets/README.md. Requires Google Cloud. |

See datasets/README.md for detailed descriptions.

### Code Repositories
Total repositories cloned: 0

| Name | URL | Purpose | Location | Notes |
|------|-----|---------|----------|-------|
| McUDI | Not found | Baseline impl | code/ | The code for the McUDI model was not found. |

See code/README.md for detailed descriptions.

### Resource Gathering Notes

#### Search Strategy
I used a combination of `google_web_search`, `web_fetch`, and direct searches on arXiv and GitHub to find relevant resources. I started by searching for broad terms like "AI model durability" and then narrowed down my search to more specific terms like "model decay," "concept drift," and "AI aging."

#### Selection Criteria
I selected papers that were highly relevant to the research topic and were published in reputable venues. I prioritized papers that were recent and had code available. For datasets, I looked for publicly available datasets that have been used in previous research on model degradation.

#### Challenges Encountered
The main challenge I encountered was finding and downloading datasets. The Google Cluster Traces dataset is not easily downloadable, and the Backblaze Disk Stats dataset has schema inconsistencies that prevent automatic download. I also had difficulty finding the code for the McUDI model.

#### Gaps and Workarounds
I was unable to download the datasets automatically. As a workaround, I have provided manual download instructions in the `datasets/README.md` file. I was also unable to find the code for the McUDI model. I have documented this in the `code/README.md` file.

### Recommendations for Experiment Design

Based on gathered resources, recommend:

1. **Primary dataset(s)**: The Backblaze Disk Stats dataset is the most promising dataset for this research, as it is publicly available and has been used in previous research. The Google Cluster Traces dataset is also a good option, but it is more difficult to obtain.
2. **Baseline methods**: We should use periodic retraining and a static model as baselines for our experiments.
3. **Evaluation metrics**: We should use a combination of drift detection accuracy, model performance preservation, and label costs to evaluate our methods.
4. **Code to adapt/reuse**: Since the code for McUDI was not found, we will need to implement it ourselves based on the description in the paper. We can also reuse the code for periodic retraining from other open-source projects.
