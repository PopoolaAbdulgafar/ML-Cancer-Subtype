ML-Cancer-Subtype

Machine learning analysis of TCGA breast cancer gene-expression data for molecular subtype classification using the PAM50 classification system.

Project Overview

This project applies machine learning and dimensionality-reduction techniques to gene-expression data from The Cancer Genome Atlas (TCGA) Breast Invasive Carcinoma (BRCA) dataset.

The main objective is to investigate whether gene-expression patterns can be used to distinguish breast cancer molecular subtypes and to identify genes that contribute strongly to classification.

Breast Cancer Subtypes

The analysis uses the following PAM50 molecular subtypes:

- Luminal A (LumA)
- Luminal B (LumB)
- Basal
- HER2
- Normal

Dataset

- Dataset: TCGA-BRCA
- Source: UCSC Xena
- Gene-expression features: 20,530 genes
- Samples used: 956 samples after removing samples with missing subtype labels
- Subtype labels: PAM50Call_RNAseq

Workflow

The project includes:

1. Data preprocessing and preparation
2. Variance-based gene selection
3. Statistical analysis
4. Spearman correlation analysis
5. Hierarchical clustering
6. K-Means clustering
7. Principal Component Analysis (PCA)
8. t-SNE dimensionality reduction
9. UMAP visualization
10. Logistic Regression classification
11. Random Forest classification
12. Hyperparameter tuning using GridSearchCV
13. Classification performance evaluation
14. Confusion matrix analysis
15. ROC and AUC analysis
16. Random Forest feature-importance analysis
17. Biological interpretation of the top important genes

Machine Learning

Two supervised classification approaches were evaluated:

- Logistic Regression
- Random Forest

Random Forest hyperparameters were optimized using GridSearchCV. The best-performing configuration was then used for the final model evaluation.

Performance was assessed using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- ROC-AUC

Dimensionality Reduction

PCA and UMAP were used to visualize the structure of the breast cancer samples and examine the separation of PAM50 molecular subtypes.

PCA was also used to reduce the dimensionality of the gene-expression data before downstream visualization.

Feature Importance

Random Forest feature importance was used to identify genes that contributed strongly to subtype classification.

The top 20 genes identified by the final model were:

Rank| Gene
1| TBC1D9
2| ROPN1B
3| ASPM
4| VGLL1
5| STAC
6| TRIM29
7| TPX2
8| CENPA
9| BBOX1
10| TTK
11| UBE2T
12| FOXC1
13| DEGS2
14| FAM72B
15| MRAS
16| ACADSB
17| ESPL1
18| SFRP1
19| CCNA2
20| FAM54A

Several of these genes are involved in processes related to cell-cycle regulation, mitosis, chromosome segregation, proliferation, and cellular signaling. These patterns provide biological context for the molecular differences detected by the classifier.

Feature importance indicates predictive usefulness within the model; it does not by itself establish that a gene is a causal driver or a definitive subtype-specific biomarker.

Repository Structure

ML-Cancer-Subtype/
│
├── data/
│ └── Dataset files and data preparation resources
│
├── notebooks/
│ └── Analysis and machine learning notebooks
│
├── results/
│ ├── PCA plots
│ ├── UMAP plots
│ ├── Confusion matrix
│ └── Feature-importance plots
│
├── models/
│ └── rf_best.pkl
│
└── src/
    └── Python source code

Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- UMAP
- Jupyter Notebook
- Git & GitHub

Key Findings

The analysis demonstrates that machine-learning methods can capture meaningful patterns in TCGA-BRCA gene-expression data for PAM50 subtype classification.

The Random Forest model identified a set of genes with high predictive importance, with several top features associated with biological processes such as proliferation and cell-cycle regulation.

The PCA and UMAP visualizations provide additional insight into the molecular structure and distribution of the breast cancer subtypes.

Disclaimer

This project is intended for educational and research purposes. The results should not be interpreted as a clinical diagnostic tool or as evidence for clinical decision-making.
