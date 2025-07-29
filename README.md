<p align="center">
  <img src="web_images/preview.png" alt="Diabetes App Cover" />
</p>

# 🩺 Diabetes Prediction App (XGBoost-powered)

This web app predicts the likelihood of diabetes using patient information such as glucose level, BMI, age, and more. Built with **Streamlit**, trained on a cleaned and scaled dataset, and deployed with an **XGBoost** model for high accuracy.

---
## Overview

This web app allows users to input health data (glucose, BMI, age, etc.) and get predictions on diabetes risk. It gives personalized advice and visual feedback based on the result.

Built with:

- Python
- Streamlit
- scikit-learn
- XGBoost

---

## Data Preprocessing

- Handled missing and zero values carefully.
- Applied `StandardScaler` to normalize the data.
- Visualized feature distribution and checked for outliers.

---

## Feature Analysis

- Used correlation heatmap to study features.
- Found **Glucose**, **BMI**, and **Age** to have the strongest correlation with diabetes.
- Removed irrelevant features and kept the most impactful ones.

---

## 🤖 Model Development

### Tried multiple classifiers:

- Logistic Regression
- K-Nearest Neighbors
- Decision Tree
- Random Forest
- **XGBoost (Best performance)**

### Why XGBoost?

- More accurate for tabular medical data.
- Handles imbalanced and noisy data better.
- Allows fine control via hyperparameters.

---

