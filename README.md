<p align="center">
  <img src="images/cover.png" alt="Diabetes App Cover" width="600"/>
</p>

# 🩺 Diabetes Prediction App (XGBoost-powered)

This web app predicts the likelihood of diabetes using patient information such as glucose level, BMI, age, and more. Built with **Streamlit**, trained on a cleaned and scaled dataset, and deployed with an **XGBoost** model for high accuracy.

---

## 🎯 Preview

| Patient at Risk | Healthy Patient |
|-----------------|-----------------|
| ![](images/diabetes_alert.gif) | ![](images/healthy_ok.png) |

> ✨ The app dynamically shows tips, GIFs, and positive messages depending on the prediction.

---

## 🧠 Model Development Process

### 📊 1. Data Cleaning & Scaling
- Handled zero/missing values appropriately.
- Applied `StandardScaler` to normalize the data.

### 📈 2. Correlation Analysis
A heatmap was used to analyze correlations between variables like:
- Glucose 🔼
- BMI 🧍‍♀️
- Age 🎂  
These had the highest impact on diabetes prediction.

### 🤖 3. Model Testing
I tested several models:
- Logistic Regression  
- SVM  
- Decision Tree  
- Random Forest  
- **XGBoost** ✅ (Best performance)

### 🔍 4. Hyperparameter Tuning
Used **GridSearchCV** to tune models, especially XGBoost:
```python
xgb = XGBClassifier(learning_rate=0.01, max_depth=4, n_estimators=500)
xgb.fit(X_train_scaled, y_train)
