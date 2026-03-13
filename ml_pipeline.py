# ml_pipeline.py - Yeh script model ko train aur save karegi

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib
import os

# --- 1. Data Loading ---
try:
    df = pd.read_csv('crop_revenue.csv')
    print("✅ Data successfully loaded.")
except FileNotFoundError:
    print("❌ ERROR: 'crop_revenue.csv' file nahi mila. Please ensure file is in the same folder.")
    exit()

# --- 2. Preprocessing and Feature Engineering ---
# Revenue aur Log Transformation
df['Revenue'] = df['Production'] * 1000
df['Log_Revenue'] = np.log1p(df['Revenue'])

# Cleaning and Log Transformations for skewed features
df['Season'] = df['Season'].str.strip()
df['Crop'] = df['Crop'].str.strip()
df['State'] = df['State'].str.strip()
df['Log_Area'] = np.log1p(df['Area'])
df['Log_Fertilizer'] = np.log1p(df['Fertilizer'])
df['Log_Pesticide'] = np.log1p(df['Pesticide'])
df['Log_Yield'] = np.log1p(df['Yield'])

# Feature Selection
features_to_drop = ['Area', 'Production', 'Fertilizer', 'Pesticide', 'Yield', 'Revenue', 'Log_Revenue', 'Annual_Rainfall']
X = df.drop(columns=features_to_drop)
y = df['Log_Revenue']

# One-Hot Encoding
X = pd.get_dummies(X, columns=['Crop', 'Season', 'State', 'Crop_Year'], drop_first=True)

# Final features
feature_cols = [col for col in X.columns if col.startswith(('Log_', 'Crop_', 'Season_', 'State_', 'Crop_Year_'))]
X = X[feature_cols]
X = X.fillna(0) 

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("✅ Data Preprocessing and Splitting Complete.")


# --- 3. Model Training and Comparison ---
models = {
    'Linear Regression': LinearRegression(),
    'Random Forest Regressor': RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1, max_depth=15),
    'Gradient Boosting Regressor': GradientBoostingRegressor(n_estimators=100, random_state=42, max_depth=5, learning_rate=0.1)
}

results = {}
fitted_models = {}

print("--- Starting Model Training ---")
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    results[name] = {'R2 Score (Log)': r2}
    fitted_models[name] = model
    print(f"{name} R2 Score (Log): {r2:.4f}")

# Best Model Selection
best_model_name = max(results, key=lambda name: results[name]['R2 Score (Log)'])
best_model = fitted_models[best_model_name]
print(f"🏆 Selected Best Model: {best_model_name}")

# --- 4. Model Saving (Joblib Files) ---
model_filename = f'{best_model_name.replace(" ", "_")}_revenue_predictor.joblib'
ohe_columns_filename = 'ohe_feature_columns.joblib'

# Save Model
joblib.dump(best_model, model_filename)
# Save OHE Columns
joblib.dump(X.columns.tolist(), ohe_columns_filename)

print("\n--- Model Saving Status ---")
print(f"✅ Model Saved: {model_filename}")
print(f"✅ OHE Columns Saved: {ohe_columns_filename}")
print(f"📂 Files saved in: {os.getcwd()}") # Prints the current directory