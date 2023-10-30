# Machine Learning Analysis README

This repository contains code and analysis related to machine learning models for predicting loan statuses based on financial data.

## Overview

The primary goal of this analysis was to predict loan statuses (healthy or high-risk) utilizing machine learning models. The dataset used includes information such as loan size, interest rates, borrower incomes, and other financial features. The analysis focused on predicting whether a loan is healthy or high-risk based on the provided data.

### Key Steps in the Analysis

1. **Data Exploration and Preparation**: Loaded data from the 'lending_data.csv' file into a Pandas DataFrame, created labels and features, and checked the balance of the labels variable.
2. **Original Model Creation**: Developed a Logistic Regression model using the original data and assessed its performance metrics.
3. **Oversampling and Model Refinement**: Balanced the training data using the RandomOverSampler module from the [imbalanced-learn](https://imbalanced-learn.org/stable/) library. Created and evaluated a Logistic Regression model with the resampled data.

### Libraries Used

The key libraries used in this analysis include:
- [Pandas](https://pandas.pydata.org/docs/): For data manipulation and analysis.
- [scikit-learn](https://scikit-learn.org/stable/): Used for building machine learning models.
- [imbalanced-learn](https://imbalanced-learn.org/stable/): Specifically employed for dealing with imbalanced datasets in machine learning.

## Results

### Model 1: Logistic Regression with Original Data
**Accuracy**: 99.18%

**Confusion Matrix:**
|             | Predicted 0 | Predicted 1 |
|-------------|-------------|-------------|
| Actual 0    | 18663       | 102         |
| Actual 1    | 56          | 563         |

**Classification Report:** 
|             | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| healthy_loan| 1.00      | 0.99   | 1.00     | 18765   |
| high_risk_loan| 0.85     | 0.91   | 0.88     | 619     |
| Accuracy    |           |        |          | 0.99    |

### Model 2: Logistic Regression with Resampled Data
**Accuracy**: 99.38%

**Confusion Matrix:**
|             | Predicted 0 | Predicted 1 |
|-------------|-------------|-------------|
| Actual 0    | 18649       | 116         |
| Actual 1    | 4           | 615         |

**Classification Report:** 
|             | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| healthy_loan| 1.00      | 0.99   | 1.00     | 18765   |
| high_risk_loan| 0.84     | 0.99   | 0.91     | 619     |
| Accuracy    |           |        |          | 0.99    |

## Conclusion

Both models showed strong performance in predicting loan statuses. The resampled model demonstrated slightly better performance in identifying high-risk loans. Choosing a model may depend on the emphasis of correctly predicting high-risk loans. If a balanced prediction of both healthy and high-risk loans is essential, the model trained with resampled data is recommended.
