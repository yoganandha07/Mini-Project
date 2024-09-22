# Future Retail Sales Prediction Model

This project aims to predict future retail sales using machine learning models. The primary model used for this prediction is **XGBoost**, known for its high performance and flexibility in handling tabular datasets. 

## Project Overview

The goal of the project is to provide accurate sales forecasts for different products in a retail store, enabling better stock management and demand planning.

### Features
- **Feature Engineering**: Various features such as product categories, store information, and temporal aspects (e.g., day, month, year) have been used to improve model accuracy.
- **Model**: XGBoost was selected as the best performing model after comparison with other machine learning algorithms.
- **Performance**: The model has been evaluated using metrics such as RMSE (Root Mean Squared Error) and MAE (Mean Absolute Error).

## Dataset

The dataset used in this project contains historical sales data for multiple products. It includes the following columns:

- `Date`: The date of the sales transaction.
- `Store ID`: The unique identifier for the store.
- `Product ID`: The unique identifier for the product.
- `Sales`: The target variable representing the sales amount.
- **Additional Features**: Other features include store location, product category, and promotional information.

## Model Details

- **Algorithm**: XGBoost (Extreme Gradient Boosting)
- **Hyperparameters**: Various hyperparameters were tuned, including `n_estimators`, `max_depth`, `learning_rate`, and `subsample`.
  
### Model Pipeline
1. **Data Preprocessing**: Missing values handling, feature scaling, and encoding of categorical variables.
2. **Model Training**: The XGBoost model is trained on the preprocessed data.
3. **Evaluation**: Model performance is evaluated using RMSE, and MAE on the test dataset.
4. **Prediction**: Future sales are predicted based on the trained model.

## Installation and Usage

### Requirements

- Python 3.8+
- Jupyter Notebook or any Python IDE
- Required Libraries:
    - `xgboost`
    - `pandas`
    - `scikit-learn`
    - `matplotlib`

You can install the required libraries by running:

```bash
pip install -r requirements.txt
